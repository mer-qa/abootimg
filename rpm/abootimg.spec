
Name:           abootimg
Version:        0.6
Release:        1
Summary:        Android boot image manipulator
License:        GPL-2.0+ and Apache-2.0
Group:          System/Boot
Url:            http://gitorious.org/ac100/abootimg
Source:         %{name}-%{version}.tar.gz 
BuildRequires:  pkgconfig(blkid)

%description
Android boot image manipulator. It can create/update/unpack boot.img - boot
file used by Android OS.

%prep
%setup -q

%build
make %{?_smp_mflags} -C abootimg

%install
install -m 755 -d %{buildroot}/%{_bindir}
install -m 755 abootimg/abootimg %{buildroot}/%{_bindir}
install -m 755 abootimg/abootimg-unpack-initrd %{buildroot}/%{_bindir}
install -m 755 abootimg/abootimg-pack-initrd %{buildroot}/%{_bindir}

%files
%doc abootimg/LICENSE abootimg/Changelog abootimg/README
%defattr(-,root,root)
%{_bindir}/*
