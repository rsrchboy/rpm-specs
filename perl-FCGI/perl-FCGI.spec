Name:           perl-FCGI
Summary:        FastCGI Perl bindings
# needed to properly replace/obsolete fcgi-perl
Epoch:          1
Version:        0.71
Release:        1%{?dist}
# same as fcgi
License:        BSD
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/FCGI-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/FCGI
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(ExtUtils::MakeMaker)

Provides:       fcgi-perl =  %{epoch}:%{version}-%{release}
Obsoletes:      fcgi-perl =< 2.4.0

%{?perl_default_filter}

%description
%{summary}.

%prep
%setup -q -n FCGI-%{version}
find . -type f -exec chmod -c -x {} +

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
%doc ChangeLog README LICENSE.TERMS echo.PL remote.PL threaded.PL
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_mandir}/man3/*.3*

%changelog
* Sat May 08 2010 Chris Weyl <cweyl@alumni.drew.edu> 1:0.71-1
- specfile by Fedora::App::MaintainerTools 0.006


