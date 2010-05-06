Name:           perl-MooseX-Traits
Summary:        Automatically apply roles at object creation time
Version:        0.09
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/J/JR/JROCKWAY/MooseX-Traits-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/MooseX-Traits
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(Class::MOP) >= 0.84
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(ok)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)

Requires:       perl(Class::MOP) >= 0.84
Requires:       perl(Moose)
Requires:       perl(Moose::Role)
Requires:       perl(namespace::autoclean)
Requires:       perl(Sub::Exporter)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
Often you want to create components that can be added to a class
arbitrarily. This module makes it easy for the end user to use these
components. Instead of requiring the user to create a named class with
the desired roles applied, or apply roles to the instance one-by-one, he
can just create a new class from yours with 'with_traits', and then
instantiate that.There is also 'new_with_traits', which exists for
compatability reasons. It accepts a 'traits' parameter, creates a new
class with those traits, and then insantiates it. Class-
>new_with_traits( traits => [qw/Foo Bar/], foo => 42, bar => 1 )

%prep
%setup -q -n MooseX-Traits-%{version}

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
* Thu May 06 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.09-1
- specfile by Fedora::App::MaintainerTools 0.006


