%global git 1
%global commit bec9c8757e59cae58fc61ed841c0bb73c84079db
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%ifnarch s390 s390x
%global with_openmpi 1
%else
%global with_openmpi 0
%endif
%global execstack_excludearch aarch64 ppc64 ppc64le s390 s390x
%ifnarch aarch64 armv7hl ppc64 ppc64le s390 s390x
%if 0%{?fedora} > 23
# https://bugzilla.redhat.com/show_bug.cgi?id=1307869
%global with_opencl 0
%else
%global with_opencl 1
%endif
%else
%global with_opencl 0
%endif

%global simd None
%ifarch x86_64
%global simd SSE2
%endif
# doesn't compile at the moment due to usage of vec_mul which is VSX-only
# http://redmine.gromacs.org/issues/1812
# also, not all Fedora-supported CPUs have AltiVec
%ifarch ppc64
#%%global simd IBM_VMX
%endif
%ifarch ppc64le
%global simd IBM_VSX
%endif
# not all Fedora-supported CPUs have NEON
%ifarch armv7hl
#%%global simd ARM_NEON
%endif
%ifarch aarch64
%global simd ARM_NEON_ASIMD
%endif

Name:		gromacs
Version:	2016
Release:	0.1.20160318git%{shortcommit}%{?dist}
Summary:	Fast, Free and Flexible Molecular Dynamics
License:	GPLv2+
URL:		http://www.gromacs.org

%if %{git}
Source0:	https://github.com/gromacs/gromacs/archive/%{commit}/gromacs-%{commit}.tar.gz
# required for building the manual
BuildRequires:	%{_bindir}/bibtex
BuildRequires:	%{_bindir}/convert
BuildRequires:	%{_bindir}/dvips
BuildRequires:	%{_bindir}/latex2html
BuildRequires:	%{_bindir}/makeindex
BuildRequires:	%{_bindir}/pdflatex
BuildRequires:	python2-sphinx
%else
Source0:	ftp://ftp.gromacs.org/pub/gromacs/gromacs-%{version}.tar.gz
Source1:	ftp://ftp.gromacs.org/pub/manual/manual-%{version}.pdf
%endif
Source6:	gromacs-README.fedora
# fix path to packaged dssp
# https://bugzilla.redhat.com/show_bug.cgi?id=1203754
Patch0:		gromacs-dssp-path.patch
# http://redmine.gromacs.org/issues/1911
# https://github.com/google/googletest/issues/705
Patch1:		gromacs-gtest-issue705.patch
# fix building documentation
Patch3:		gromacs-sphinx-no-man.patch
BuildRequires:	cmake
BuildRequires:	atlas-devel >= 3.10.1
BuildRequires:	boost-devel
BuildRequires:	fftw-devel
BuildRequires:	gsl-devel
BuildRequires:	libxml2-devel
BuildRequires:	libX11-devel
BuildRequires:	motif-devel
%if %{with_opencl}
BuildRequires:	ocl-icd-devel
BuildRequires:	opencl-headers
# use CPU-based OpenCL implementation for build
BuildRequires:	pocl
Requires:	gromacs-opencl = %{version}-%{release}
%endif
# To get rid of executable stacks
%ifnarch %{execstack_excludearch}
BuildRequires:	/usr/bin/execstack
%endif
Requires:	gromacs-common = %{version}-%{release}
Requires:	gromacs-libs = %{version}-%{release}
Obsoletes:	gromacs-ngmx < 5.0.4-1

%description
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package provides single and double precision binaries.
The documentation is in the package gromacs-common.

mdrun has been compiled with thread parallellization, so it runs in parallel
on shared memory systems. If you want to run on a cluster, you probably want
to install one of the MPI parallellized packages.

N.B. All binaries have names starting with g_, for example mdrun has been
renamed to g_mdrun.


%package common
Summary:	GROMACS shared data and documentation
BuildArch:	noarch
Provides:	gromacs-bash = %{version}-%{release}
Obsoletes:	gromacs-bash < 5.0.4-1

%description common
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package includes architecture independent data and HTML documentation.


