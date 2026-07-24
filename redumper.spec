# upstream does not support building with gcc
%global toolchain clang

Name:           redumper
Version:        b735
Release:        %autorelease
Summary:        Low level CD dumper utility

License:        GPL-3.0-only
URL:            https://github.com/superg/redumper
Source0:        https://github.com/superg/redumper/archive/%{version}/redumper-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  cmake(GTest)

%description
redumper is a low-level byte-perfect CD disc dumper. It supports incremental
dumps, advanced SCSI/C2 repair, intelligent audio CD offset detection and a lot
of other features.

redumper is also a general purpose DVD/HD-DVD/Blu-ray disc dumper.

%prep
%autosetup -p1

%build
%cmake -DREDUMPER_VERSION_BUILD=%{version}%{?dist} -DREDUMPER_LINKER_FLAGS=
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/redumper

%changelog
%autochangelog
