Name:           perl-CatalystX-RoleApplicator
Summary:        Apply roles to your Catalyst application-related classes
Version:        0.005
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/H/HD/HDP/CatalystX-RoleApplicator-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/CatalystX-RoleApplicator
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(Catalyst::Runtime) >= 5.7
BuildRequires:  perl(Class::MOP) >= 0.80
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose) >= 0.73
BuildRequires:  perl(MooseX::RelatedClassRoles) >= 0.003

Requires:       perl(Catalyst::Runtime) >= 5.7
Requires:       perl(Class::MOP) >= 0.80
Requires:       perl(Moose) >= 0.73
Requires:       perl(MooseX::RelatedClassRoles) >= 0.003

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
CatalystX::RoleApplicator makes it easy for you to apply roles to all
the various classes that your Catalyst application uses.

%prep
%setup -q -n CatalystX-RoleApplicator-%{version}

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
* Thu May 06 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.005-1
- specfile by Fedora::App::MaintainerTools 0.006


