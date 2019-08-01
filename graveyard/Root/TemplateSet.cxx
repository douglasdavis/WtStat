// WtStat
#include <WtStat/TemplateSet.h>
// TopLoop
#include <TopLoop/spdlog/fmt/fmt.h>
// avoid clang-format reorder
#include <TopLoop/spdlog/sinks/stdout_color_sinks.h>

// ROOT
#include <TChain.h>
#include <ROOT/RDataFrame.hxx>

#if ROOT_VERSION_CODE < ROOT_VERSION(6, 16, 00)
#include <ROOT/RDFHistoModels.hxx>
#else
#include <ROOT/RDF/HistoModels.hxx>
#endif

wts::TemplateSet::TemplateSet(const std::string& name, const std::string& treePref,
                              const std::string& treeSuff, bool doSysWeights)
    : m_name(name),
      m_treePref(treePref),
      m_treeSuff(treeSuff),
      m_doSysWeights(doSysWeights) {
  m_logger = spdlog::stdout_color_st(name);
  m_sysJson = wts::getSystematicJson();
  spdlog::set_pattern("%n   %^[%=9l]%$   %v");
}

void wts::TemplateSet::flowThroughFilters(const wts::FilterDefs_t& filters,
                                          TFile* outFile) const {
  std::string tree_name = fmt::format("{}_{}", m_treePref, m_treeSuff);
  TChain c(tree_name.c_str());
  for (const auto& f : m_fileNames) {
    c.Add(f.c_str());
    m_logger->info("Adding file {}", f);
  }
  ROOT::RDataFrame nom_df(c, {});

  double customXmin;
  double customXmax;
  int customNbin;

  m_logger->info("Registering the following filters:");
  std::string table_hline =
      fmt::format("+-{:-^20}-+-{:-^50}-+-{:-^7}-+-{:-^7}-+", "", "", "", "");
  m_logger->info(table_hline);
  m_logger->info("| {0:^20} | {1:^50} | {2:^7} | {3:^7} |", "Name", "Selection", "Min",
                 "Max");
  m_logger->info(table_hline);
  FilterTable_t filterTable;
  for (const auto& ifd : filters) {
    auto fname = std::get<0>(ifd);
    auto filttup = std::get<1>(ifd);
    auto filt = std::get<0>(filttup);
    customXmin = std::get<1>(filttup);
    customXmax = std::get<2>(filttup);
    customNbin = std::get<3>(filttup);
    filterTable.emplace(std::make_pair(
        fname,
        std::make_tuple(nom_df.Filter(filt, fname), customXmin, customXmax, customNbin)));
    m_logger->info("| {0:^20} | {1:^50} | {2:^7} | {3:^7} |", fname, filt, customXmin,
                   customXmax);
  }
  m_logger->info(table_hline);

  std::string exsuff = "";
  if (m_treeSuff != "nominal") {
    exsuff = fmt::format("_{}", m_treeSuff);
  }

  m_logger->info("Registering the following histogram templates:");
  table_hline = fmt::format("+-{:-^25}-+-{:-^19}-+-{:-^17}-+-{:-^12}-+", "", "", "", "");
  m_logger->info(table_hline);
  m_logger->info("| {0:^25} | {1:^19} | {2:^17} | {3:^12} |", "Variable", "Binning",
                 "Use Filter MinMax", "Filter");
  m_logger->info(table_hline);
  for (const auto& htemplate : m_histTemplates) {
    for (const auto& hft : htemplate.filters) {
      m_logger->info("| {0:^25} | [{1:>3}, {2:>5}, {3:>5}] | {4:^17} | {5:^12} |",
                     htemplate.var, htemplate.nbins, htemplate.xmin, htemplate.xmax,
                     htemplate.use_filter_minmax, hft);
    }
  }
  m_logger->info(table_hline);

  std::vector<HResult_t> histograms;

  for (const auto& ifilter : filterTable) {
    auto filterName = std::get<0>(ifilter);
    auto filterTuple = std::get<1>(ifilter);
    auto filter = std::get<0>(filterTuple);
    auto filterXmin = std::get<1>(filterTuple);
    auto filterXmax = std::get<2>(filterTuple);
    auto filterNbin = std::get<3>(filterTuple);

    for (const auto& htemplate : m_histTemplates) {
      if (!wts::inVec(htemplate.filters, filterName)) continue;
      float xmin = htemplate.xmin;
      float xmax = htemplate.xmax;
      int nbin = htemplate.nbins;
      if (htemplate.use_filter_minmax) {
        xmin = filterXmin;
        xmax = filterXmax;
        nbin = filterNbin;
      }

      std::string hname =
          fmt::format("{}_{}_{}{}", filterName, htemplate.var, m_name, exsuff);
      if (outFile->GetListOfKeys()->Contains(hname.c_str())) {
        m_logger->warn("Skipping {} because it's already in the output file", hname);
      }
      else {
        histograms.push_back(filter.Histo1D(
            ROOT::RDF::TH1DModel(hname.c_str(), hname.c_str(), nbin, xmin, xmax),
            htemplate.var, "weight_nominal"));
      }
    }

    // only do extra weight stuff if nominal
    if (m_treeSuff == "nominal") {
      // do the systematic weights
      if (doSysWeights()) {
        flowOnSysWeights(filter, filterName, histograms, filterXmin, filterXmax, filterNbin,
                         outFile);
      }
      // do extra weights
      for (auto const& xw : m_extraWeights) {
        for (const auto& htemplate : m_histTemplates) {
          if (!wts::inVec(htemplate.filters, filterName)) continue;
          float xmin = htemplate.xmin;
          float xmax = htemplate.xmax;
          int nbin = htemplate.nbins;
          if (htemplate.use_filter_minmax) {
            xmin = filterXmin;
            xmax = filterXmax;
            nbin = filterNbin;
          }

          std::string xwshort = xw;
          std::string removethis = "weight_sys_";
          auto findws = xwshort.find(removethis);
          xwshort.erase(findws, removethis.length());
          std::string hname =
              fmt::format("{}_{}_{}_{}", filterName, htemplate.var, m_name, xwshort);
          if (outFile->GetListOfKeys()->Contains(hname.c_str())) {
            m_logger->warn("Skipping {} because it's already in the output file", hname);
          }
          else {
            histograms.push_back(filter.Histo1D(
                ROOT::RDF::TH1DModel(hname.c_str(), hname.c_str(), nbin, xmin, xmax),
                htemplate.var, xw));
          }
        }
      }
    }
  }

  if (histograms.empty()) return;
  m_logger->info("Evaulation starting");
  for (auto& h : histograms) {
    wts::saveToFile(h, outFile);
  }
  m_logger->info("Evaulation done");
}

