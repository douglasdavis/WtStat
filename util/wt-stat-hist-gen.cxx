// yaml-cpp
#include <yaml-cpp/yaml.h>
// WtStat
#include <WtStat/TemplateSet.h>
#include <WtStat/Utils.h>
// TopLoop
#include <TopLoop/spdlog/fmt/fmt.h>
// WtLoop
#include <WtLoop/Externals/CLI11.hpp>
// C++
#include <map>


int main(int argc, char* argv[]) {
  CLI::App app{"Make histograms for the tW fit"};
  std::vector<std::string> inputFiles;
  std::string treePref = "WtTMVA";
  std::string treeSuff = "nominal";
  std::string templateSetName;
  std::string outFileName;
  std::string yamlFileName;
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
  app.add_option("-y,--yaml-config", yamlFileName,
                 "yaml file defining templates and filters")
      ->required()
      ->check(CLI::ExistingFile);
  app.add_flag("--no-multithread", singlethreaded, "run ROOT::EnableImplicitMT()");

  CLI11_PARSE(app, argc, argv);

  if (!singlethreaded) {
    ROOT::EnableImplicitMT();
  }

  YAML::Node yaml_top = YAML::LoadFile(yamlFileName);
  auto yaml_filters = yaml_top["filters"];
  auto yaml_templates = yaml_top["templates"];

  wts::FilterDefs_t filters;
  for (const auto& filt : yaml_filters) {
    double xmin = 0;
    double xmax = 0;
    std::string y_name = filt["name"].as<std::string>();
    std::string y_filt = filt["filter"].as<std::string>();
    if (filt["xmin"] && filt["xmax"]) {
      xmin = filt["xmin"].as<float>();
      xmax = filt["xmax"].as<float>();
    }
    filters.emplace(std::make_pair(y_name, std::make_tuple(y_filt, xmin, xmax)));
  }

  wts::TemplateSet templateSet(templateSetName, treePref, treeSuff, doWeights);
  templateSet.setFiles(inputFiles);
  templateSet.setExtraWeights(extraWeights);

  for (const auto& htemplate : yaml_templates) {
    std::vector<std::string> filtersfortemplate;
    for (const auto& filtname : htemplate["filters"] ) {
      filtersfortemplate.push_back(filtname.as<std::string>());
    }
    templateSet.addHTemplate({htemplate["nbins"].as<int>(), htemplate["xmin"].as<float>(),
                              htemplate["xmax"].as<float>(),
                              htemplate["var"].as<std::string>(),
                              htemplate["use_filter_extrema"].as<bool>(),
                              filtersfortemplate});
  }

  auto outFile = TFile::Open(outFileName.c_str(), "UPDATE");
  templateSet.flowThroughFilters(filters, outFile);
  outFile->Close();

  return 0;
}
