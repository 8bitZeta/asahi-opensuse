Name:           uboot-asahi
Version:        2023.07.02
Release:        4
Summary:        U-Boot for Apple Silicon Macs
License:        GPLv3+
URL:            https://github.com/AsahiLinux
BuildArch:      aarch64
%define debug_package %{nil}
%define uboot_commit_id asahi-v%{version}-%{release}

# to download the sources
# spectool -g uboot-asahi.spec

Source0:        https://github.com/AsahiLinux/u-boot/archive/%{uboot_commit_id}.tar.gz

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  ImageMagick
BuildRequires:  make
BuildRequires:  libopenssl-devel


Provides: /usr/lib/asahi-boot/u-boot-nodtb.bin

%description
U-Boot for Apple Silicon Macs

%prep
%setup -b 0 -n u-boot-%{uboot_commit_id}
make %{_builddir}/u-boot-%{uboot_commit_id} apple_m1_defconfig

%build
%make_build HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE=""

%install
install -Dpm0644 -t %{buildroot}/usr/lib/asahi-boot %{_builddir}/u-boot-%{uboot_commit_id}/u-boot-nodtb.bin

%posttrans
update-m1n1

%files
/usr/lib/asahi-boot/u-boot-nodtb.bin

%changelog
