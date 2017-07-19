# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?__python2: %global __python2 %__python}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

%if 0%{?fedora}
%bcond_without python3
%else
%bcond_with python3
%endif

Name:           pyqtgraph
Version:        0.10.0
Release:        1%{?dist}
Summary:        A pure-Python graphics library for PyQt/PySide

License:        MIT
URL:            http://www.pyqtgraph.org
Source0:        https://github.com/pyqtgraph/pyqtgraph/archive/pyqtgraph-%{version}.tar.gz

BuildArch:
BuildRequires:  python2-devel
%if %{with python3}
BuildRequires:  python3-devel
%endif # with python3

%description
A pure-Python graphics library for PyQt/PySide

%if %{with python3}
%package     -n
Summary:

%description -n

%endif # with python3


%prep
%autosetup -c
mv %{name}-%{version} python2

%if %{with python3}
cp -a python2 python3
%endif # with python3


%build
pushd python2
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build
popd

%if %{with python3}
pushd python3
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd
%endif # with python3


%install
rm -rf $RPM_BUILD_ROOT
# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if %{with python3}
pushd python3
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
%endif # with python3

pushd python2
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd


%check
pushd python2
%{__python2} setup.py test
popd

%if %{with python3}
pushd python3
%{__python3} setup.py test
popd
%endif


%files
%license add-license-file-here
%doc add-docs-here
# For noarch packages: sitelib
%{python2_sitelib}/*
# For arch-specific packages: sitearch
%{python2_sitearch}/*

%if %{with python3}
%files -n
%license add-license-file-here
%doc add-docs-here
# For noarch packages: sitelib
%{python3_sitelib}/*
# For arch-specific packages: sitearch
%{python3_sitearch}/*
%endif # with python3


%changelog
* Fri Nov 11 2016 Stuart I. Campbell, 8600 MS-6475 <stuart@stuartcampbell.me>
- Initial version