%package opencl
Summary:	GROMACS OpenCL kernels
# suggest installing a GPU-based OpenCL implementation
Suggests:	beignet
Suggests:	mesa-libOpenCL
# or at least a CPU-based one
Suggests:	pocl

%description opencl
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package includes the OpenCL kernels.


%package doc
Summary:	GROMACS manual
BuildArch:	noarch
Obsoletes: gromacs-common < 5.0.5-2

%description doc
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package the manual in PDF format.


%package devel
Summary:	GROMACS header files and development libraries
Requires:	gromacs-libs = %{version}-%{release}
Requires:	cmake

%description devel
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains header files and development libraries for the GROMACS
molecular dynamics software. You need it if you want to write your own analysis
programs.


%package libs
Summary:	GROMACS shared libraries

%description libs
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains libraries needed for operation of GROMACS.


%if %{with_openmpi}
%package openmpi
Summary:	GROMACS Open MPI binaries and libraries
Requires:	gromacs-common = %{version}-%{release}
%if %{with_opencl}
Requires:	gromacs-opencl = %{version}-%{release}
%endif
Requires:	gromacs-openmpi-libs = %{version}-%{release}
BuildRequires:	openmpi-devel

%description openmpi
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

mdrun has been compiled with thread parallellization (for running on
a single node) and with Open MPI (for running on multiple nodes).
This package single and double precision binaries and libraries.


%package openmpi-libs
Summary:	GROMACS Open MPI shared libraries

%description openmpi-libs
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains libraries needed for operation of GROMACS Open MPI.


%package openmpi-devel
Summary:	GROMACS Open MPI development libraries
Requires:	gromacs-devel = %{version}-%{release}
Requires:	gromacs-openmpi = %{version}-%{release}
BuildRequires:	openmpi-devel
Requires:	openmpi-devel


%description openmpi-devel
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains development libraries for GROMACS Open MPI.
You may need it if you want to write your own analysis programs.
%endif


%package mpich
Summary:	GROMACS MPICH binaries and libraries
Requires:	gromacs-common = %{version}-%{release}
%if %{with_opencl}
Requires:	gromacs-opencl = %{version}-%{release}
%endif
Requires:	gromacs-mpich-libs = %{version}-%{release}

%description mpich
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

mdrun has been compiled with thread parallellization (for running on
a single node) and with MPICH (for running on multiple nodes).
This package single and double precision binaries and libraries.

%package mpich-libs
Summary:	GROMACS MPICH shared libraries

%description mpich-libs
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains libraries needed for operation of GROMACS MPICH.


%package mpich-devel
Summary:	GROMACS MPICH development libraries
Requires:	gromacs-devel = %{version}-%{release}
Requires:	gromacs-mpich = %{version}-%{release}
BuildRequires:	mpich-devel
Requires:	mpich-devel

%description mpich-devel
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains development libraries for GROMACS MPICH.
You may need it if you want to write your own analysis programs.


%package zsh
Summary:	GROMACS zsh support
Requires:	zsh
BuildArch:	noarch


%description zsh
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package provides scripts needed to run GROMACS with zsh and zsh
completion.


%package csh
Summary:	GROMACS csh support
Requires:	csh
BuildArch:	noarch


%description csh
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package provides scripts needed to run GROMACS with csh and a completion
script.

%prep
%if %{git}
%setup -q -n gromacs-%{commit}
%patch3 -p1 -b .sphinx-no-man
%else
%setup -q
install -Dpm644 %{SOURCE1} ./serial/docs/manual/manual.pdf
%endif
%patch0 -p1 -b .dssp
%if 0%{?fedora} > 23
%patch1 -p1 -b .gtest705
%endif
mkdir {serial,mpich,openmpi}{,_d}

%build
# Assembly kernels haven't got .note.GNU-stack sections
# because of incompatibilies with Microsoft Assembler.
# Add noexecstack to compiler flags

export CFLAGS="%optflags -Wa,--noexecstack -fPIC"
export LDFLAGS="-L%{_libdir}/atlas"

