# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate bzip2

Name:           rust-bzip2
Version:        0.5.2
Release:        %autorelease
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bzip2
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Bindings to libbzip2 for bzip2 compression and decompression exposed as
Reader/Writer streams.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/SECURITY.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+libbz2-rs-sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libbz2-rs-sys-devel %{_description}

This package contains library source intended for building other packages which
use the "libbz2-rs-sys" feature of the "%{crate}" crate.

%files       -n %{name}+libbz2-rs-sys-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-devel %{_description}

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%files       -n %{name}+static-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
