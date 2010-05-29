Name:           plack
Summary:        Perl Superglue for Web frameworks and Web Servers (PSGI toolkit)
Version:        0.9937
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/Plack-%{version}.tar.gz 
Source100:      %{name}.macros
URL:            http://search.cpan.org/dist/Plack
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

# the canonical name
Provides:       perl-Plack = %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Devel::StackTrace::AsHTML)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(Filesys::Notify::Simple)
BuildRequires:  perl(Hash::MultiValue) >= 0.05
BuildRequires:  perl(HTTP::Body) >= 1.06
BuildRequires:  perl(LWP) >= 5.814
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP) >= 0.11
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI) >= 1.36

# optional tests
BuildRequires:  perl(Authen::Simple::Password)
BuildRequires:  perl(IO::Handle::Util)
BuildRequires:  perl(Log::Dispatch::Array)

Requires:       perl(Devel::StackTrace)
Requires:       perl(Devel::StackTrace::AsHTML) >= 0.09
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(Filesys::Notify::Simple)
Requires:       perl(Hash::MultiValue) >= 0.05
Requires:       perl(HTTP::Body) >= 1.06
Requires:       perl(LWP) >= 5.814
Requires:       perl(parent)
Requires:       perl(Pod::Usage)
Requires:       perl(Test::TCP) >= 0.11
Requires:       perl(Try::Tiny)
Requires:       perl(URI) >= 1.36

# include our package-specific macros 
%include %{SOURCE100}

%plack_handler_pkg Apache2
%plack_handler_pkg FCGI 
%plack_handler_pkg HTTP-Server
%plack_handler_pkg Net-FastCGI
# we don't have 1.3.x in Fedora :)
#plack_handler_pkg Apache1

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
Plack is a set of tools for using the PSGI stack. It contains
middleware components, a reference server and utilities for web
application frameworks. Plack is like Ruby's Rack or Python's
Paste for WSGI.

See the PSGI manpage for the PSGI specification and the PSGI::FAQ 
manpage to learn more about PSGI and Plack and why we need them.

%prep
%setup -q -n Plack-%{version}

find . -type f -exec chmod -c -x {} +

%plack_handler_pkg_files Apache2
%plack_handler_pkg_files FCGI 
%plack_handler_pkg_files HTTP-Server
%plack_handler_pkg_files Net-FastCGI
# not a typo leaving this in -- handles excluding the Apache1 files for us
%plack_handler_pkg_files Apache1

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
export TEST_FCGI_CLIENT=1
make test


%clean
rm -rf %{buildroot}
rm %{main_excludes}

%files -f %{main_excludes}
%defattr(-,root,root,-)
%doc Changes README benchmarks/ eg/
%{perl_vendorlib}/*
%{_mandir}/man[13]/*
%{_bindir}/*

%changelog
* Sat May 22 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.9937-1
- update to 0.9937

* Sat May 08 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.9935-1
- update to 0.9935
- break out new handler subpackage -- Net-FastCGI

* Sun Apr 11 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.9929-1
- update to 0.9929
- add additional optional test BR's for packages now up for review

* Sat Mar 20 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.9920-1
- specfile by Fedora::App::MaintainerTools 0.006


