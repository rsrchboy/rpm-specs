Name:           perl-MooseX-MarkAsMethods
Summary:        Mark overload code symbols as methods
Version:        0.05
Release:        1%{?dist}
License:        LGPLv2 or LGPLv3
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/R/RS/RSRCHBOY/MooseX-MarkAsMethods-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/MooseX-MarkAsMethods
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(B::Hooks::EndOfScope)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Perl6::Junction)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More)

Requires:       perl(B::Hooks::EndOfScope)
Requires:       perl(namespace::autoclean)
Requires:       perl(namespace::clean)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
MooseX::MarkAsMethods allows one to easily mark certain functions as
Moose methods. This will allow other packages such as
namespace::autoclean to operate without, say, blowing away your
overloads.By default we check for overloads, and mark those functions as
methods.  If 'autoclean => 1' is passed to import on use'ing this module,
we will clean out all non-methods in the same fashion
namespace::autoclean does, except without the ability to specify
additional non-methods to nuke.

%prep
%setup -q -n MooseX-MarkAsMethods-%{version}

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
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Thu May 06 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.05-1
- specfile by Fedora::App::MaintainerTools 0.006


