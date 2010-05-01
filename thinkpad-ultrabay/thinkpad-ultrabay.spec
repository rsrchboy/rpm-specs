Name:           thinkpad-ultrabay
Version:        1
Release:        0.1%{?dist}
Summary:        Ultrabay hotswap enablement

Group:          System/Environment
License:        GPLv2+
URL:            http://thinkwiki.org/wiki/How_to_hotswap_UltraBay_devices
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Source0:        events.ultrabay-eject
Source1:        events.ultrabay-insert
Source10:       ultrabay_eject
Source11:       ultrabay_insert
Source20:       ibm-ultrabay.rules
Source21:       10-ultrabay.fdi

#BuildRequires:  
#Requires:       

%description
Provide the acpi, udev, and hal configurations needed to enable ultrabay
hotswap. :)

%prep
#setup -q
# NO-OP

%build
# NO-OP


%install
rm -rf %{buildroot}

# acpi events
mkdir -p %{buildroot}/etc/acpi/events
install -m 0644 %{SOURCE0} %{SOURCE1} %{buildroot}/etc/acpi/events/

# supporting scripties...
mkdir -p %{buildroot}%{_sbindir}
install -m 0755 %{SOURCE10} %{SOURCE11} %{buildroot}%{_sbindir}

# udev rules, hal
mkdir -p %{buildroot}/etc/udev/rules.d %{buildroot}/etc/hal/fdi/information
install -m 0644 %{SOURCE20} %{buildroot}/etc/udev/rules.d/ibm-ultrabay.rules
install -m 0644 %{SOURCE21} \
    %{buildroot}/etc/hal/fdi/information/10-ultrabay.fdi



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
#doc
/etc/udev/rules.d/ibm-ultrabay.rules
/etc/hal/fdi/information/10-ultrabay.fdi
/etc/acpi/events/*
%{_sbindir}/*



%changelog
* Sat Jan 19 2008 Chris Weyl <cweyl@alumni.drew.edu> 1-1
- initial rpm creation

