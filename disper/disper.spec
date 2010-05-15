Name:           disper
Version:        0.2.3
Release:        1%{?dist}
Summary:        On-the-fly display switch utility

Group:          Applications/System
License:        GPLv3+
URL:            http://willem.engen.nl/projects/disper/
Source0:        http://ppa.launchpad.net/wvengen/ppa/ubuntu/pool/main/d/disper/%{name}_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  gzip
Requires:       /usr/bin/nvidia-settings

%description
Disper is an on-the-fly display switch utility. It is intended to be used just
before giving a presentation with a laptop, when all one wants is that the
beamer, which has just been connected, is able to show whatever you prepared.

Disper gives you the option to either clone the all detected displays, or
extend the desktop to them. Resolutions are automatically detected. For
cloning, the highest resolution supported by all displays devices is chosen;
for extending every display device gets its heighest supported resolution.
For special setups requiring more detailed control, one can still use the
standard display configuration utilities.

At the moment nVidia cards are supported, and a basic XRandR backend is in
place.


%prep
%setup -q -n trunk


%build
# nothing to build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
chmod +x $RPM_BUILD_ROOT%{_datadir}/%{name}/src/xrandr/core.py
chmod +x $RPM_BUILD_ROOT%{_datadir}/%{name}/src/xrandr/gdk.py
chmod +x $RPM_BUILD_ROOT%{_datadir}/%{name}/src/xrandr/__init__.py
gzip %{name}.1
install -Dpm 0644 %{name}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1.gz



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Tue Jul 07 2009 Felix Kaechele <heffer@fedoraproject.org> - 0.2.3-1
- initial build

