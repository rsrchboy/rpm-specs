Name:           perl-Catalyst-Engine-PSGI
Summary:        PSGI engine for Catalyst
Version:        0.08
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/Catalyst-Engine-PSGI-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/Catalyst-Engine-PSGI
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(Catalyst::Action::RenderView)
BuildRequires:  perl(Catalyst::Runtime) >= 5.80007
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP)

Requires:       perl(Catalyst::Action::RenderView)
Requires:       perl(Catalyst::Runtime) >= 5.80007

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
%{summary}.

%prep
%setup -q -n Catalyst-Engine-PSGI-%{version}

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
* Sat Mar 27 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.08-1
- specfile by Fedora::App::MaintainerTools 0.006


