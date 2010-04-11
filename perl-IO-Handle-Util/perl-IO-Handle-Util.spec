Name:           perl-IO-Handle-Util
Summary:        Utilities for working with IO::Handle-like objects
Version:        0.01
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/N/NU/NUFFIN/IO-Handle-Util-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/IO-Handle-Util
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(asa)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::use::ok)

Requires:       perl(asa)
Requires:       perl(IO::String)
Requires:       perl(parent)
Requires:       perl(Scalar::Util)
Requires:       perl(Sub::Exporter)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
This module provides a number of helpful routines to manipulate or
create IO::Handle like objects.

%prep
%setup -q -n IO-Handle-Util-%{version}

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
%doc 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Sun Apr 11 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.01-1
- specfile by Fedora::App::MaintainerTools 0.006


