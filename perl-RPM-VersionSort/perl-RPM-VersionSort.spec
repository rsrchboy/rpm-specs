Name:       perl-RPM-VersionSort 
Version:    1.00 
Release:    0%{?dist}
# license auto-determination failed
License:    CHECK(GPL+ or Artistic) 
Group:      Development/Libraries
Summary:    RPM version sorting algorithm, in perl XS 
Source:     http://search.cpan.org/CPAN/authors/id/H/HA/HAG/RPM-VersionSort-%{version}.tar.gz 
Url:        http://search.cpan.org/dist/RPM-VersionSort
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 
Requires:   perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires: perl(ExtUtils::MakeMaker)

# don't "provide" private Perl libs
%global _use_internal_dependency_generator 0
%global __deploop() while read FILE; do /usr/lib/rpm/rpmdeps -%{1} ${FILE}; done | /bin/sort -u
%global __find_provides /bin/sh -c "%{__grep} -v '%{perl_vendorarch}/.*\\.so$' | %{__deploop P}"
%global __find_requires /bin/sh -c "%{__deploop R}"

%description
RPM uses a version number sorting algorithm for some of its decisions.
It's useful to get at this sorting algoritm for other nefarious purposes
if you are using RPM at your site.


%prep
%setup -q -n RPM-VersionSort-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}
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
%doc Changes 
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_mandir}/man3/*.3*

%changelog
* Sun Jun 07 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.00-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)

