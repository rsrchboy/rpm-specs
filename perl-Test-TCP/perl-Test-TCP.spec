Name:           perl-Test-TCP
Summary:        TCP program testing utilities
Version:        0.16
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/T/TO/TOKUHIROM/Test-TCP-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/Test-TCP
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(IO::Socket::INET) >= 1.31
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::SharedFork) >= 0.09
BuildRequires:  perl(YAML)

# note versioning
Requires:       perl(IO::Socket::INET) >= 1.31
Requires:       perl(Test::SharedFork) >= 0.09

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
Test::TCP provides utilities to assist in testing TCP/IP programs.

%prep
%setup -q -n Test-TCP-%{version}

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
* Sat Mar 20 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.16-1
- specfile by Fedora::App::MaintainerTools 0.006


