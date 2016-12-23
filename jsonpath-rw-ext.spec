#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsonpath-rw-ext
Version  : 1.0.0
Release  : 14
URL      : https://pypi.python.org/packages/source/j/jsonpath-rw-ext/jsonpath-rw-ext-1.0.0.tar.gz
Source0  : https://pypi.python.org/packages/source/j/jsonpath-rw-ext/jsonpath-rw-ext-1.0.0.tar.gz
Summary  : Extensions for JSONPath RW
Group    : Development/Tools
License  : Apache-2.0
Requires: jsonpath-rw-ext-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Sphinx-python
BuildRequires : coverage-python
BuildRequires : decorator-python
BuildRequires : discover-python
BuildRequires : docutils
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : hacking
BuildRequires : jsonpath-rw-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : ply-python
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-subunit-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : testrepository
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : traceback2-python
BuildRequires : unittest2-python

%description
===============================
python-jsonpath-rw-ext
===============================

%package python
Summary: python components for the jsonpath-rw-ext package.
Group: Default
Requires: Babel-python
Requires: jsonpath-rw-python

%description python
python components for the jsonpath-rw-ext package.


%prep
%setup -q -n jsonpath-rw-ext-1.0.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
