#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gitdb
Version  : 4.0.2
Release  : 9
URL      : https://files.pythonhosted.org/packages/53/e5/893d1f727a00d598466192360c0313c68e5aec7629c7647210b50e285f2b/gitdb-4.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/53/e5/893d1f727a00d598466192360c0313c68e5aec7629c7647210b50e285f2b/gitdb-4.0.2.tar.gz
Summary  : Git Object Database
Group    : Development/Tools
License  : BSD-3-Clause
Requires: gitdb-license = %{version}-%{release}
Requires: gitdb-python = %{version}-%{release}
Requires: gitdb-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
GitDB is a pure-Python git object database

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

%description python3
python3 components for the gitdb package.


%prep
%setup -q -n gitdb-4.0.2
cd %{_builddir}/gitdb-4.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582929937
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gitdb
cp %{_builddir}/gitdb-4.0.2/LICENSE %{buildroot}/usr/share/package-licenses/gitdb/85fecc66fdbbf8449e2d81d00ca036333fc2e975
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gitdb/85fecc66fdbbf8449e2d81d00ca036333fc2e975

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
