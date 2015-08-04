%ifnarch s390 s390x
%global with_openmpi 1
%else
%global with_openmpi 0
%endif

Name:		gromacs
Version:	5.0.6
Release:	2%{?dist}
Summary:	Fast, Free and Flexible Molecular Dynamics
Group:		Applications/Engineering
License:	GPLv2+
URL:		http://www.gromacs.org

Source0:	ftp://ftp.gromacs.org/pub/gromacs/gromacs-%{version}.tar.gz
Source1:	ftp://ftp.gromacs.org/pub/manual/manual-%{version}.pdf
Source6:	gromacs-README.fedora
# fix path to packaged dssp
# https://bugzilla.redhat.com/show_bug.cgi?id=1203754
Patch0:		gromacs-dssp-path.patch

BuildRequires:	cmake
BuildRequires:	atlas-devel >= 3.10.1
BuildRequires:	boost-devel
BuildRequires:	fftw-devel
BuildRequires:	gsl-devel
BuildRequires:	libxml2-devel
BuildRequires:	libX11-devel
BuildRequires:	motif-devel
# To get rid of executable stacks
%ifnarch aarch64 ppc64le
BuildRequires:	/usr/bin/execstack
%endif
Requires:	gromacs-common = %{version}-%{release}
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
Group:		Applications/Engineering
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
Group:		Applications/Engineering
Requires:	gromacs = %{version}-%{release}

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
Group:		System Environment/Libraries

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
Group:		Applications/Engineering
Obsoletes:	gromacs-mpi < %{version}-%{release}
Requires:	gromacs-common = %{version}-%{release}
BuildRequires:	openmpi-devel
Requires:	openmpi

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
Group:		System Environment/Libraries
Obsoletes:	gromacs-mpi-libs < %{version}-%{release}
Requires:	openmpi

%description openmpi-libs
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains libraries needed for operation of GROMACS Open MPI.


%package openmpi-devel
Summary:	GROMACS Open MPI development libraries
Group:		Applications/Engineering
Obsoletes:	gromacs-mpi-devel < %{version}-%{release}
Requires:	gromacs-devel = %{version}-%{release}
Requires:	gromacs-openmpi = %{version}-%{release}
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
Group:		Applications/Engineering
Requires:	gromacs-common = %{version}-%{release}
Requires:	mpich
Provides:	%{name}-mpich2 = %{version}-%{release}
Obsoletes:	gromacs-mpich2 < 4.6.3-2

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
Group:		System Environment/Libraries
Requires:	mpich
Provides:	%{name}-mpich2-libs = %{version}-%{release}
Obsoletes:	%{name}-mpich2-libs < 4.6.3-2

%description mpich-libs
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains libraries needed for operation of GROMACS MPICH.


%package mpich-devel
Summary:	GROMACS MPICH development libraries
Group:		Applications/Engineering
Requires:	gromacs-devel = %{version}-%{release}
Requires:	gromacs-mpich = %{version}-%{release}
BuildRequires:	mpich-devel
Requires:	mpich-devel
Provides:	%{name}-mpich2-devel = %{version}-%{release}
Obsoletes:	%{name}-mpich2-devel < 4.6.3-2

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
Group:		Applications/Engineering
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
Group:		Applications/Engineering
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
%setup -q
%patch0 -p1 -b .dssp
mkdir {serial,mpich,openmpi}{,_d}

%build
# Assembly kernels haven't got .note.GNU-stack sections
# because of incompatibilies with Microsoft Assembler.
# Add noexecstack to compiler flags

export CFLAGS="%optflags -Wa,--noexecstack -fPIC"
export LDFLAGS="-L%{_libdir}/atlas"

# Default options, used for all compilations
export DEFOPTS="\
 -DBUILD_SHARED_LIBS=ON \
 -DBUILD_TESTING:BOOL=ON \
 -DCMAKE_C_FLAGS_RELEASE= \
 -DCMAKE_CXX_FLAGS_RELEASE= \
 -DCMAKE_SKIP_RPATH:BOOL=ON \
 -DCMAKE_SKIP_BUILD_RPATH:BOOL=ON \
 -DGMX_BLAS_USER=satlas \
 -DGMX_BUILD_UNITTESTS:BOOL=ON \
 -DGMX_LAPACK_USER=satlas \
 -DGMX_X11=ON \
"
export DOUBLE="-D GMX_DOUBLE=ON" # Double precision
export MPI="-DGMX_MPI=ON -DGMX_THREAD_MPI=OFF -DGMX_DEFAULT_SUFFIX=OFF"

