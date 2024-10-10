Name:           trick
Version:        1.0
Release:        1%{?dist}
Summary:        Contains the bin, include, and lib64 directories in the NASA Trick Simulation Development Framework necessary to run Trick-based simulations.

License:        National Aeronautics and Space Administration (NASA)
URL:            https://github.com/nasa/trick
Source0:        trick-1.0.tar.gz

Requires:       bison clang flex git llvm make maven swig cmake clang-devel gcc gcc-c++ java-11-openjdk-devel libxml2-devel llvm-devel llvm-static ncurses-devel openmotif openmotif-devel perl perl-Digest-MD5 udunits2 udunits2-devel which zlib-devel gtest-devel libX11-devel libXt-devel python3-devel diffutils



%description
This package contains the necessary directories from the NASA Trick Simulation Development Framework, specifically "bin", "include", "libexec", "er7_utils" and "lib64", required for running Trick-based simulations.

%prep
%setup -n include bin lib64 libexec trick_source/er7_utils

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin/trick/bin
mkdir -p %{buildroot}/usr/bin/trick/include/
mkdir -p %{buildroot}/usr/bin/trick/lib64
mkdir -p %{buildroot}/usr/bin/trick/libexec
#mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils

mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/rk2_heun/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/position_verlet/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/mm4/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/rk4/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/rkg4/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/rkn4/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/beeman/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/velocity_verlet/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/symplectic_euler/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/euler/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/core/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/abm4/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/rk2_midpoint/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/rkf78/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/nl2/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/rkf45/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/trick/integration/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/trick/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/interface/include
mkdir -p %{buildroot}/usr/bin/trick/trick_source/er7_utils/math/include

# Copy the files to the appropriate locations
cp -r ${TRICK_HOME}/bin %{buildroot}/usr/bin/trick/bin/
cp -r ${TRICK_HOME}/include %{buildroot}/usr/bin/trick/include/
cp -r ${TRICK_HOME}/lib64 %{buildroot}/usr/bin/trick/lib64/
cp -r ${TRICK_HOME}/libexec %{buildroot}/usr/bin/trick/libexec
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/rk2_heun/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/rk2_heun/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/position_verlet/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/position_verlet/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/mm4/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/mm4/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/rk4/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/rk4/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/rkg4/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/rkg4/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/rkn4/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/rkn4/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/beeman/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/beeman/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/velocity_verlet/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/velocity_verlet/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/symplectic_euler/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/symplectic_euler/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/euler/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/euler/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/core/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/core/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/abm4/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/abm4/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/rk2_midpoint/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/rk2_midpoint/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/rkf78/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/rkf78/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/nl2/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/nl2/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/integration/rkf45/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/integration/rkf45/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/trick/integration/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/trick/integration/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/trick/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/trick/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/interface/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/interface/include
cp -r ${TRICK_HOME}/trick_source/er7_utils/math/include %{buildroot}/usr/bin/trick/trick_source/er7_utils/math/include

rm %{buildroot}/usr/bin/trick/libexec/libexec/trick/make_changelog

%files
/usr/bin/trick/bin
/usr/bin/trick/include
/usr/bin/trick/lib64
/usr/bin/trick/libexec
/usr/bin/trick/trick_source/er7_utils



%changelog
* Mon Sep 30 2024 AdityaGirish <aditya.girish@nasa.gov>
- Updated RPM to have the new folders.
