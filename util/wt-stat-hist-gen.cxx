// WtStat
#include <WtStat/TemplateSet.h>
#include <WtStat/Utils.h>
// TopLoop
#include <TopLoop/spdlog/fmt/fmt.h>
// WtLoop
#include <WtLoop/Externals/CLI11.hpp>

int main(int argc, char *argv[]) {
  CLI::App app{"Make histograms for the tW fit"};
  std::vector<std::string> inputFiles;
  std::string treePref = "WtTMVA";
  std::string treeSuff = "nominal";
  std::string templateSetName;
  std::string outFileName;
  bool doWeights;
  std::vector<std::string> extraWeights{};
  app.add_option("-i,--input-files", inputFiles, "input ROOT files")
      ->required()
      ->check(CLI::ExistingFile);
  app.add_option("-t,--tree-pref", treePref, "tree prefix");
  app.add_option("-s,--tree-suff", treeSuff, "tree suffix");
  app.add_option("-n,--name", templateSetName, "template set name")->required();
  app.add_option("-o,--out-file", outFileName, "output file name")->required();
  app.add_flag("-w,--do-weights", doWeights, "process systematic weights");
  app.add_option("-x,--extra-weights", extraWeights, "extra weights to process");

  CLI11_PARSE(app, argc, argv);

  ROOT::EnableImplicitMT();

  wts::FilterDefs_t filters = {{"SR_1j1b", "reg1j1b && elmu && OS"},
                               {"SR_2j1b", "reg2j1b && elmu && OS"},
                               {"SR_2j2b", "reg2j2b && elmu && OS"},
                               {"SR_2j2bmblc", "reg2j2b && elmu && OS && minimaxmbl<150"},
                               {"CR_3j", "njets==3 && elmu && OS"},
                               {"CR_4j", "njets==3 && elmu && OS"},
                               {"CR_3j1b", "njets==3 && nbjets==1 && elmu && OS"},
                               {"CR_4j1b", "njets==4 && nbjets==1 && elmu && OS"},
                               {"VR_ALL", "elmu && OS"},
                               {"VR_1j0b", "reg1j0b && elmu && OS"},
                               {"VR_2j0b", "reg2j0b && elmu && OS"}};

  wts::TemplateSet templateSet(templateSetName, treePref, treeSuff, doWeights);
  templateSet.setFiles(inputFiles);
  templateSet.setExtraWeights(extraWeights);
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
