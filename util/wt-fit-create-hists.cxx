#include <TopLoop/spdlog/fmt/fmt.h>
#include <WtLoop/Externals/CLI11.hpp>
#include <WtStat/Utils.h>

#include <TChain.h>
#include <ROOT/RDataFrame.hxx>
#include <ROOT/RDFHistoModels.hxx>

#include <iostream>

void aSet(const std::vector<std::string>& fileNames, const std::vector<wts::RHModel>& templates,
          const std::string& treeName, const std::string& sampleName, const std::string& suffix,
          bool isUp, bool isDown, TFile* outFile) {
  TChain c(treeName.c_str());
  for (const auto f : fileNames) {
    c.Add(f.c_str());
  }
  ROOT::RDataFrame df(c, {});
  wts::FilterTable_t filters = {
    {"SR_1j1b", df.Filter("reg1j1b&&elmu&&OS", "1j1b")},
    {"SR_2j1b", df.Filter("reg2j1b&&elmu&&OS", "2j1b")},
    {"SR_2j2b", df.Filter("reg2j2b&&elmu&&OS", "2j2b")}
  };

  std::string upOrDown = "";
  if (isUp) upOrDown = "_Up";
  if (isDown) upOrDown = "_Down";

  std::vector<ROOT::RDF::RResultPtr<TH1D>> histograms;

  for (const auto& ifilter : filters) {
    std::string filterName = std::get<0>(ifilter);
    auto f = std::get<1>(ifilter);
    for (const auto& htemplate : templates) {
      // {Region}_{variable}_{Sample}_{sysname}_{up/down}
      std::string name = fmt::format("{}_{}_{}{}{}",
                                     filterName, htemplate.var, sampleName, suffix, upOrDown);
      histograms.push_back(f.Histo1D(ROOT::RDF::TH1DModel(name.c_str(), name.c_str(),
                                                          htemplate.nbins, htemplate.xmin, htemplate.xmax),
                                     htemplate.var, htemplate.weight));
    }
  }

  for (auto& h : histograms) {
    wts::saveToFile(h, outFile);
  }
}

int main(int argc, char *argv[]) {
  CLI::App app{"Make histograms for the tW fit"};
  std::vector<std::string> inputFiles;
  std::string treeName = "WtTMVA_nominal";
  std::string weightBranch = "weight_nominal";
  std::string outFileName;
  auto inputFiles_o = app.add_option("-i,--input-files", inputFiles, "input ROOT files")
    ->required()
    ->check(CLI::ExistingFile);
  auto treeName_o = app.add_option("-t,--tree-name", treeName, "tree name to parse");
  auto weightBranch_o = app.add_option("-w,--weight-name", weightBranch, "weight branch to use");
  auto outFile_o = app.add_option("-o,--out-file", outFileName, "output file name")->required();
  CLI11_PARSE(app, argc, argv);

  ///////////////////

  ROOT::EnableImplicitMT();

  std::vector<wts::RHModel> templates;
  templates.emplace_back(50, 27., 277., std::string("pT_lep1"), std::string("weight_nominal"));
  templates.emplace_back(50, 20., 170., std::string("pT_lep2"), std::string("weight_nominal"));
  templates.emplace_back(50, 25., 275., std::string("pT_jet1"), std::string("weight_nominal"));

  auto outFile = TFile::Open(outFileName.c_str(), "UPDATE");

  aSet(inputFiles, templates, "WtLoop_nominal", "tW", "", false, false, outFile);

  outFile->Close();

  return 0;
}
