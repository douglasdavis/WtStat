#include <WtStat/TemplateSet.h>
#include <TopLoop/spdlog/fmt/fmt.h>
#include <TopLoop/spdlog/sinks/stdout_color_sinks.h>

#include <TChain.h>
#include <ROOT/RDataFrame.hxx>
#include <ROOT/RDFHistoModels.hxx>

wts::TemplateSet::TemplateSet(const std::string& name,
                              const std::string& treePref,
                              bool doWeightSys,
                              bool doTreeSys) :
  m_name(name),
  m_treePref(treePref),
  m_doWeightSys(doWeightSys),
  m_doTreeSys(doTreeSys) {

  m_logger = spdlog::stdout_color_st(name);
}

void wts::TemplateSet::flowThroughFilters(const wts::FilterDefs_t& filters, TFile* outFile) const {
  nlohmann::json j_top;
  if (doWeightSys()) {
    j_top = wts::getSystematicJson();
  }

  std::string nom_name = fmt::format("{}_nominal", m_treePref);
  TChain c(nom_name.c_str());
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


  std::vector<HResult_t> histograms;

  for (const auto& ifilter : filterTable) {
    auto filterName = std::get<0>(ifilter);
    auto filter = std::get<1>(ifilter);
    for (const auto& htemplate : m_histTemplates) {
      std::string hname = fmt::format("{}_{}_{}", filterName, htemplate.var, m_name);
      histograms.push_back(filter.Histo1D(ROOT::RDF::TH1DModel(hname.c_str(),
                                                               hname.c_str(),
                                                               htemplate.nbins,
                                                               htemplate.xmin,
                                                               htemplate.xmax),
                                          htemplate.var, "weight_nominal"));
      if (doWeightSys()) {
        auto sysWeightNode = j_top["SYS_WEIGHTS"];
        for (const auto& entry : sysWeightNode.items()) {
          auto hname_up = fmt::format("{}_{}_Up", hname, entry.key());
          auto hname_down = fmt::format("{}_{}_Down", hname, entry.key());
          auto wn_up  = entry.value()["up"].get<std::string>();
          auto wn_down = entry.value()["down"].get<std::string>();
          histograms.push_back(filter.Histo1D(ROOT::RDF::TH1DModel(hname_up.c_str(),
                                                                   hname_up.c_str(),
                                                                   htemplate.nbins,
                                                                   htemplate.xmin,
                                                                   htemplate.xmax),
                                              htemplate.var, wn_up));
          histograms.push_back(filter.Histo1D(ROOT::RDF::TH1DModel(hname_down.c_str(),
                                                                   hname_down.c_str(),
                                                                   htemplate.nbins,
                                                                   htemplate.xmin,
                                                                   htemplate.xmax),
                                              htemplate.var, wn_down));
        }
      }

    }
  }
  for (auto& h : histograms) {
    wts::saveToFile(h, outFile);
  }
}
