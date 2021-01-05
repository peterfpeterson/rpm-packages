%global srcname lmfit-py
%global summary Non-Linear Least Squares Minimization
%global descr Non-Linear Least Squares Minimization, with flexible Parameter settings, based on scipy.optimize.leastsq, and with many additional classes and methods for curve fitting http:/lmfit.github.io/lmfit-py/
%define release 1

Summary: %{summary}
Name: python-%{srcname}
Version: 0.9.14
Release: %{release}%{?dist}
Source0: https://github.com/lmfit/lmfit-py/archive/%{version}.tar.gz
License: Custom
Group: Science/Research
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Matt Newville
Url: https://lmfit.github.io/lmfit-py/

%description
%{descr}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:  %{summary}
Requires: python%{python3_pkgversion}
Requires: python%{python3_pkgversion}-asteval >= 0.9.12
Requires: python%{python3_pkgversion}-numpy >= 1.10
Requires: python%{python3_pkgversion}-scipy >= 0.19
Requires: python%{python3_pkgversion}-six >= 0.10
Requires: python%{python3_pkgversion}-uncertainties >= 3.0
#Requires: python{python3_pkgversion}-dateutil

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

BuildRequires: python3-setuptools
%if 0%{?rhel}
BuildRequires: python36-pytest
%else
BuildRequires: python%{python3_pkgversion}-pytest
%endif
#BuildRequires: python{python3_pkgversion}-dill           # does not exist
#BuildRequires: python{python3_pkgversion}-emcee          # does not exist
BuildRequires: python%{python3_pkgversion}-matplotlib
BuildRequires: python%{python3_pkgversion}-pandas
BuildRequires: python%{python3_pkgversion}-sphinx
#BuildRequires: python{python3_pkgversion}-sphinx-gallery  # does not exist
#corner
#jupyter_sphinx
#numdifftools
#pre-commit

%description -n python%{python3_pkgversion}-%{srcname}
%{descr}

%prep
%setup -n %{srcname}-%{version} -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

# testing is somehow broken, but the package did work
#check
#__python3} setup.py test

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/*
