#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gitdb
Version  : 0.6.4
Release  : 5
URL      : https://files.pythonhosted.org/packages/e3/95/7e5d7261feb46c0539ac5e451be340ddd64d78c5118f2d893b052c76fe8c/gitdb-0.6.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/e3/95/7e5d7261feb46c0539ac5e451be340ddd64d78c5118f2d893b052c76fe8c/gitdb-0.6.4.tar.gz
Summary  : Git Object Database
Group    : Development/Tools
License  : BSD-3-Clause
Requires: gitdb-license = %{version}-%{release}
Requires: gitdb-python = %{version}-%{release}
Requires: gitdb-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

%description
No detailed description available

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

%description python3
python3 components for the gitdb package.


%prep
%setup -q -n gitdb-0.6.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565625727
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
cp LICENSE %{buildroot}/usr/share/package-licenses/gitdb/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gitdb/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
