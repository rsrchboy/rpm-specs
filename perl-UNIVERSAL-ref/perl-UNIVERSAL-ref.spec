Name:           perl-UNIVERSAL-ref
Summary:        Turns ref() into a multimethod
Version:        0.12
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/J/JJ/JJORE/UNIVERSAL-ref-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/UNIVERSAL-ref
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(B::Utils)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

Requires:       perl(B::Utils)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
This module changes the behavior of the builtin function ref(). If
ref() is called on an object that has requested an overloaded ref,
the object's '->ref' method will be called and its return value
used instead.

%prep
%setup -q -n UNIVERSAL-ref-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_mandir}/man3/*.3*

%changelog
* Sat Apr 03 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.12-1
- specfile by Fedora::App::MaintainerTools 0.006


