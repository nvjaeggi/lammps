# Preset that turns on all existing packages. Using the combination
# of this preset followed by the nolib.cmake preset should configure
# a LAMMPS binary, with as many packages included, that can be compiled
# with just a working C++ compiler and an MPI library.

set(VESICLES_PACKAGES
  EXTRA-DUMP
  EXTRA-PAIR
  KSPACE
  MANYBODY
  MOLECULE
  REAXFF
  RIGID
  VORONOI
  )

foreach(PKG ${VESICLES_PACKAGES})
  set(PKG_${PKG} ON CACHE BOOL "" FORCE)
endforeach()
