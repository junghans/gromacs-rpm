%ifnarch s390 s390x
%global with_openmpi 1
%else
%global with_openmpi 0
%endif

Name:		gromacs
Version:	4.5.3
Release:	2%{?dist}
Summary:	Fast, Free and Flexible Molecular Dynamics
Group:		Applications/Engineering
License:	GPLv2+
URL:		http://www.gromacs.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	ftp://ftp.gromacs.org/pub/gromacs/gromacs-%{version}.tar.gz
# File gotten from http://www.gromacs.org/@api/deki/files/126/=gromacs_manual-4.5.pdf
Source1:	manual-4.5.pdf
Source2:	gromacs-template-makefile-single
Source3:	gromacs-template-makefile-double
Source4:	gromacs-template-makefile-mpi-single
Source5:	gromacs-template-makefile-mpi-double
Source6:	gromacs-README.fedora

# Add shebangs to scripts
Patch0:		gromacs-GMXRC.patch
# Patch gmxdemo for new filenames
Patch1:		gromacs-gmxdemo.patch

BuildRequires:	cmake
BuildRequires:	atlas-devel
BuildRequires:	fftw-devel
BuildRequires:	gsl-devel
BuildRequires:	libxml2-devel
BuildRequires:	libX11-devel

Requires:	gromacs-common = %{version}-%{release}

# Libs were branched from gromacs, so there are 64-bit installs that have 32-bit packages installed
Obsoletes:	gromacs < 4.5.2-1 


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
# Due to switch to noarch package
Obsoletes:	gromacs-common < 4.0.7-1

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
# Libs were branched from gromacs, so there are 64-bit installs that have 32-bit packages installed
Obsoletes:	gromacs-openmpi < 4.5.3-2

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


%package mpich2
Summary:	GROMACS MPICH2 binaries and libraries
Group:		Applications/Engineering
Requires:	gromacs-common = %{version}-%{release}
Requires:	mpich2
# Libs were branched from gromacs, so there are 64-bit installs that have 32-bit packages installed
Obsoletes:	gromacs-mpich2 < 4.5.3-2

%description mpich2
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

mdrun has been compiled with thread parallellization (for running on
a single node) and with MPICH2 (for running on multiple nodes).
This package single and double precision binaries and libraries.

%package mpich2-libs
Summary:	GROMACS MPICH2 shared libraries
Group:		System Environment/Libraries
Requires:	mpich2

%description mpich2-libs
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains libraries needed for operation of GROMACS MPICH2.


%package mpich2-devel
Summary:	GROMACS MPICH2 development libraries
Group:		Applications/Engineering
Requires:	gromacs-devel = %{version}-%{release}
Requires:	gromacs-mpich2 = %{version}-%{release}
BuildRequires:	mpich2-devel
Requires:	mpich2-devel

%description mpich2-devel
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains development libraries for GROMACS MPICH2.
You may need it if you want to write your own analysis programs.



%package bash
Summary:	GROMACS bash completion
Group:		Applications/Engineering
Requires:	bash-completion
BuildArch:	noarch
# Due to switch to noarch package
Obsoletes:	gromacs-bash < 4.0.7-1 


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
# Due to switch to noarch package
Obsoletes:	gromacs-zsh < 4.0.7-1


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
# Due to switch to noarch package
Obsoletes:	gromacs-csh < 4.0.7-1 


%description csh
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package provides scripts needed to run GROMACS with csh and a completion
script.

%package tutor
Summary:	GROMACS tutorial files
Group:		Applications/Engineering
Requires:	gromacs-common = %{version}-%{release}
BuildArch:	noarch
# Due to switch to noarch package
Obsoletes:	gromacs-tutor < 4.0.7-1 

%description tutor
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package provides tutorials for the use of GROMACS.

%prep
%setup -q 
%patch0 -p1 -b .gmxrc
%patch1 -p1 -b .gmxdemo

# Fix incorrect permission
#chmod a-x src/tools/gmx_xpm2ps.c



%build
# First, override bug in MPICH2 packaging.
%{_mpich2_unload}

# Assembly kernels haven't got .note.GNU-stack sections
# because of incompatibilies with Microsoft Assembler.
# Add noexecstack to compiler flags

export CFLAGS="%optflags -Wa,--noexecstack -fPIC"
export LIBS="-L%{_libdir}/atlas -lblas -llapack"

# Default options, used for all compilations
export DEFOPTS="-D BUILD_SHARED_LIBS=ON -DCMAKE_SKIP_RPATH:BOOL=ON -DCMAKE_SKIP_BUILD_RPATH:BOOL=ON -DLIB=%{_lib}"
export SINGLE="-D GMX_DOUBLE=OFF" # Single precision
export DOUBLE="-D GMX_DOUBLE=ON" # Double precision
export MPI="-D GMX_MPI=ON"

# Add this to the configure options if you want to build a debug version
export NOASM="-D GMX_ACCELERATION=OFF"

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


