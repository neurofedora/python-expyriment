%global upname expyriment
%{!?__python2: %global __python2 %__python}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           python-expyriment
Version:        0.8.0
Release:        1%{?dist}
Summary:        Python library for cognitive and neuroscientific experiments
License:        GPLv3
URL:            http://www.expyriment.org/
Source0:        %{upname}.tar.gz
BuildRequires:  python2-devel, python-pip, pygame-devel, numpy, pyserial, pypar-common

%description
Expyriment is an open-source and platform-independent
lightweight Python library for designing and conducting
timing-critical behavioral and neuroimaging experiments.
The major goal is to provide a well-structured Python
library for script-based experiment development, with
a high priority being the readability of the resulting
program code. Due to the availability of an Android
runtime environment, Expyriment is also suitable for
the development of experiments running on tablet PCs
or smart-phones.


%prep
%setup -qn %{upname}

%build
%py2_build

%install
%py2_install

%files
%doc
%{python2_sitelib}/*
%{python2_sitearch}/*

%changelog
* Wed Nov  4 2015 Adrian Alves <alvesadrian@fedoraproject.org> 0.8.0-1
- Initial Build
