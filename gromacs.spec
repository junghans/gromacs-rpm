%ifnarch s390 s390x
%global with_openmpi 1
%else
%global with_openmpi 0
%endif

Name:		gromacs
Version:	4.6.5
Release:	6%{?dist}
Summary:	Fast, Free and Flexible Molecular Dynamics
Group:		Applications/Engineering
License:	GPLv2+
URL:		http://www.gromacs.org

Source0:	ftp://ftp.gromacs.org/pub/gromacs/gromacs-%{version}.tar.gz
Source1:	ftp://ftp.gromacs.org/pub/manual/manual-%{version}.pdf
Source6:	gromacs-README.fedora

BuildRequires:	cmake
BuildRequires:	atlas-devel
BuildRequires:	fftw-devel
BuildRequires:	gsl-devel
BuildRequires:	libxml2-devel
BuildRequires:	libX11-devel
BuildRequires:	lesstif-devel
# To get rid of executable stacks
%ifnarch aarch64 ppc64le
BuildRequires:	prelink
%endif

Requires:	gromacs-common = %{version}-%{release}


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

%description common
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package includes architecture independent data and documentation.


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
# Libs were branched from gromacs, so there are 64-bit installs that have 32-bit packages installed (at version 4.5.3-2)
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

%package ngmx
Summary:	GROMACS X11 visualization program
Group:		Applications/Engineering

%description ngmx
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains ngmx, the X11 visualization program.


%package bash
Summary:	GROMACS bash completion
Group:		Applications/Engineering
Requires:	bash-completion
BuildArch:	noarch


%description bash
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package provides bash completion for GROMACS.


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

%build
# Assembly kernels haven't got .note.GNU-stack sections
# because of incompatibilies with Microsoft Assembler.
# Add noexecstack to compiler flags

export CFLAGS="%optflags -Wa,--noexecstack -fPIC"
export LIBS="-L%{_libdir}/atlas -lblas -llapack"

# Default options, used for all compilations
export DEFOPTS="-D BUILD_SHARED_LIBS=ON -DCMAKE_SKIP_RPATH:BOOL=ON -DCMAKE_SKIP_BUILD_RPATH:BOOL=ON -DGMXLIB=%{_lib} -DGMX_X11=ON -DCMAKE_C_FLAGS_RELEASE= -DCMAKE_CXX_FLAGS_RELEASE="
export SINGLE="-D GMX_DOUBLE=OFF" # Single precision
export DOUBLE="-D GMX_DOUBLE=ON" # Double precision
export MPI="-D GMX_MPI=ON"

# Acceleration flag
export CPUACC="None"
# .. but on x86_64 we know that SSE2 is available always, so
%ifarch x86_64
export CPUACC="SSE2"
%endif
export DEFOPTS+=" -DGMX_CPU_ACCELERATION=${CPUACC}"

# Single precision
mkdir single
cd single
%cmake $DEFOPTS $SINGLE ..
make VERBOSE=1 %{?_smp_mflags}
cd ..

# Double precision
mkdir double
cd double
%cmake $DEFOPTS $DOUBLE ..
make VERBOSE=1 %{?_smp_mflags}
cd ..


### MPI versions
export CC=mpicc
export CXX=mpicxx
export F77=mpif77
export F90=mpif90
export FC=mpif90

## Open MPI
%if %{with_openmpi}
%{_openmpi_load}
# Suffix to be used for single precision is
SUFFIXCONF="-D GMX_DEFAULT_SUFFIX=OFF -D GMX_BINARY_SUFFIX=$SUFFIX -D GMX_LIBS_SUFFIX=${MPI_SUFFIX}"
# single precision
mkdir openmpi-single
cd openmpi-single
%cmake $DEFOPTS $SINGLE $MPI $SUFFIXCONF ..
make VERBOSE=1 %{?_smp_mflags} mdrun
cd ..

