Name:           perl-HTTP-Parser-XS
Summary:        A fast, primitive HTTP request parser
Version:        0.07
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/K/KA/KAZUHO/HTTP-Parser-XS-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/HTTP-Parser-XS
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
HTTP::Parser::XS is a fast, primitive HTTP request parser that can
be used either for writing a synchronous HTTP server or an event-
driven server.

%prep
%setup -q -n HTTP-Parser-XS-%{version}

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
* Sun Mar 21 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.07-1
- specfile by Fedora::App::MaintainerTools 0.006