# Default options, used for all compilations
%global defopts \\\
 -DBUILD_SHARED_LIBS=ON \\\
 -DBUILD_TESTING:BOOL=ON \\\
 -DCMAKE_SKIP_RPATH:BOOL=ON \\\
 -DCMAKE_SKIP_BUILD_RPATH:BOOL=ON \\\
 -DGMX_BLAS_USER=satlas \\\
 -DGMX_BUILD_UNITTESTS:BOOL=ON \\\
 -DGMX_LAPACK_USER=satlas \\\
 -DGMX_SIMD=%{simd} \\\

%if %{with_opencl}
# OpenCL is available for single precision only
%global single -DGMX_GPU:BOOL=ON -DGMX_USE_OPENCL:BOOL=ON
%endif
%global double -DGMX_DOUBLE:BOOL=ON
%global mpi -DGMX_BUILD_MDRUN_ONLY:BOOL=ON -DGMX_MPI:BOOL=ON -DGMX_THREAD_MPI:BOOL=OFF -DGMX_DEFAULT_SUFFIX:BOOL=OFF

%if %{with_openmpi}
%{_openmpi_load}
for p in '' _d ; do
cd openmpi${p}
%cmake \
 %{defopts} \
 %{mpi} \
 -DGMX_BINARY_SUFFIX=${MPI_SUFFIX}${p} -DGMX_LIBS_SUFFIX=${MPI_SUFFIX}${p} \
 $(test -n "$p" && echo %{double} || echo %{?single}) \
 ..
make VERBOSE=1 %{?_smp_mflags}
cd ..
done
%{_openmpi_unload}
%endif

%{_mpich_load}
for p in '' _d ; do
cd mpich${p}
%cmake \
 %{defopts} \
 %{mpi} \
 -DGMX_BINARY_SUFFIX=${MPI_SUFFIX}${p} -DGMX_LIBS_SUFFIX=${MPI_SUFFIX}${p} \
 $(test -n "$p" && echo %{double} || echo %{?single}) \
 ..
make VERBOSE=1 %{?_smp_mflags}
cd ..
done
%{_mpich_unload}

for p in '' _d ; do
cd serial${p}
%cmake \
 %{defopts} \
 -DGMX_X11=ON \
 $(test -n "$p" && echo %{double} || echo %{?single}) \
 ..
make VERBOSE=1 %{?_smp_mflags}
cd ..
done

%if %{git}
cd serial
%cmake \
 %{defopts} \
 -DGMX_X11=ON \
 %{?single} \
 -DGMX_BUILD_MANUAL:BOOL=ON -DGMX_BUILD_HELP:BOOL=ON \
 ..
LD_LIBRARY_PATH=$PWD/lib make VERBOSE=1 completion install-guide man manual
cd ..
%endif

%install
%if %{with_openmpi}
%{_openmpi_load}
# Make install-mdrun target is broken, do install manually
mkdir -p %{buildroot}{$MPI_BIN,$MPI_LIB}
for p in '' _d ; do
cd openmpi${p}
install -p -m 755 bin/mdrun${MPI_SUFFIX}${p} %{buildroot}$MPI_BIN/
cp -a lib/libgromacs_mdrun${MPI_SUFFIX}${p}.so* %{buildroot}$MPI_LIB/
cd ..
done
%{_openmpi_unload}
%endif

%{_mpich_load}
# Make install-mdrun target is broken, do install manually
mkdir -p %{buildroot}{$MPI_BIN,$MPI_LIB}
for p in '' _d ; do
cd mpich${p}
install -p -m 755 bin/mdrun${MPI_SUFFIX}${p} %{buildroot}$MPI_BIN/
cp -a lib/libgromacs_mdrun${MPI_SUFFIX}${p}.so* %{buildroot}$MPI_LIB/
cd ..
done
%{_mpich_unload}

for p in '' _d ; do
cd serial${p}
make DESTDIR=%{buildroot} INSTALL="install -p" install
cd ..
done

mkdir -p %{buildroot}%{_docdir}/gromacs
install -pm 644 AUTHORS COPYING README %{buildroot}%{_docdir}/gromacs
# Install manual & packager's note
install -cpm 644 serial/docs/manual/gromacs.pdf %{buildroot}%{_docdir}/gromacs/manual.pdf
install -cpm 644 %{SOURCE6} %{buildroot}%{_docdir}/gromacs/README.fedora

