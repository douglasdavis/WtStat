#ifndef WTSTAT_UTILS_H
#define WTSTAT_UTILS_H

// TopLoop
#include <TopLoop/json/json.hpp>
// ROOT
#include <TH1D.h>
#include <ROOT/RResultPtr.hxx>
#include <ROOT/RDFInterface.hxx>
// C++
#include <map>
#include <string>

namespace wts {

  using FilterDefs_t = std::map<std::string, std::string>;
  using Filter_t = ROOT::RDF::RInterface<ROOT::Detail::RDF::RJittedFilter, void>;
  using FilterTable_t = std::map<std::string, wts::Filter_t>;
  using HResult_t = ROOT::RDF::RResultPtr<TH1D>;

  struct HTemplate {
    HTemplate(int n, float min, float max, std::string v)
      : nbins(n), xmin(min), xmax(max), var(v) {}
    int nbins;
    double xmin;
    double xmax;
    std::string var;
  };

  void saveToFile(ROOT::RDF::RResultPtr<TH1D>& h, TFile* f);
  void shiftOverflowAndScale(TH1D* h, float lumi = 1.0);
  nlohmann::json getSystematicJson();
}

#endif
