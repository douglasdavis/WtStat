#ifndef WTSTAT_UTILS_H
#define WTSTAT_UTILS_H

#include <TH1D.h>
#include <ROOT/RResultPtr.hxx>
#include <ROOT/RDFInterface.hxx>

namespace wts {

  using Filter_t = ROOT::RDF::RInterface<ROOT::Detail::RDF::RJittedFilter, void>;
  using FilterTable_t = std::map<std::string, wtf::Filter_t>;

  struct RHModel {
    RHModel(int n, float min, float max, std::string v, std::string w) {
      nbins = n;
      xmin = min;
      xmax = max;
      var = v;
      weight = w;
    }
    int nbins;
    double xmin;
    double xmax;
    std::string var;
    std::string weight;
  };

  void saveToFile(ROOT::RDF::RResultPtr<TH1D>& h, TFile* f);
  void shiftOverflowAndScale(TH1D* h, float lumi = 1.0);
}

#endif
