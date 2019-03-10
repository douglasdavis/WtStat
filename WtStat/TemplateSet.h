#ifndef WTSTAT_TEMPLATESET_H
#define WTSTAT_TEMPLATESET_H

// WtStat
#include <WtStat/Utils.h>
// TopLoop
#include <TopLoop/spdlog/spdlog.h>
// ROOT
#include <TChain.h>
// C++
#include <memory>
#include <vector>

namespace wts {
class TemplateSet {
 private:
  std::string m_name;
  std::string m_treePref;
  std::string m_treeSuff;
  bool m_doSysWeights;
  std::vector<std::string> m_fileNames;
  std::vector<std::string> m_extraWeights;
  std::vector<wts::HTemplate> m_histTemplates;
  std::shared_ptr<spdlog::logger> m_logger;
  nlohmann::json m_sysJson;

 public:
  TemplateSet() = delete;
  virtual ~TemplateSet() = default;

  TemplateSet(TemplateSet&&) = default;
  TemplateSet(const TemplateSet&) = default;
  TemplateSet& operator=(TemplateSet&&) = default;
  TemplateSet& operator=(const TemplateSet&) = default;

  TemplateSet(const std::string& name, const std::string& treePref,
              const std::string& treeSuff, bool doSysWeights = false);

  void addFile(const std::string& fname) { m_fileNames.emplace_back(fname); }
  void setFiles(const std::vector<std::string>& files) { m_fileNames = files; }
  void addExtraWeight(const std::string& wname) { m_extraWeights.emplace_back(wname); }
  void setExtraWeights(const std::vector<std::string>& names) { m_extraWeights = names; }
  void addHTemplate(wts::HTemplate&& htemplate) { m_histTemplates.emplace_back(htemplate); }

  const std::string& name() const { return m_name; }
  const std::vector<std::string>& fileNames() { return m_fileNames; }
  bool doSysWeights() const { return m_doSysWeights; }

  void flowThroughFilters(const wts::FilterDefs_t& filters, TFile* outFile) const;
  void flowOnSysWeights(wts::Filter_t& filter, const std::string& filterName,
                        std::vector<HResult_t>& histograms, double filterXmin,
                        double filterXmax, TFile* outFile) const;
};
}  // namespace wts

#endif
