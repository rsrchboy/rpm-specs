
%global dojo_dir      %{_datadir}/dojo

Name:           dojo
Version:        1.4.3
Release:        1%{?dist}
Summary:        The Dojo JavaScript Toolkit
Source0:        http://download.dojotoolkit.org/release-%{version}/dojo-release-%{version}.tar.gz

Group:          Development/Libraries
License:        AFLv2.1 or BSD
URL:            http://dojotoolkit.org
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# yum conf, apache conf, etc.
Requires:       dojo-conf

%description
Dojo saves you time, delivers powerful performance, and scales with your
development process. It's the toolkit experienced developers turn to for
building great web experiences.

%prep
%setup -q -n dojo-release-%{version}

# just in case.
find . -type f -exec chmod -c -x {} +
%{_fixperms} *

%build
# no-op

%install
rm -rf %{buildroot}

# install...
mkdir -p %{buildroot}%{dojo_dir}/%{version}
tar -cf - * | ( cd %{buildroot}%{dojo_dir}/%{version} && tar -xf - ) 

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc dojo/LICENSE
%{dojo_dir}/

%changelog
* Fri Apr 02 2010 Chris Weyl <cweyl@alumni.drew.edu> 1.4.3-1
- dojo 1.4.3

* Fri Mar 26 2010 Chris Weyl <cweyl@alumni.drew.edu> 1.4.2-1
- initial packaging

