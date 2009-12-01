Name:		gromacs
Version:	4.0.5
Release:	3%{?dist}
Summary:	Fast, Free and Flexible Molecular Dynamics
Group:		Applications/Engineering
License:	GPLv2+
URL:		http://www.gromacs.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	ftp://ftp.gromacs.org/pub/gromacs/gromacs-%{version}.tar.gz
Source1:	ftp://ftp.gromacs.org/pub/manual/manual-4.0.pdf
Source2:	gromacs-template-makefile-single
Source3:	gromacs-template-makefile-double
Source4:	gromacs-template-makefile-mpi-single
Source5:	gromacs-template-makefile-mpi-double
Source6:	gromacs-README.fedora

# Add shebangs to scripts
Patch0:		gromacs-GMXRC.patch
# Patch gmxdemo for new filenames
Patch1:		gromacs-gmxdemo.patch
# Patch configure for the library suffix
Patch2:		gromacs-configure.patch

BuildRequires:	blas-devel
BuildRequires:	fftw-devel
BuildRequires:	gsl-devel
BuildRequires:	lapack-devel
BuildRequires:	libxml2-devel
BuildRequires:	libX11-devel


Requires:	gromacs-common = %{version}-%{release}


%description
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package provides single and double precision binaries.
The documentation is in the package gromacs-common.

N.B. All binaries have names starting with g_, for example mdrun has been
renamed to g_mdrun.


%package common
Summary:	GROMACS shared data and documentation
Group:		Applications/Engineering
BuildArch:	noarch
# Due to switch to noarch package
Obsoletes:	gromacs-common < %{version}-%{release}

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

This package provides Open MPI single precision and double precision binaries
and libraries.


%package openmpi-devel
Summary:	GROMACS Open MPI development libraries
Group:		Applications/Engineering
Obsoletes:	gromacs-mpi-devel < %{version}-%{release}
Requires:	gromacs-devel = %{version}-%{release}
Requires:	openmpi-devel


%description openmpi-devel
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains development libraries for GROMACS Open MPI.
You need it if you want to write your own analysis programs.


%package mpich2
Summary:	GROMACS MPICH2 binaries and libraries
Group:		Applications/Engineering
Requires:	gromacs-common = %{version}-%{release}
Requires:	mpich2

%description mpich2
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package provides MPICH2 single precision and double precision binaries
and libraries.


%package mpich2-devel
Summary:	GROMACS MPICH2 development libraries
Group:		Applications/Engineering
Requires:	gromacs-devel = %{version}-%{release}
BuildRequires:	mpich2-devel
Requires:	mpich2-devel

%description mpich2-devel
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains development libraries for GROMACS MPICH2.
You need it if you want to write your own analysis programs.



%package bash
Summary:	GROMACS bash completion
Group:		Applications/Engineering
Requires:	bash-completion
BuildArch:	noarch
# Due to switch to noarch package
Obsoletes:	gromacs-common < %{version}-%{release}


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
Obsoletes:	gromacs-common < %{version}-%{release}


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
Obsoletes:	gromacs-common < %{version}-%{release}


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
Obsoletes:	gromacs-common < %{version}-%{release}

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
%patch2 -p1 -b .libsuffix

# Fix incorrect permission
#chmod a-x src/tools/gmx_xpm2ps.c



%build
# Assembly kernels haven't got .note.GNU-stack sections
# because of incompatibilies with Microsoft Assembler.
# Add noexecstack to compiler flags

export CFLAGS="%optflags -Wa,--noexecstack -fPIC"
export LIBS="-lblas -llapack"

# Default options, used for all compilations
export DEFOPTS="--enable-shared --disable-static --with-external-blas \
	--with-external-lapack --with-gsl --with-x"
export SINGLE="--enable-float" # Single precision
export DOUBLE="--disable-float" # Double precision
export MPI="--enable-mpi"

# Add this to the configure options if you want to build a debug version
export NOASM="--disable-ia32-3dnow --disable-ia32-sse --disable-x86-64-sse \
	--disable-ppc-altivec --disable-ia64-asm"


# Single precision
mkdir single
cd single
sed "s|@LIBSUFFIX@||g" < ../configure > configure; chmod 777 configure
%configure $DEFOPTS $SINGLE
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}
cd ..

# Double precision
mkdir double
cd double
sed "s|@LIBSUFFIX@|_d|g" < ../configure > configure; chmod 777 configure
%configure $DEFOPTS $DOUBLE --program-suffix="_d"
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}
cd ..


### MPI versions
export CC=mpicc
export CXX=mpicxx
export F77=mpif77
export F90=mpif90
export FC=mpif90

## Open MPI
%{_openmpi_load}
# single precision
mkdir openmpi-single
cd openmpi-single
sed "s|@LIBSUFFIX@|_mpi|g" < ../configure > configure; chmod 777 configure
%configure $DEFOPTS $SINGLE $MPI --program-suffix=${MPI_SUFFIX} --bindir=${MPI_BIN} --libdir=${MPI_LIB}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} mdrun
cd ..
# double precision
mkdir openmpi-double
cd openmpi-double
sed "s|@LIBSUFFIX@|_mpi_d|g" < ../configure > configure; chmod 777 configure
%configure $DEFOPTS $DOUBLE $MPI --program-suffix=${MPI_SUFFIX}_d --bindir=${MPI_BIN} --libdir=${MPI_LIB}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} mdrun
cd ..
# unload
%{_openmpi_unload}

