#include <WtStat/Utils.h>
#include <TH1D.h>
#include <TopLoop/spdlog/fmt/fmt.h>

namespace wts {

  void shiftOverflowAndScale(TH1D* h, float lumi) {
    int nb = h->GetNbinsX();

    double v_under = h->GetBinContent(0);
    double v_over = h->GetBinContent(nb+1);

    double e_under = h->GetBinError(0);
    double e_over = h->GetBinError(nb+1);

    double v_first = h->GetBinContent(1);
    double v_last = h->GetBinContent(nb);

    double e_first = h->GetBinError(1);
    double e_last = h->GetBinError(nb);

    h->SetBinContent(1, v_under + v_first);
    h->SetBinContent(nb, v_over + v_last);
    h->SetBinError(1, std::sqrt(e_under*e_under + e_first*e_first));
    h->SetBinError(nb, std::sqrt(e_over*e_over + e_last*e_last));

    h->Scale(lumi);
  }

  void saveToFile(ROOT::RDF::RResultPtr<TH1D>& h, TFile* f) {
    if (f->GetListOfKeys()->Contains(h->GetName())) {
      auto msg = fmt::format("File contains {}, skipping",
                             h->GetName());
      std::cout << msg << std::endl;
      return;
    }
    shiftOverflowAndScale(h.GetPtr(), 140.5);
    h->SetDirectory(f);
    h->Write();
  }

}