void wts::TemplateSet::flowOnSysWeights(wts::Filter_t& filter,
                                        const std::string& filterName,
                                        std::vector<HResult_t>& histograms,
                                        double filterXmin, double filterXmax,
                                        int filterNbin, TFile* outFile) const {
  if (m_treeSuff != "nominal") {
    m_logger->warn(
        "You asked for weight systematics on a systematic tree. Nope. "
        "bail bail bail");
    return;
  }
  auto sysWeightNode = m_sysJson["SYS_WEIGHTS"];
  auto pdfWeightNode = m_sysJson["PDF_WEIGHTS"];

  for (const auto& htemplate : m_histTemplates) {
    if (!wts::inVec(htemplate.filters, filterName)) continue;
    std::string hname = fmt::format("{}_{}_{}", filterName, htemplate.var, m_name);

    for (const auto& entry : sysWeightNode.items()) {
      auto hname_up = fmt::format("{}_{}_Up", hname, entry.key());
      auto hname_down = fmt::format("{}_{}_Down", hname, entry.key());
      auto wn_up = entry.value()["up"].get<std::string>();
      auto wn_down = entry.value()["down"].get<std::string>();
      float xmin = htemplate.xmin;
      float xmax = htemplate.xmax;
      int nbin = htemplate.nbins;
      if (htemplate.use_filter_minmax) {
        xmin = filterXmin;
        xmax = filterXmax;
        nbin = filterNbin;
      }

      if (outFile->GetListOfKeys()->Contains(hname_up.c_str())) {
        m_logger->warn("Skipping {} because it's already in the output file", hname);
      }
      else {
        histograms.push_back(filter.Histo1D(
            ROOT::RDF::TH1DModel(hname_up.c_str(), hname_up.c_str(), nbin, xmin, xmax),
            htemplate.var, wn_up));
      }
      if (outFile->GetListOfKeys()->Contains(hname_down.c_str())) {
        m_logger->warn("Skipping {} because it's already in the output file", hname);
      }
      else {
        histograms.push_back(filter.Histo1D(
            ROOT::RDF::TH1DModel(hname_down.c_str(), hname_down.c_str(), nbin, xmin, xmax),
            htemplate.var, wn_down));
      }
    }

    for (const auto& entry : pdfWeightNode.items()) {
      auto hname_up = fmt::format("{}_{}", hname, entry.key());
      auto wn_up = entry.value()["up"].get<std::string>();
      float xmin = htemplate.xmin;
      float xmax = htemplate.xmax;
      int nbin = htemplate.nbins;
      if (htemplate.use_filter_minmax) {
        xmin = filterXmin;
        xmax = filterXmax;
        nbin = filterNbin;
      }

      if (outFile->GetListOfKeys()->Contains(hname_up.c_str())) {
        m_logger->warn("Skipping {} because it's already in the output file", hname);
      }
      else {
        histograms.push_back(filter.Histo1D(
            ROOT::RDF::TH1DModel(hname_up.c_str(), hname_up.c_str(), nbin, xmin, xmax),
            htemplate.var, wn_up));
      }
    }
  }
}