pushd %{buildroot}
# Fix GMXRC file permissions
chmod a+x ./%{_bindir}/GMXRC ./%{_bindir}/GMXRC.*

for bin in demux.pl xplor2gmx.pl; do
mv ./%{_bindir}/$bin ./%{_bindir}/g_${bin}
done

# Move completion files around
chmod a-x ./%{_bindir}/gmx-completion*
# Bash
mkdir -p ./%{_sysconfdir}/bash_completion.d
mv ./%{_bindir}/gmx-completion.bash ./etc/bash_completion.d/gmx-completion
mv ./%{_bindir}/gmx-completion-gmx.bash ./etc/bash_completion.d/gmx-completion-gmx
mv ./%{_bindir}/gmx-completion-gmx_d.bash ./etc/bash_completion.d/gmx-completion-gmx_d

# Remove .la files
find ./ -name *.la -delete

# Get rid of executable stacks
%ifnarch %{execstack_excludearch}
find ./ -name *.so.* -exec execstack -c {} \;
%endif
popd


# Post install for libs. MPI packages don't need this.
%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%if 1
%check
%if %{with_openmpi}
%{_openmpi_load}
for p in '' _d ; do
  cd openmpi${p}
  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}${MPI_LIB} make VERBOSE=1 %{?_smp_mflags} check
  cd ..
done
%{_openmpi_unload}
%endif
%{_mpich_load}
for p in '' _d ; do
  cd mpich${p}
  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}${MPI_LIB} make VERBOSE=1 %{?_smp_mflags} check
  cd ..
done
%{_mpich_unload}
# s390 has too little memory to run the testsuite with double precision
%ifnarch s390
for p in '' _d ; do
%else
for p in '' ; do
%endif
  cd serial${p}
  LD_LIBRARY_PATH=%{buildroot}%{_libdir} make VERBOSE=1 %{?_smp_mflags} check
  cd ..
done
%endif


%files
%{_bindir}/gmx*
%{_bindir}/g_*

%files common
%{_docdir}/gromacs
%exclude %{_docdir}/gromacs/manual.pdf
%config(noreplace) %{_sysconfdir}/bash_completion.d/gmx-completion*
%{_bindir}/GMXRC
%{_bindir}/GMXRC.bash
%{_mandir}/man1/gromacs.1*
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/template
%if %{with_opencl}
%exclude %{_datadir}/%{name}/opencl

%files opencl
%doc docs/OpenCLTODOList.txt
%{_datadir}/%{name}/opencl
%endif

%files doc
%{_docdir}/gromacs/manual.pdf

%files libs
%{_libdir}/libgromacs*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/libgromacs*.so
%{_libdir}/pkgconfig/libgromacs*.pc
%{_datadir}/%{name}/template
%{_datadir}/cmake/gromacs*

%if %{with_openmpi}
%files openmpi
%{_libdir}/openmpi/bin/mdrun_openmpi*

%files openmpi-libs
%{_libdir}/openmpi/lib/libgromacs_mdrun_openmpi*.so.*

%files openmpi-devel
%{_libdir}/openmpi/lib/libgromacs_mdrun_openmpi*.so
%endif

%files mpich
%{_libdir}/mpich/bin/mdrun_mpich*

%files mpich-libs
%{_libdir}/mpich/lib/libgromacs_mdrun_mpich*.so.*

%files mpich-devel
%{_libdir}/mpich/lib/libgromacs_mdrun_mpich*.so

%files zsh
%{_bindir}/GMXRC.zsh

%files csh
%{_bindir}/GMXRC.csh

%changelog
* Fri Mar 18 2016 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2016-0.1.20160318gitbec9c87
- update to git master branch
- disable OpenCL for now (due to pocl FTBFS #1307869)
- use BOOL with all boolean cmake options

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.1.1-1
- update to 5.1.1

* Wed Sep 23 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.1-6
- don't remove -DNDEBUG from CFLAGS (makes HandlesPermuteModifier test fail
  randomly)
- convert shell variables to rpm macros
- enable OpenCL support (x86 and single precision only)

* Tue Sep 22 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.1-5
- disable HandlesPermuteModifier test which fails randomly on i686

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 5.1-4
- Rebuild for openmpi 1.10.0

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 5.1-3
- Rebuilt for Boost 1.59

