Name:           perl-Catalyst-TraitFor-Request-BrowserDetect
Summary:        Browser detection for Catalyst::Requests
Version:        0.02
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Catalyst-TraitFor-Request-BrowserDetect-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/Catalyst-TraitFor-Request-BrowserDetect
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(aliased)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(CatalystX::RoleApplicator)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::BrowserDetect)
BuildRequires:  perl(Moose)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(aliased)
Requires:       perl(Catalyst)
Requires:       perl(CatalystX::RoleApplicator)
Requires:       perl(HTTP::BrowserDetect)
Requires:       perl(Moose)
Requires:       perl(namespace::autoclean)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
Extend request objects with a method for browser detection.

%prep
%setup -q -n Catalyst-TraitFor-Request-BrowserDetect-%{version}

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
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Thu May 06 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.02-1
- specfile by Fedora::App::MaintainerTools 0.006


