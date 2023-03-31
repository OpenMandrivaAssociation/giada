Name:		giada
Version:	0.23.0
Release:	2
Summary:	Sampler Audio Tool
License:	GPLv3+
Group:		Sound/Utilities
URL:		https://giadamusic.com
Source0:	https://github.com/monocasual/giada/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	giada.desktop
#Patch0:   giada-findFLTK.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:  fltk-fluid
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(jansson) >= 2.7
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-simple)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(rtaudio)
BuildRequires:	pkgconfig(rtmidi)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xpm)

%description
Giada is an audio tool for DJs and live performers. Up to 32 samples
may be loaded or recorded, and may be played in single mode (drum
machine) or loop mode (sequencer). The keyboard can be used to
control this.

%prep
%autosetup -p1

%build
# If not set, OBJCXX is set to g++ unconditionally (and used to link).
# Since g++ doesn't like clang++ LTO, make sure OBJCXX is set to the
# system compiler.
export OBJCXX=%{__cxx}
%cmake 
%make_build

%install
%make_install -C build

install -Dm 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -p -D -m644 extras/giada-logo.png %{buildroot}%{_datadir}/icons/hicolor/150x150/apps/%{name}-logo.png

%files
%doc ChangeLog README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/150x150/apps/%{name}-logo.png