* Wed Aug 19 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.1-2
- enable NEON SIMD on aarch64
- fix compilation of VSX code with double precision on ppc64le
- enable VSX on ppc64le only
- don't manually output testuite logs upon failure, ctest does that already

* Sat Aug 15 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.1-1
- update to 5.1
- drop ancient Obsoletes:/Provides:
- drop Group: tags
- build mdrun-only MPI binaries again
- simplify SIMD enablement handling
- enable SIMD on ppc64(le)
- no execstack on ppc64 or s390(x), either
- output testsuite logs upon failure

* Sat Aug 15 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.0.6-6
- Rebuild for MPI provides

* Mon Aug 10 2015 Sandro Mani <manisandro@gmail.com> - 5.0.6-5
- Rebuild for RPM MPI Requires Provides Change

* Thu Aug 06 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.0.6-4
- fix up dependencies between subpackages

* Thu Aug 06 2015 Jonathan Wakely <jwakely@redhat.com> 5.0.6-3
- Rebuilt for Boost 1.58

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Sun Jul 26 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.0.6-1
- update to 5.0.6

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 5.0.5-4
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.0.5-2
- obsolete old -common subpackage in -doc so that users don't lose the manual

* Sat Jun 13 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.0.5-1
- update to 5.0.5
- fix path to packaged dssp
- drop upstreamed patch
- move the large manual into a separate -doc subpackage

