Name:           perl-Devel-StackTrace-AsHTML
Summary:        Displays a stack trace in HTML
Version:        0.09
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/Devel-StackTrace-AsHTML-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/Devel-StackTrace-AsHTML
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
Devel::StackTrace::AsHTML adds an 'as_html' method to Devel::StackTrace
which displays the stack trace in beautiful HTML, with code snippet
context and function parameters. If you call it on an instance of
Devel::StackTrace::WithLexicals, you even get to see the lexical
variables of each stack frame.

%prep
%setup -q -n Devel-StackTrace-AsHTML-%{version}

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
%doc Changes README eg/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Sun Apr 11 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.09-1
- specfile by Fedora::App::MaintainerTools 0.006