# double precision
# Suffix to be used for double precision is
SUFFIXCONF="-D GMX_DEFAULT_SUFFIX=OFF -D GMX_BINARY_SUFFIX=$SUFFIX -D GMX_LIBS_SUFFIX=${MPI_SUFFIX}_d"
mkdir openmpi-double
cd openmpi-double
%cmake $DEFOPTS $DOUBLE $MPI $SUFFIXCONF ..
make VERBOSE=1 %{?_smp_mflags} mdrun
cd ..
# unload
%{_openmpi_unload}
%endif


## MPICH
%{_mpich_load}
# Suffix to be used for single precision is
SUFFIXCONF="-D GMX_DEFAULT_SUFFIX=OFF -D GMX_BINARY_SUFFIX=$SUFFIX -D GMX_LIBS_SUFFIX=${MPI_SUFFIX}"
# MPICH 2 is broken, so need to modify linker command
export CC="mpicc -lstdc++"
# single precision
mkdir mpich-single
cd mpich-single
%cmake $DEFOPTS $SINGLE $MPI $SUFFIXCONF ..
make VERBOSE=1 %{?_smp_mflags} mdrun
cd ..
# double precision
# Suffix to be used for double precision is
SUFFIXCONF="-D GMX_DEFAULT_SUFFIX=OFF -D GMX_BINARY_SUFFIX=$SUFFIX -D GMX_LIBS_SUFFIX=${MPI_SUFFIX}_d"
mkdir mpich-double
cd mpich-double
%cmake $DEFOPTS $DOUBLE $MPI $SUFFIXCONF ..
make VERBOSE=1 %{?_smp_mflags} mdrun
cd ..
%{_mpich_unload}


%install
## Open MPI
%if %{with_openmpi}
%{_openmpi_load}
# Make install-mdrun target is broken, do install manually
mkdir -p %{buildroot}%{_libdir}/openmpi/{bin,lib}
# single precision
cd openmpi-single
install -p -m 755 src/kernel/mdrun %{buildroot}%{_libdir}/openmpi/bin/g_mdrun_openmpi
cp -a src/*/*.so* %{buildroot}%{_libdir}/openmpi/lib/
cd ..
# double precision
cd openmpi-double
install -p -m 755 src/kernel/mdrun %{buildroot}%{_libdir}/openmpi/bin/g_mdrun_openmpi_d
cp -a src/*/*.so* %{buildroot}%{_libdir}/openmpi/lib/
cd ..
%{_openmpi_unload}
%endif

## MPICH
%{_mpich_load}
# Make install-mdrun target is broken, do install manually
mkdir -p %{buildroot}%{_libdir}/mpich/{bin,lib}
# single precision
cd mpich-single
install -p -m 755 src/kernel/mdrun %{buildroot}%{_libdir}/mpich/bin/g_mdrun_mpich
cp -a src/*/*.so* %{buildroot}%{_libdir}/mpich/lib/
cd ..
# double precision
cd mpich-double
install -p -m 755 src/kernel/mdrun %{buildroot}%{_libdir}/mpich/bin/g_mdrun_mpich_d
cp -a src/*/*.so* %{buildroot}%{_libdir}/mpich/lib/
cd ..
%{_mpich_unload}


## Serial versions

# Single precision
cd single
make DESTDIR=%{buildroot} INSTALL="install -p" install
cd ..
# Double precision
cd double
make DESTDIR=%{buildroot} INSTALL="install -p" install
cd ..

## Now, the rest of the necessary stuff

# Install manual & packager's note
install -cpm 644 %{SOURCE1} manual.pdf
install -cpm 644 %{SOURCE6} README.fedora

# Fix GMXRC file permissions
chmod a+x %{buildroot}%{_bindir}/GMXRC %{buildroot}%{_bindir}/GMXRC.*

# Rename binaries and man pages to prevent clashes
# (This is done here so that we don't need to mess with machine generated makefiles.
#for bin in anadock do_dssp editconf eneconv genbox genconf genion genrestr gmxcheck gmxdump grompp highway luck make_edi make_ndx mdrun mk_angndx ngmx pdb2gmx protonate sigeps tpbconv trjcat trjconv trjorder wheel x2top xpm2ps xrama ; do 
for bin in do_dssp editconf eneconv genbox genconf genion genrestr gmxcheck gmxdump grompp make_edi make_ndx mdrun mk_angndx pdb2gmx tpbconv trjcat trjconv trjorder xpm2ps; do
mv %{buildroot}%{_bindir}/${bin} %{buildroot}%{_bindir}/g_${bin}
mv %{buildroot}%{_bindir}/${bin}_d %{buildroot}%{_bindir}/g_${bin}_d
done

