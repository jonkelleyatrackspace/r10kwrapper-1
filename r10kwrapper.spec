%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define _unpackaged_files_terminate_build 0 
%define _missing_doc_files_terminate_build 0 

%define module_name r10kwrapper

Name:           %{module_name}
Version:        0.3.2
Release:        1
Epoch:          2
Summary:        r10kwrapper - A tool that does a bit of automation and management around the use of the r10k command.

License:        Apache License Version 2.0
URL:            https://github.com/jonkelleyatrackspace/r10kwrapper
Source0:        %{module_name}-%{version}.tar.gz
Requires:       python-setuptools
BuildArch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  python-devel

%description

%prep
%setup -q -n %{module_name}-%{version}


%build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT

%files
#%doc README.md
%{python_sitelib}/*
%attr(0755,-,-) %{_bindir}/r10kwrapper

%changelog
* Thu Aug 12 2015 Jonathan Kelley <jon.kelley@rackspace.com> 0.3.2
- Fixed bug in the all_global_hiera ifelse logic
* Thu Aug 12 2015 Jonathan Kelley <jon.kelley@rackspace.com> 0.3.1
- Added osmkdir for non existing targets.
- Added built in config option all_global_hiera, to auto apply all hieras.
- Added built in config option all_product_hiera, to auto apply all product hieras.
* Thu Nov 17 2014 Jonathan Kelley <jon.kelley@rackspace.com> 0.1.3
- Fixed error reporting.
- Added the ability to fetch a seperate `R10K_BINARY` based on environment.
- Export a sensible PATH. 
* Thu Oct 2 2014 Jonathan Kelley <jon.kelley@rackspace.com> - 0.1.2
- Initial spec
