Name:           perl-MooseX-RelatedClassRoles
Summary:        Apply roles to a class related to yours
Version:        0.004
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/H/HD/HDP/MooseX-RelatedClassRoles-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/MooseX-RelatedClassRoles
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(Class::MOP) >= 0.80
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose) >= 0.73
BuildRequires:  perl(MooseX::Role::Parameterized) >= 0.04

Requires:       perl(Class::MOP) >= 0.80
Requires:       perl(Moose) >= 0.73
Requires:       perl(MooseX::Role::Parameterized) >= 0.04

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
Frequently, you have to use a class that provides some 'foo_class'
accessor or attribute as a method of dependency injection. Use this role
when you'd rather apply roles to make your custom 'foo_class' instead of
manually setting up a subclass.

%prep
%setup -q -n MooseX-RelatedClassRoles-%{version}

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
* Thu May 06 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.004-1
- specfile by Fedora::App::MaintainerTools 0.006