* Tue Apr 14 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.0.4-1
- update to 5.0.4
- switch Motif library to original Motif (as it's in Fedora since long)
- link against new-style atlas library (atlas 3.10.1+)
- BR: boost-devel
- csh/zsh completion removed upstream
- move bash completion into main package
- separate ngmx and mdrun dropped upstream
- enable testsuite
- factorize a lot of build logic
- drop redundant comments
- skip double precision tests on i686 (http://redmine.gromacs.org/issues/1716)

* Mon Apr 13 2015 Dominik Mierzejewski <rpm@greysector.net> - 4.6.5-6
- rebuilt for changed mpich libraries

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 4.6.5-4
- Fix builds on aarch64/ppc64le
- Modernise spec
- Remove ancient obsoletes

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 22 2014 Deji Akingunola <dakingun@gmail.com> - 4.6.5-2
- Rebuild for mpich-3.1

* Tue Dec 03 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.6.5-1
- Update to 4.6.5.

* Thu Nov 14 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.6.4-1
- Update to 4.6.4.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Deji Akingunola <dakingun@gmail.com> - 4.6.3-2
- Rename mpich2 sub-packages to mpich and rebuild for mpich-3.0

* Sat Jul 06 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.6.3-1
- Update to 4.6.3.

* Tue Jun 04 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.6.2-1
- Update to 4.6.2.

* Wed Mar 06 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.6.1-1
- Update to 4.6.1.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.6-1
- Update to stable 4.6 release.

* Mon Dec 31 2012 Dan Horák <dan[at]danny.cz> - 4.6-0.2.beta3
- fix build on non-x86 arches

* Mon Dec 24 2012 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.6-0.1.beta3
- Update to 4.6 beta 3.

* Fri Nov 02 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.5-3.1
- Bump due to MPICH2 update.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.5-1
- Update to 4.5.5.

* Wed Mar 30 2011 Deji Akingunola <dakingun@gmail.com> - 4.5.4-2
- Rebuild for mpich2 soname bump

* Wed Mar 23 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.4-1
- Update to 4.5.4.

* Sun Feb 13 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.3-4
- Get rid of executable stacks.

* Mon Feb 07 2011 Dan Horák <dan[at]danny.cz> - 4.5.3-3
- conditionalize OpenMPI support
- fix build on 64-bit platforms

* Mon Dec 20 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.3-2
- Fix rest of BZ #649338.

* Thu Nov 18 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.3-1
- Update to 4.5.3.

* Fri Nov 05 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.2-3
- Rebuild due to libxml2 soname bump.

* Wed Nov 03 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.2-2
- Make gromacs package obsolete older versions of gromacs package due to the
  branching of libraries.

* Mon Nov 01 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.2-1
- Update to 4.5.2.

* Wed Oct 27 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.1-2
- Patch around #644950.
- Split libraries in own packages to avoid multilib problems.

* Sat Oct 09 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.1-1
- Update to 4.5.1.

* Sun Dec 06 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.0.7-1
- Update to 4.0.7.

* Sun Dec 06 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.0.6-1
- Update to 4.0.6.

* Fri Dec 04 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.0.5-6
- Fix file conflict.

* Tue Dec 01 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.0.5-5
- Put correct MPI devel package requires in place.

* Tue Dec 01 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.0.5-4
- Fix obsoletes.

* Mon Nov 30 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.0.5-3
- Combine libs with binaries and drop debug packages to avoid explosion of
  number of packages.
- Adopt use of MPI guidelines.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.5-1
- Update to 4.0.5.
- Change spec %%defines to %%globals.
- Add debug subpackages to make debugging of GROMACS possible.

* Tue Feb 17 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.4-1
- Update to 4.0.4.

* Mon Jan 19 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.3-4
- Retry fixing gmxdemo.

* Mon Jan 19 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.3-3
- Fixed gmxdemo.

* Mon Jan 19 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.3-2
- Fix EPEL 4 build.

* Mon Jan 19 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.3-1
- Update to 4.0.3.

* Wed Jan 14 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.2-7
- Update manual to latest version.
- Removed Requires: blas and lapack.

* Mon Nov 10 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.2-6
- Update to 4.0.2.

* Sun Nov 09 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.1-5
- Add Requires: blas too.

* Sun Nov 09 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.1-4
- Update to 4.0.1.
- Add Requires: lapack and openmpi to prevent yum from pulling atlas and lam
instead.

* Wed Oct 15 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-3
- Rename also man pages.

* Mon Oct 13 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-2
- Added noreplace to bash completion file.
- Changed double precision mpi binary suffix to _mpi_d.

* Sun Oct 12 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-1
- Update to Gromacs 4.0.
- Remove module system and patch file names to begin with g_.

* Wed Oct 08 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.15.rc3
- Changed location of binaries.
- Removed conflict of module file, as the program is binary compatible with older versions.

* Wed Oct 08 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.14.rc3
- The gromacs module is loaded automatically and it conflicts with gromacs3.

* Tue Oct 07 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.13.rc3
- Renamed module files from %%{name}-%%{version} to %%{name}.

* Mon Oct 06 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.12.rc3
- Fix BR to get GROMACS to build in mock for epel-4.

* Sat Oct 04 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.11.rc3
- Fix to get GROMACS to build in mock for epel-5.

* Sat Oct 04 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.10.rc3
- Implement module system & remove binary renaming.
- No need for autoreconf anymore.
- Update to rc3.

* Sat Oct 04 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.9.rc2
- Fall back to autoreconf due to binary renaming.

* Fri Oct 03 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.8.rc2
- Modified install commands to preserve timestamps.

* Fri Oct 03 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.7.rc2
- Even more review fixes.
- Binaries renamed:
	highway	->	g_highway
	luck	->	g_luck
	sigeps	->	g_sigeps
	wheel	->	g_wheel

* Thu Oct 02 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.6.rc2
- Final review fixes.

* Wed Oct 01 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.5.rc2
- Strip down requires by branching tutor to its own package.

* Tue Sep 30 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.4.rc2
- Extensive package review fixes.
- Unclear licenses on some files, filed upstream bug 217.
  http://bugzilla.gromacs.org/show_bug.cgi?id=217

* Mon Sep 29 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.3.rc2
- Move .so files to -devel package.
- Remove .la files.

* Mon Sep 29 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.2.rc2
- Implement out-of-tree-builds.
- Add --noexecstack to CFLAGS.
- Remove execstack procedure and prelink from buildreqs.
- Filed upstream bug 215 to add .note.GNU-stack .
- Fix incorrect file permission on src/tools/gmx_xpm2ps.c .

* Mon Sep 29 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.1.rc2
- Alphabetized buildrequires.
- Changed gromacs-share to gromacs-common.

* Fri Sep 26 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.0.rc2
- Initial build.
