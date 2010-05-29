Name:           couchdb-view-server-perl
Summary:        Handle and create CouchDB views in Perl
Version:        0.003
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/H/HD/HDP/CouchDB-View-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/CouchDB-View
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

# the canonical name
Provides:       perl-CouchDB-View = %{version}-%{release}

Requires:       couchdb

BuildRequires:  perl(Data::Dump::Streamer)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::Escape)

Requires:       perl(Data::Dump::Streamer)
Requires:       perl(JSON::XS)
Requires:       perl(PadWalker)
Requires:       perl(URI::Escape)

%{?perl_default_filter}
# need to figure out subpackage naming scheme in these cases
#{?perl_default_subpackage_tests}

%description
CouchDB::View provides a perlish way to define and serve views in CouchDB.

See the CouchDB::View::Document manpage for defining CouchDB views in Perl.
See the CouchDB::View::Server manpage for how to use Perl as a view server.

For more general information on how views and view servers work with CouchDB,
you may also want to see:

    http://incubator.apache.org/couchdb/
    http://wiki.apache.org/couchdb/

%prep
%setup -q -n CouchDB-View-%{version}

cat - > perl-view-server.ini <<EOINI
[Couch Query Servers]
# the canonical path suggested by CouchDB::View::Server...
text/perl=%{_bindir}/couchdb-view-server.pl
# ...and one that conforms more to the naming suggested
perl=%{_bindir}/couchdb-view-server.pl
EOINI

%build
%{?perl_ext_env_unset}
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

mkdir -p %{buildroot}%{_sysconfdir}/couchdb/default.d/
cp perl-view-server.ini %{buildroot}%{_sysconfdir}/couchdb/default.d/

%{_fixperms} %{buildroot}/*

%check
make test


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/*
%{_sysconfdir}/couchdb/default.d/*
%{_mandir}/man3/*.3*

%changelog
* Sat May 29 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.003-1
- specfile by Fedora::App::MaintainerTools 0.006


