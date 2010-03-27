
%global dojo_dir       %{_datadir}/dojo
%global httpd_conf_dir %{_sysconfdir}/httpd/conf.d

Name:           dojo-conf
Version:        1.4
Release:        1%{?dist}
Summary:        The Dojo JavaScript Toolkit configuration

Source0:        yum.conf
Source1:        apache2.conf

Group:          Development/Libraries
License:        AFLv2 or BSD
URL:            http://dojotoolkit.org
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Dojo saves you time, delivers powerful performance, and scales with your
development process. It's the toolkit experienced developers turn to for
building great web experiences.

This package delivers config files to allow Apache to access dojo
automatically and to keep yum from trying to upgrade the "dojo" package (only
ever install successive versions).

%prep
# no-op

%build
# no-op

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_sysconfdir}/yum
cp %{SOURCE0} %{buildroot}/%{_sysconfdir}/yum/dojo.conf

mkdir -p %{buildroot}/%{httpd_conf_dir}
cat %{SOURCE1} | perl -pe 's!XXXX!%{_datadir}/dojo!' > %{buildroot}/%{httpd_conf_dir}/dojo.conf

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_sysconfdir}/yum/dojo.conf
%{httpd_conf_dir}/dojo.conf

%changelog
* Fri Mar 26 2010 Chris Weyl <cweyl@alumni.drew.edu> 1.4-1
- initial packaging

