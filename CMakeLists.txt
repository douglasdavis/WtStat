## CMakeLists.txt for WtStat package to be built within ATLAS
## Analysis Relase 21.2.X series.
## Author: Doug Davis <ddavis@cern.ch>

# Declare the name of this package:
atlas_subdir( WtStat None )

# This package depends on other packages:
atlas_depends_on_subdirs( PUBLIC
  TopLoop
  WtLoop
  )

# This package uses ROOT:
find_package( ROOT REQUIRED COMPONENTS Physics Core Tree Hist RIO MathCore TreePlayer ROOTDataFrame ROOTVecOps Imt )

# Build a library that other components can link against:
atlas_add_library( WtStat
  WtStat/*.h Root/*.cxx Root/*.h
  PUBLIC_HEADERS WtStat
  SHARED
  LINK_LIBRARIES TopLoop
  PRIVATE_LINK_LIBRARIES ${ROOT_LIBRARIES}
  PRIVATE_INCLUDE_DIRS ${ROOT_INCLUDE_DIRS} )

#add_dependencies( WtStat yaml-cpp )

#atlas_add_dictionary( WtStatDict
#  WtStat/WtStatDict.h WtStat/selection.xml
#  LINK_LIBRARIES WtStat )

# Install data files from the package:
atlas_install_data( data/* )

# Install python modules
atlas_install_python_modules( python/* )

# Install scripts
atlas_install_scripts( scripts/* )

atlas_add_executable( wt-fit-create-hists
  util/wt-fit-create-hists.cxx
  LINK_LIBRARIES ${ROOT_LIBRARIES} WtStat TopLoop )
