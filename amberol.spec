%define debug_package %{nil}
%global _lto_cflags %nil
%global numjobs 10
%global use_all_cpus 0

%if %{use_all_cpus}
%global numjobs %{_smp_build_ncpus}
%endif

Name:           amberol
Version:        2025.1
Release:        0
Summary:        Simple and modern GNOME music player

License:        GPL-3.0
URL:            https://gitlab.gnome.org/World/amberol.git
Source0:        https://gitlab.gnome.org/World/amberol/-/archive/%{version}/amberol-%{version}.tar.gz

BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

BuildRequires:  cargo-rpm-macros
BuildRequires:  meson
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:	cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:	reuse
BuildRequires:  dbus-devel
BuildRequires:  pkgconf-pkg-config

Requires:       libadwaita
Requires:       gtk4
Requires:       hicolor-icon-theme


BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  git

Requires:       gstreamer1
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad-free

# ASS subtitles (assrender)
Recommends:     gstreamer1-plugins-bad-free-extras

# CD Playback
Suggests:       gstreamer1-plugins-ugly-free



%description
A GNOME music player

%prep
%autosetup -p1 -n amberol-%{version}

%build
%meson --buildtype release
%meson_build

%install
%meson_install

%files
%{_bindir}/amberol
%{_datadir}/amberol/amberol.gresource
%{_datadir}/applications/io.bassi.Amberol.desktop
%{_datadir}/dbus-1/services/io.bassi.Amberol.service
%{_datadir}/glib-2.0/schemas/io.bassi.Amberol.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/io.bassi.Amberol.svg
%{_datadir}/icons/hicolor/symbolic/apps/io.bassi.Amberol-symbolic.svg
%{_datadir}/locale/*/LC_MESSAGES/amberol.mo
%{_datadir}/metainfo/io.bassi.Amberol.metainfo.xml


%changelog
* Sun Apr 13 2025 Trung Lê <8@tle.id.au> - 2025.1-0
- New release

* Fri Feb 28 2025 Trung Lê <8@tle.id.au> - 2024.2-0
- New release

* Tue Jun 18 2024 Trung Lê <8@tle.id.au> - 0.10.3-2
- Initial build
