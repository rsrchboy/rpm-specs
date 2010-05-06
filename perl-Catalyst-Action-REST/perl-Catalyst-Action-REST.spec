Name:       perl-Catalyst-Action-REST 
Version:    0.66 
Release:    0%{?dist}
# lib/Catalyst/Action/Deserialize.pm -> GPL+ or Artistic
# lib/Catalyst/Action/REST.pm -> GPL+ or Artistic
# lib/Catalyst/Action/Serialize.pm -> GPL+ or Artistic
# lib/Catalyst/Action/SerializeBase.pm -> GPL+ or Artistic
# lib/Catalyst/Controller/REST.pm -> GPL+ or Artistic
# lib/Catalyst/Request/REST.pm -> GPL+ or Artistic
License:    GPL+ or Artistic 
Group:      Development/Libraries
Summary:    Automated REST Method Dispatching 
Source:     http://search.cpan.org/CPAN/authors/id/J/JS/JSHIRLEY/Catalyst-Action-REST-%{version}.tar.gz 
Url:        http://search.cpan.org/dist/Catalyst-Action-REST
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 
Requires:   perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:  noarch

BuildRequires: perl(Catalyst) >= 5.7001
BuildRequires: perl(Class::Inspector) >= 1.13
BuildRequires: perl(Data::Dump)
BuildRequires: perl(Data::Serializer) >= 0.36
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(LWP::UserAgent) >= 2.033
BuildRequires: perl(Module::Pluggable::Object)
BuildRequires: perl(Params::Validate) >= 0.76
BuildRequires: perl(URI::Find)
BuildRequires: perl(YAML::Syck) >= 0.67



%description
This Action handles doing automatic method dispatching for REST
requests. It takes a normal Catalyst action, and changes the dispatch to
append an underscore and method name. For example, in the synopsis
above, calling GET on "/foo" would result in the foo_GET method being
dispatched.If a method is requested that is not implemented, this action
will return a status 405 (Method Not Found). It will populate the
"Allow" header with the list of implemented request methods. You can
override this behavior by implementing a custom 405 handler like so:



%prep
%setup -q -n Catalyst-Action-REST-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root,-)
%doc Changes README 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Wed Mar 18 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.66-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)

