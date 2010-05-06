Name:           perl-Catalyst-Action-REST
Summary:        Automated REST Method Dispatching
Version:        0.83
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/Catalyst-Action-REST-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/Catalyst-Action-REST
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(Catalyst::Runtime) >= 5.80
BuildRequires:  perl(Class::Inspector) >= 1.13
BuildRequires:  perl(Data::Serializer) >= 0.36
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(LWP::UserAgent) >= 2.033
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MRO::Compat) >= 0.10
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Params::Validate) >= 0.76
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI::Find)
BuildRequires:  perl(YAML::Syck) >= 0.67

Requires:       perl(Catalyst::Runtime) >= 5.80
Requires:       perl(Class::Inspector) >= 1.13
Requires:       perl(Data::Serializer) >= 0.36
Requires:       perl(LWP::UserAgent) >= 2.033
Requires:       perl(Module::Pluggable::Object)
Requires:       perl(Moose)
Requires:       perl(MRO::Compat) >= 0.10
Requires:       perl(namespace::autoclean)
Requires:       perl(Params::Validate) >= 0.76
Requires:       perl(URI::Find)
Requires:       perl(YAML::Syck) >= 0.67

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
This Action handles doing automatic method dispatching for REST
requests. It takes a normal Catalyst action, and changes the dispatch to
append an underscore and method name. First it will try dispatching to
an action with the generated name, and failing that it will try to
dispatch to a regular method.For example, in the synopsis above, calling
GET on "/foo" would result in the foo_GET method being dispatched.If a
method is requested that is not implemented, this action will return a
status 405 (Method Not Found). It will populate the "Allow" header with
the list of implemented request methods. You can override this behavior
by implementing a custom 405 handler like so:

%prep
%setup -q -n Catalyst-Action-REST-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}
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
* Thu May 06 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.83-1
- specfile by Fedora::App::MaintainerTools 0.006


