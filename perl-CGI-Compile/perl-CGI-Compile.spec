Name:           perl-CGI-Compile
Summary:        Compile .cgi scripts to a code reference like ModPerl::Registry
Version:        0.11
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/CGI-Compile-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/CGI-Compile
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)

Requires:       perl(File::pushd)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
CGI::Compile is an utility to compile CGI scripts into a code reference
that can run many times on its own namespace, as long as the script is
ready to run on a persistent environment.

%prep
%setup -q -n CGI-Compile-%{version}

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
* Sat Mar 20 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.11-1
- specfile by Fedora::App::MaintainerTools 0.006