for bin in demux.pl xplor2gmx.pl; do
mv %{buildroot}%{_bindir}/$bin %{buildroot}%{_bindir}/g_${bin}
done

# Man pages
#for bin in anadock do_dssp editconf eneconv genbox genconf genion genrestr gmxcheck gmxdump grompp highway make_edi make_ndx mdrun mk_angndx ngmx pdb2gmx protonate sigeps tpbconv trjcat trjconv trjorder wheel x2top xpm2ps xrama ; do 
for bin in do_dssp editconf eneconv genbox genconf genion genrestr gmxcheck gmxdump grompp make_edi make_ndx mdrun mk_angndx pdb2gmx tpbconv trjcat trjconv trjorder xpm2ps; do
mv %{buildroot}%{_mandir}/man1/${bin}.1 %{buildroot}%{_mandir}/man1/g_${bin}.1
#mv %{buildroot}%{_mandir}/man1/${bin}_d.1 %{buildroot}%{_mandir}/man1/g_${bin}_d.1
done

# Move completion files around
chmod a-x %{buildroot}%{_bindir}/completion.*
# Zsh
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
mv %{buildroot}%{_bindir}/completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/gromacs
# Bash
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
mv %{buildroot}%{_bindir}/completion.bash %{buildroot}/etc/bash_completion.d/gromacs
# Tcsh
mv %{buildroot}%{_bindir}/completion.csh . 

# Remove .la files
find %{buildroot} -name *.la -delete

# Get rid of executable stacks
%ifnarch aarch64 ppc64le
find %{buildroot} -name *.so.* -exec execstack -c {} \;
%endif

# Post install for libs. MPI packages don't need this.
%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


# Files section

%files
%{_bindir}/g_*

%files ngmx
%{_bindir}/ngmx*

%files common
%doc AUTHORS COPYING README manual.pdf README.fedora
%{_bindir}/GMXRC
%{_bindir}/GMXRC.bash
%{_mandir}/man1/*
%{_mandir}/man7/gromacs.*
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/template/

%files libs
%{_libdir}/libgmx.so.*
%{_libdir}/libgmx_d.so.*
%{_libdir}/libgmxana.so.*
%{_libdir}/libgmxana_d.so.*
%{_libdir}/libgmxpreprocess.so.*
%{_libdir}/libgmxpreprocess_d.so.*
%{_libdir}/libmd.so.*
%{_libdir}/libmd_d.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/libgmx.so
%{_libdir}/libgmx_d.so
%{_libdir}/libgmxana.so
%{_libdir}/libgmxana_d.so
%{_libdir}/libgmxpreprocess.so
%{_libdir}/libgmxpreprocess_d.so
%{_libdir}/libmd.so
%{_libdir}/libmd_d.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/%{name}/template/
%exclude %{_datadir}/%{name}/template/Makefile.mpi.*

%if %{with_openmpi}
%files openmpi
%{_libdir}/openmpi/bin/g_mdrun*

%files openmpi-libs
%{_libdir}/openmpi/lib/lib*.so.*

%files openmpi-devel
%{_libdir}/openmpi/lib/lib*.so
%endif

%files mpich
%{_libdir}/mpich/bin/g_mdrun*

%files mpich-libs
%{_libdir}/mpich/lib/lib*.so.*

%files mpich-devel
%{_libdir}/mpich/lib/lib*.so

%files zsh
%{_datadir}/zsh/site-functions/gromacs
%{_bindir}/GMXRC.zsh

%files bash
%config(noreplace) %{_sysconfdir}/bash_completion.d/gromacs

%files csh
%doc completion.csh
%{_bindir}/GMXRC.csh


%changelog
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
