#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsonpath-rw-ext
Version  : 1.2.2
Release  : 28
URL      : https://files.pythonhosted.org/packages/d5/f0/5d865b2543be45e3ab7a8c2ae8dfa5c3e56cfdd48f19d4455eb02f370386/jsonpath-rw-ext-1.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/d5/f0/5d865b2543be45e3ab7a8c2ae8dfa5c3e56cfdd48f19d4455eb02f370386/jsonpath-rw-ext-1.2.2.tar.gz
Summary  : Extensions for JSONPath RW
Group    : Development/Tools
License  : Apache-2.0
Requires: jsonpath-rw-ext-license = %{version}-%{release}
Requires: jsonpath-rw-ext-python = %{version}-%{release}
Requires: jsonpath-rw-ext-python3 = %{version}-%{release}
Requires: jsonpath-rw
Requires: pbr
BuildRequires : buildreq-distutils3
BuildRequires : jsonpath-rw
BuildRequires : pbr

%description
===============================
python-jsonpath-rw-ext
===============================

%package license
Summary: license components for the jsonpath-rw-ext package.
Group: Default

%description license
license components for the jsonpath-rw-ext package.


%package python
Summary: python components for the jsonpath-rw-ext package.
Group: Default
Requires: jsonpath-rw-ext-python3 = %{version}-%{release}

%description python
python components for the jsonpath-rw-ext package.


%package python3
Summary: python3 components for the jsonpath-rw-ext package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jsonpath-rw-ext package.


%prep
%setup -q -n jsonpath-rw-ext-1.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562949699
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
mkdir -p %{buildroot}/usr/share/package-licenses/jsonpath-rw-ext
cp LICENSE %{buildroot}/usr/share/package-licenses/jsonpath-rw-ext/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jsonpath-rw-ext/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