## MPICH2
%{_mpich2_load}
# single precision
mkdir mpich2-single
cd mpich2-single
sed "s|@LIBSUFFIX@|_mpi|g" < ../configure > configure; chmod 777 configure
%configure $DEFOPTS $SINGLE $MPI --program-suffix=${MPI_SUFFIX} --bindir=${MPI_BIN} --libdir=${MPI_LIB}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} mdrun
cd ..
# double precision
mkdir mpich2-double
cd mpich2-double
sed "s|@LIBSUFFIX@|_mpi_d|g" < ../configure > configure; chmod 777 configure
%configure $DEFOPTS $DOUBLE $MPI --program-suffix=${MPI_SUFFIX}_d --bindir=${MPI_BIN} --libdir=${MPI_LIB}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} mdrun
cd ..
%{_mpich2_unload}


%install
rm -rf %{buildroot}


## Open MPI
%{_openmpi_load}
# single precision
cd openmpi-single
make DESTDIR=%{buildroot} INSTALL="install -p" BINDIR=${MPI_BIN} LIBDIR=${MPI_LIB} install-mdrun
cd ..
# double precision
cd openmpi-double
make DESTDIR=%{buildroot} INSTALL="install -p" BINDIR=${MPI_BIN} LIBDIR=${MPI_LIB} install-mdrun
cd ..
%{_openmpi_unload}

## MPICH 2
%{_mpich2_load}
# single precision
cd mpich2-single
make DESTDIR=%{buildroot} INSTALL="install -p" BINDIR=${MPI_BIN} LIBDIR=${MPI_LIB} install-mdrun
cd ..
# double precision
cd mpich2-double
make DESTDIR=%{buildroot} INSTALL="install -p" BINDIR=${MPI_BIN} LIBDIR=${MPI_LIB} install-mdrun
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
for bin in anadock do_dssp editconf eneconv genbox genconf genion genrestr gmxcheck gmxdump grompp highway luck make_edi make_ndx mdrun mk_angndx ngmx pdb2gmx protonate sigeps tpbconv trjcat trjconv trjorder wheel x2top xpm2ps xrama ; do 
mv %{buildroot}%{_bindir}/${bin} %{buildroot}%{_bindir}/g_${bin}
mv %{buildroot}%{_bindir}/${bin}_d %{buildroot}%{_bindir}/g_${bin}_d
done

for bin in demux.pl xplor2gmx.pl; do
mv %{buildroot}%{_bindir}/$bin %{buildroot}%{_bindir}/g_${bin}
done

# MPI-enabled binaries (list will continue when the makefile has
# the possibility to compile all mpi-enabled files
for mpi in openmpi mpich2; do
 for mpibin in mdrun; do
  mv %{buildroot}%{_libdir}/$mpi/bin/${mpibin}_${mpi} %{buildroot}%{_libdir}/$mpi/bin/g_${mpibin}_${mpi}
  mv %{buildroot}%{_libdir}/$mpi/bin/${mpibin}_${mpi}_d %{buildroot}%{_libdir}/$mpi/bin/g_${mpibin}_${mpi}_d
 done
done

# Man pages
for bin in anadock do_dssp editconf eneconv genbox genconf genion genrestr gmxcheck gmxdump grompp highway make_edi make_ndx mdrun mk_angndx ngmx pdb2gmx protonate sigeps tpbconv trjcat trjconv trjorder wheel x2top xpm2ps xrama ; do 
mv %{buildroot}%{_mandir}/man1/${bin}.1 %{buildroot}%{_mandir}/man1/g_${bin}.1
mv %{buildroot}%{_mandir}/man1/${bin}_d.1 %{buildroot}%{_mandir}/man1/g_${bin}_d.1
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
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}


# Files section

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/libgmx.so.*
%{_libdir}/libgmx_d.so.*
%{_libdir}/libgmxana.so.*
%{_libdir}/libgmxana_d.so.*
%{_libdir}/libmd.so.*
%{_libdir}/libmd_d.so.*

%files common
%defattr(-,root,root,-)
%doc AUTHORS COPYING README manual-4.0.pdf README.fedora
%{_bindir}/GMXRC
%{_bindir}/GMXRC.bash
%{_mandir}/man1/*
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/template
%exclude %{_datadir}/%{name}/tutor

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/libgmx.so
%{_libdir}/libgmx_d.so
%{_libdir}/libgmxana.so
%{_libdir}/libgmxana_d.so
%{_libdir}/libmd.so
%{_libdir}/libmd_d.so
%{_datadir}/%{name}/template
%exclude %{_datadir}/%{name}/template/Makefile.mpi.*

%files openmpi
%defattr(-,root,root,-)
%{_libdir}/openmpi/bin/g_mdrun*
%{_libdir}/openmpi/lib/lib*.so.*

%files openmpi-devel
%defattr(-,root,root,-)
%{_libdir}/openmpi/lib/lib*.so

%files mpich2
%defattr(-,root,root,-)
%{_libdir}/mpich2/bin/g_mdrun*
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
%{_datadir}/%{name}/tutor


%changelog
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
