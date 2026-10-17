# upstream does not support building with gcc
%global toolchain clang

Name:           redumper
Version:        b766
Release:        %autorelease
Summary:        Low level CD dumper utility

License:        GPL-3.0-only
URL:            https://github.com/superg/redumper
Source0:        https://github.com/superg/redumper/archive/%{version}/redumper-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  cmake(GTest)

%description
redumper is a cross-platform command-line tool for creating accurate optical
disc dumps. It provides a low-level, byte-perfect workflow for CDs, including
incremental refinement, SCSI/C2 error recovery, raw subchannel preservation,
and automatic audio-offset detection. It also supports dumping of DVD, HD DVD,
and Blu-ray media.

%prep
%autosetup -p1

%build
%cmake -DREDUMPER_VERSION_BUILD=%{version} -DREDUMPER_LINKER_FLAGS=
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
