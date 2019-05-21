#ifndef WTSTAT_UTILS_H
#define WTSTAT_UTILS_H

// TopLoop
#include <TopLoop/json/json.hpp>

// ROOT
#include <TH1D.h>
#include <ROOT/RResultPtr.hxx>

#if ROOT_VERSION_CODE < ROOT_VERSION(6, 16, 00)
#include <ROOT/RDFInterface.hxx>
#else
#include <ROOT/RDF/InterfaceUtils.hxx>
#endif

// C++
#include <map>
#include <string>

namespace wts {

#if ROOT_VERSION_CODE < ROOT_VERSION(6, 16, 00)
using Filter_t = ROOT::RDF::RInterface<ROOT::Detail::RDF::RJittedFilter, void>;
#else
using Filter_t = ROOT::RDF::RNode;
#endif
using FilterDefs_t = std::map<std::string, std::tuple<std::string, double, double, int>>;
using FilterTable_t = std::map<std::string, std::tuple<wts::Filter_t, double, double, int>>;
using HResult_t = ROOT::RDF::RResultPtr<TH1D>;

/// simple struct to define a template histogram
struct HTemplate {
  HTemplate(int n, float min, float max, std::string v, bool ufe,
            const std::vector<std::string>& filts)
      : nbins(n), xmin(min), xmax(max), var(v), use_filter_minmax(ufe), filters(filts) {}
  int nbins;
  double xmin;
  double xmax;
  std::string var;
  bool use_filter_minmax;
  std::vector<std::string> filters;
};

/// save a histogram \p h from RDF Filter to file \p f
void saveToFile(ROOT::RDF::RResultPtr<TH1D>& h, TFile* f);
/// shift under and overflow bins of \p h and scale to \p lumi
void shiftOverflowAndScale(TH1D* h, float lumi = 1.0);
/// clean helper function for grabbing systematic json info
nlohmann::json getSystematicJson();

/// check for entry in vector
template <class T>
bool inVec(const std::vector<T>& v, const T& val) {
  if (std::find(std::begin(v), std::end(v), val) != std::end(v)) return true;
  return false;
}

}  // namespace wts

#endif