# Acceleration flag
export CPUACC="None"
# .. but on x86_64 we know that SSE2 is available always, so
%ifarch x86_64
export CPUACC="SSE2"
%endif
export DEFOPTS+=" -DGMX_SIMD=${CPUACC}"

for p in '' _d ; do
cd serial${p}
%cmake $DEFOPTS $(test -n "$p" && echo $DOUBLE) ..
make VERBOSE=1 %{?_smp_mflags}
cd ..
done

%if %{with_openmpi}
%{_openmpi_load}
for p in '' _d ; do
SUFFIXCONF="-D GMX_BINARY_SUFFIX=${MPI_SUFFIX}${p} -D GMX_LIBS_SUFFIX=${MPI_SUFFIX}${p}"
cd openmpi${p}
%cmake $DEFOPTS $MPI $SUFFIXCONF $(test -n "$p" && echo $DOUBLE) ..
make VERBOSE=1 %{?_smp_mflags}
cd ..
done
%{_openmpi_unload}
%endif

%{_mpich_load}
for p in '' _d ; do
SUFFIXCONF="-D GMX_BINARY_SUFFIX=${MPI_SUFFIX}${p} -D GMX_LIBS_SUFFIX=${MPI_SUFFIX}${p}"
cd mpich${p}
%cmake $DEFOPTS $MPI $SUFFIXCONF $(test -n "$p" && echo $DOUBLE) ..
make VERBOSE=1 %{?_smp_mflags}
cd ..
done
%{_mpich_unload}


%install
%if %{with_openmpi}
%{_openmpi_load}
# Make install-mdrun target is broken, do install manually
mkdir -p %{buildroot}{$MPI_BIN,$MPI_LIB}
for p in '' _d ; do
cd openmpi${p}
install -p -m 755 bin/gmx* %{buildroot}$MPI_BIN/
cp -a lib/libgromacs${MPI_SUFFIX}${p}.so* %{buildroot}$MPI_LIB/
cd ..
done
%{_openmpi_unload}
%endif

%{_mpich_load}
# Make install-mdrun target is broken, do install manually
mkdir -p %{buildroot}%{_libdir}/mpich/{bin,lib}
for p in '' _d ; do
cd mpich${p}
install -p -m 755 bin/gmx* %{buildroot}$MPI_BIN/
cp -a lib/libgromacs${MPI_SUFFIX}${p}.so* %{buildroot}$MPI_LIB/
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
install -cpm 644 %{SOURCE1} %{buildroot}%{_docdir}/gromacs/manual.pdf
install -cpm 644 %{SOURCE6} %{buildroot}%{_docdir}/gromacs/README.fedora

pushd %{buildroot}
# Fix GMXRC file permissions
chmod a+x ./%{_bindir}/GMXRC ./%{_bindir}/GMXRC.*

# Rename binaries to prevent clashes
# (This is done here so that we don't need to mess with machine generated makefiles.
for bin in do_dssp editconf eneconv genbox genconf genion genrestr gmxcheck gmxdump grompp make_edi make_ndx mdrun mk_angndx pdb2gmx tpbconv trjcat trjconv trjorder xpm2ps; do
for p in '' _d ; do
mv ./%{_bindir}/${bin}${p} ./%{_bindir}/g_${bin}${p}
done
done

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
%ifnarch aarch64 ppc64le
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
for p in '' _d ; do
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
%{_mandir}/man1/gmx*.1*
%{_mandir}/man7/gromacs.7*
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/template

%files doc
%{_docdir}/gromacs/manual.pdf

%files libs
%{_libdir}/libgromacs*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/libgromacs*.so
%{_libdir}/pkgconfig/libgromacs*.pc
%{_datadir}/%{name}/template

%if %{with_openmpi}
%files openmpi
%{_libdir}/openmpi/bin/gmx*

%files openmpi-libs
%{_libdir}/openmpi/lib/libgromacs_openmpi*.so.*

%files openmpi-devel
%{_libdir}/openmpi/lib/libgromacs_openmpi*.so
%endif

%files mpich
%{_libdir}/mpich/bin/gmx*

%files mpich-libs
%{_libdir}/mpich/lib/libgromacs_mpich*.so.*

%files mpich-devel
%{_libdir}/mpich/lib/libgromacs_mpich*.so

%files zsh
%{_bindir}/GMXRC.zsh

%files csh
%{_bindir}/GMXRC.csh

%changelog
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
