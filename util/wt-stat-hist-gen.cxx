// WtStat
#include <WtStat/TemplateSet.h>
#include <WtStat/Utils.h>
// TopLoop
#include <TopLoop/spdlog/fmt/fmt.h>
#include <TopLoop/json/json.hpp>
// WtLoop
#include <WtLoop/Externals/CLI11.hpp>

int main(int argc, char* argv[]) {
  CLI::App app{"Make histograms for the tW fit"};
  std::vector<std::string> inputFiles;
  std::string treePref = "WtTMVA";
  std::string treeSuff = "nominal";
  std::string templateSetName;
  std::string outFileName;
  std::string jsonFileName;
  bool doWeights;
  bool singlethreaded = false;
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
  app.add_option("-j,--json-config", jsonFileName,
                 "json file defining templates and filters")
      ->required()
      ->check(CLI::ExistingFile);
  app.add_flag("--no-multithread", singlethreaded, "run ROOT::EnableImplicitMT()");

  CLI11_PARSE(app, argc, argv);

  if (!singlethreaded) {
    ROOT::EnableImplicitMT();
  }

  std::ifstream in(jsonFileName.c_str());
  auto j = nlohmann::json::parse(in);

  wts::FilterDefs_t filters;
  for (const auto& filt : j["filters"]) {
    double xmin = 0;
    double xmax = 0;
    if (filt.find("xmin") != filt.end() && filt.find("xmax") != filt.end()) {
      xmin = filt["xmin"].get<double>();
      xmax = filt["xmax"].get<double>();
    }
    filters.emplace(
        std::make_pair(filt["name"].get<std::string>(),
                       std::make_tuple(filt["filter"].get<std::string>(), xmin, xmax)));
  }

  wts::TemplateSet templateSet(templateSetName, treePref, treeSuff, doWeights);
  templateSet.setFiles(inputFiles);
  templateSet.setExtraWeights(extraWeights);

  for (const auto& htemplate : j["templates"]) {
    templateSet.addHTemplate({htemplate["nbins"].get<int>(), htemplate["xmin"].get<float>(),
                              htemplate["xmax"].get<float>(),
                              htemplate["var"].get<std::string>(),
                              htemplate["use_filter_extrema"].get<bool>()});
  }

  auto outFile = TFile::Open(outFileName.c_str(), "UPDATE");
  templateSet.flowThroughFilters(filters, outFile);
  outFile->Close();

  return 0;
}
