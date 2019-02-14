#ifndef WTSTAT_TEMPLATESET_H
#define WTSTAT_TEMPLATESET_H

#include <WtStat/Utils.h>

#include <TChain.h>

#include <vector>

namespace wts {
  class TemplateSet {
  private:
    std::string m_name;
    std::string m_treePref;
    bool m_doWeightSys;
    bool m_doTreeSys;
    std::vector<std::string> m_fileNames;
    std::vector<std::string> m_extraWeights;
    std::vector<wts::HTemplate> m_histTemplates;

  public:
    TemplateSet() = delete;
    virtual ~TemplateSet() = default;

    TemplateSet(TemplateSet&&) = default;
    TemplateSet(const TemplateSet&) = default;
    TemplateSet& operator=(TemplateSet&&) = default;
    TemplateSet& operator=(const TemplateSet&) = default;

    TemplateSet(const std::string& name,
                const std::string& treePref,
                bool doWeightSys = false,
                bool doTreeSys = false);

    void addFile(const std::string& fname) { m_fileNames.emplace_back(fname); }
    void setFiles(const std::vector<std::string>& files) { m_fileNames = files; }
    void addExtraWeight(const std::string& wname) { m_extraWeights.emplace_back(wname); }
    void addHTemplate(wts::HTemplate&& htemplate) { m_histTemplates.emplace_back(htemplate); }

    const std::string& name() const { return m_name; }
    const std::vector<std::string>& fileNames() { return m_fileNames; }
    bool doWeightSys() const { return m_doWeightSys; }
    bool doTreeSys() const { return m_doTreeSys; }

    void flowThroughFilters(const wts::FilterDefs_t& filters, TFile* outFile) const;

  };
}

#endif