## MPICH2
%{_mpich2_load}
# Suffix to be used for single precision is
SUFFIXCONF="-D GMX_DEFAULT_SUFFIX=OFF -D GMX_BINARY_SUFFIX=$SUFFIX -D GMX_LIBS_SUFFIX=${MPI_SUFFIX}"
# MPICH 2 is broken, so need to modify linker command
export CC="mpicc -lstdc++"
# single precision
mkdir mpich2-single
cd mpich2-single
%cmake $DEFOPTS $SINGLE $MPI $SUFFIXCONF ..
make VERBOSE=1 %{?_smp_mflags} mdrun
cd ..
# double precision
# Suffix to be used for double precision is
SUFFIXCONF="-D GMX_DEFAULT_SUFFIX=OFF -D GMX_BINARY_SUFFIX=$SUFFIX -D GMX_LIBS_SUFFIX=${MPI_SUFFIX}_d"
mkdir mpich2-double
cd mpich2-double
%cmake $DEFOPTS $DOUBLE $MPI $SUFFIXCONF ..
make VERBOSE=1 %{?_smp_mflags} mdrun
cd ..
%{_mpich2_unload}


%install
rm -rf %{buildroot}


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

## MPICH 2
%{_mpich2_load}
# Make install-mdrun target is broken, do install manually
mkdir -p %{buildroot}%{_libdir}/mpich2/{bin,lib}
# single precision
cd mpich2-single
install -p -m 755 src/kernel/mdrun %{buildroot}%{_libdir}/mpich2/bin/g_mdrun_mpich2
cp -a src/*/*.so* %{buildroot}%{_libdir}/mpich2/lib/
cd ..
# double precision
cd mpich2-double
install -p -m 755 src/kernel/mdrun %{buildroot}%{_libdir}/mpich2/bin/g_mdrun_mpich2_d
cp -a src/*/*.so* %{buildroot}%{_libdir}/mpich2/lib/
cd ..
%{_mpich2_unload}


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

# Fix location of libraries
%ifarch x86_64 sparc64
mv %{buildroot}/usr/lib/*.so* %{buildroot}%{_libdir}/
# and pkgconfig files
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
mv %{buildroot}/usr/lib/pkgconfig/* %{buildroot}%{_libdir}/pkgconfig/
%endif

# Install manual & packager's note
install -cpm 644 %{SOURCE1} .
install -cpm 644 %{SOURCE6} README.fedora

# Remove broken makefiles generated by build process
rm -rf %{buildroot}%{_datadir}/%{name}/template/Makefil*
# Install template makefiles
install -cpm 644 %{SOURCE2} %{buildroot}%{_datadir}/%{name}/template/Makefile.single
install -cpm 644 %{SOURCE3} %{buildroot}%{_datadir}/%{name}/template/Makefile.double
install -cpm 644 %{SOURCE4} %{buildroot}%{_datadir}/%{name}/template/Makefile.mpi.single
install -cpm 644 %{SOURCE5} %{buildroot}%{_datadir}/%{name}/template/Makefile.mpi.double

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
find %{buildroot} -name *.la -exec rm -rf {} \;

# Post install for libs. MPI packages don't need this.
%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%clean
rm -rf %{buildroot}


# Files section

%files
%defattr(-,root,root,-)
%{_bindir}/g_*

%files common
%defattr(-,root,root,-)
%doc AUTHORS COPYING README manual-4.5.pdf README.fedora
%{_bindir}/GMXRC
%{_bindir}/GMXRC.bash
%{_mandir}/man1/*
%{_mandir}/man7/gromacs.*
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/template/
%exclude %{_datadir}/%{name}/tutor/

%files libs
%defattr(-,root,root,-)
%{_libdir}/libgmx.so.*
%{_libdir}/libgmx_d.so.*
%{_libdir}/libgmxana.so.*
%{_libdir}/libgmxana_d.so.*
%{_libdir}/libgmxpreprocess.so.*
%{_libdir}/libgmxpreprocess_d.so.*
%{_libdir}/libmd.so.*
%{_libdir}/libmd_d.so.*

%files devel
%defattr(-,root,root,-)
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
%defattr(-,root,root,-)
%{_libdir}/openmpi/bin/g_mdrun*

%files openmpi-libs
%defattr(-,root,root,-)
%{_libdir}/openmpi/lib/lib*.so.*

%files openmpi-devel
%defattr(-,root,root,-)
%{_libdir}/openmpi/lib/lib*.so
%endif

%files mpich2
%defattr(-,root,root,-)
%{_libdir}/mpich2/bin/g_mdrun*

%files mpich2-libs
%defattr(-,root,root,-)
%{_libdir}/mpich2/lib/lib*.so.*

%files mpich2-devel
%defattr(-,root,root,-)
%{_libdir}/mpich2/lib/lib*.so

%files zsh
%defattr(-,root,root,-)
%{_datadir}/zsh/site-functions/gromacs
%{_bindir}/GMXRC.zsh

%files bash
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/bash_completion.d/gromacs

%files csh
%defattr(-,root,root,-)
%doc completion.csh
%{_bindir}/GMXRC.csh

%files tutor
%defattr(-,root,root,-)
%{_datadir}/%{name}/tutor/


%changelog
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
