
Name:           abootimg
Version:        0.6
Release:        1
Summary:        Android boot image manipulator
License:        GPL-2.0+ and Apache-2.0
Group:          System/Boot
Url:            http://gitorious.org/ac100/abootimg
Source:         %{name}.tar.bz2
BuildRequires:  pkgconfig(blkid)

%description
Android boot image manipulator. It can create/update/unpack boot.img - boot
file used by Android OS.

%prep
%setup -q -n %{name}

%build
# First make clean as a binary already exists in the tarball
make clean -C aboot
make %{?_smp_mflags} -C aboot

%install
install -m 755 -d %{buildroot}/%{_bindir}
install -m 755 aboot/abootimg %{buildroot}/%{_bindir}
install -m 755 aboot/abootimg-unpack-initrd %{buildroot}/%{_bindir}
install -m 755 aboot/abootimg-pack-initrd %{buildroot}/%{_bindir}

%files
%defattr(-,root,root)
%{_bindir}/*
