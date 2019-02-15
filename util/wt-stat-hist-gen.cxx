#include <TopLoop/spdlog/fmt/fmt.h>
#include <WtLoop/Externals/CLI11.hpp>
#include <WtStat/Utils.h>
#include <WtStat/TemplateSet.h>


int main(int argc, char *argv[]) {
  CLI::App app{"Make histograms for the tW fit"};
  std::vector<std::string> inputFiles;
  std::string treePref = "WtTMVA";
  std::string templateSetName;
  std::string outFileName;
  auto inputFiles_o = app.add_option("-i,--input-files", inputFiles, "input ROOT files")->required()->check(CLI::ExistingFile);
  auto treeName_o = app.add_option("-t,--tree-pref", treePref, "tree prefix");
  auto templateSetName_o = app.add_option("-n,--name", templateSetName, "template set name")->required();
  auto outFile_o = app.add_option("-o,--out-file", outFileName, "output file name")->required();
  CLI11_PARSE(app, argc, argv);

  ROOT::EnableImplicitMT();

  wts::FilterDefs_t filters = {
    {"SR_1j1b",     "reg1j1b && elmu && OS"},
    {"SR_2j1b",     "reg2j1b && elmu && OS"},
    {"SR_2j2b",     "reg2j2b && elmu && OS"},
    {"SR_2j2bmblc", "reg2j2b && elmu && OS && minimaxmbl<150"},
    {"CR_3j",       "njets==3 && elmu && OS"},
    {"CR_4j",       "njets==3 && elmu && OS"},
    {"CR_3j1b",     "njets==3 && nbjets==1 && elmu && OS"},
    {"CR_4j1b",     "njets==4 && nbjets==1 && elmu && OS"},
    {"VR_ALL",      "elmu && OS"},
    {"VR_1j0b",     "reg1j0b && elmu && OS"},
    {"VR_2j0b",     "reg2j0b && elmu && OS"}
  };

  wts::TemplateSet templateSet(templateSetName, treePref, true, false);
  templateSet.setFiles(inputFiles);
  templateSet.addHTemplate({50, 27., 277., "pT_lep1"});
  templateSet.addHTemplate({50, 20., 170., "pT_lep2"});
  templateSet.addHTemplate({50, 25., 270., "pT_jet1"});
  templateSet.addHTemplate({50, 25., 175., "pT_jet2"});
  templateSet.addHTemplate({100, -1.0, 1.0, "bdt_response"});

  auto outFile = TFile::Open(outFileName.c_str(), "UPDATE");
  templateSet.flowThroughFilters(filters, outFile);
  outFile->Close();

  return 0;
}
