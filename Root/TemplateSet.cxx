// WtStat
#include <WtStat/TemplateSet.h>
// TopLoop
#include <TopLoop/spdlog/fmt/fmt.h>
#include <TopLoop/spdlog/sinks/stdout_color_sinks.h>
// ROOT
#include <TChain.h>
#include <ROOT/RDFHistoModels.hxx>
#include <ROOT/RDataFrame.hxx>

wts::TemplateSet::TemplateSet(const std::string& name, const std::string& treePref,
                              const std::string& treeSuff, bool doSysWeights)
    : m_name(name),
      m_treePref(treePref),
      m_treeSuff(treeSuff),
      m_doSysWeights(doSysWeights) {
  m_logger = spdlog::stdout_color_st(name);
  m_sysJson = wts::getSystematicJson();
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

  FilterTable_t filterTable;
  for (const auto& ifd : filters) {
    auto fname = std::get<0>(ifd);
    auto filt = std::get<1>(ifd);
    filterTable.emplace(std::make_pair(fname, nom_df.Filter(filt, fname)));
  }

  std::string exsuff = "";
  if (m_treeSuff != "nominal") {
    exsuff = fmt::format("_{}", m_treeSuff);
  }

  std::vector<HResult_t> histograms;

  for (const auto& ifilter : filterTable) {
    auto filterName = std::get<0>(ifilter);
    auto filter = std::get<1>(ifilter);
    for (const auto& htemplate : m_histTemplates) {
      std::string hname =
          fmt::format("{}_{}_{}{}", filterName, htemplate.var, m_name, exsuff);
      histograms.push_back(
          filter.Histo1D(ROOT::RDF::TH1DModel(hname.c_str(), hname.c_str(), htemplate.nbins,
                                              htemplate.xmin, htemplate.xmax),
                         htemplate.var, "weight_nominal"));
    }

    // only do extra weight stuff if nominal
    if (m_treeSuff == "nominal") {
      // do the systematic weights
      if (doSysWeights()) {
        flowOnSysWeights(filter, filterName, histograms);
      }
      // do extra weights
      for (auto const& xw : m_extraWeights) {
        for (const auto& htemplate : m_histTemplates) {
          std::string xwshort = xw;
          std::string removethis = "weight_sys_";
          auto findws = xwshort.find(removethis);
          xwshort.erase(findws, removethis.length());
          std::cout << xwshort << " " << xw << std::endl;
          std::string hname =
              fmt::format("{}_{}_{}_{}", filterName, htemplate.var, m_name, xwshort);
          histograms.push_back(filter.Histo1D(
              ROOT::RDF::TH1DModel(hname.c_str(), hname.c_str(), htemplate.nbins,
                                   htemplate.xmin, htemplate.xmax),
              htemplate.var, xw));
        }
      }
    }
  }

  for (auto& h : histograms) {
    wts::saveToFile(h, outFile);
  }
}

void wts::TemplateSet::flowOnSysWeights(wts::Filter_t& filter,
                                        const std::string& filterName,
                                        std::vector<HResult_t>& histograms) const {
  if (m_treeSuff != "nominal") {
    m_logger->warn(
        "You asked for weight systematics on a systematic tree. Nope. "
        "bail bail bail");
    return;
  }
  auto sysWeightNode = m_sysJson["SYS_WEIGHTS"];

  for (const auto& htemplate : m_histTemplates) {
    std::string hname = fmt::format("{}_{}_{}", filterName, htemplate.var, m_name);

    for (const auto& entry : sysWeightNode.items()) {
      auto hname_up = fmt::format("{}_{}_Up", hname, entry.key());
      auto hname_down = fmt::format("{}_{}_Down", hname, entry.key());
      auto wn_up = entry.value()["up"].get<std::string>();
      auto wn_down = entry.value()["down"].get<std::string>();
      histograms.push_back(filter.Histo1D(
          ROOT::RDF::TH1DModel(hname_up.c_str(), hname_up.c_str(), htemplate.nbins,
                               htemplate.xmin, htemplate.xmax),
          htemplate.var, wn_up));
      histograms.push_back(filter.Histo1D(
          ROOT::RDF::TH1DModel(hname_down.c_str(), hname_down.c_str(), htemplate.nbins,
                               htemplate.xmin, htemplate.xmax),
          htemplate.var, wn_down));
    }
  }
}
