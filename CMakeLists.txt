## CMakeLists.txt for WtStat package to be built within ATLAS
## Analysis Relase 21.2.X series.
## Author: Doug Davis <ddavis@cern.ch>

# Declare the name of this package:
atlas_subdir(WtStat None)

# This package depends on other packages:
atlas_depends_on_subdirs(PUBLIC WtPyext)

# Install data files from the package:
atlas_install_data(data/*)

# Install python modules
atlas_install_python_modules(python/*)

# Install scripts
atlas_install_scripts(scripts/*)
