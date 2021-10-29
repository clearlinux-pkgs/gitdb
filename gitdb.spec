#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gitdb
Version  : 4.0.9
Release  : 25
URL      : https://files.pythonhosted.org/packages/fc/44/64e02ef96f20b347385f0e9c03098659cb5a1285d36c3d17c56e534d80cf/gitdb-4.0.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/fc/44/64e02ef96f20b347385f0e9c03098659cb5a1285d36c3d17c56e534d80cf/gitdb-4.0.9.tar.gz
Summary  : Git Object Database
Group    : Development/Tools
License  : BSD-3-Clause
Requires: gitdb-license = %{version}-%{release}
Requires: gitdb-python = %{version}-%{release}
Requires: gitdb-python3 = %{version}-%{release}
Requires: smmap
BuildRequires : buildreq-distutils3
BuildRequires : smmap

%description
GitDB
=====
GitDB allows you to access bare git repositories for reading and writing. It aims at allowing full access to loose objects as well as packs with performance and scalability in mind. It operates exclusively on streams, allowing to handle large objects with a small memory footprint.

%package license
Summary: license components for the gitdb package.
Group: Default

%description license
license components for the gitdb package.


%package python
Summary: python components for the gitdb package.
Group: Default
Requires: gitdb-python3 = %{version}-%{release}

%description python
python components for the gitdb package.


%package python3
Summary: python3 components for the gitdb package.
Group: Default
Requires: python3-core
Provides: pypi(gitdb)
Requires: pypi(smmap)

%description python3
python3 components for the gitdb package.


%prep
%setup -q -n gitdb-4.0.9
cd %{_builddir}/gitdb-4.0.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635204210
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gitdb
cp %{_builddir}/gitdb-4.0.9/LICENSE %{buildroot}/usr/share/package-licenses/gitdb/338a160e1cc55e2722d66d2eb5e78b149763f1f6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gitdb/338a160e1cc55e2722d66d2eb5e78b149763f1f6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
