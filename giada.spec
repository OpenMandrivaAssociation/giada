Name:		giada
Version:	0.16.0
Release:	1
Summary:	Sampler Audio Tool
License:	GPLv3+
Group:		Sound/Utilities
URL:		https://giadamusic.com
Source0:	https://github.com/monocasual/giada/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	giada.svg
Source2:	giada.desktop

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(jansson) >= 2.7
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-simple)
BuildRequires:	pkgconfig(portaudio-2.0)
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
%setup -q

%build
./autogen.sh
%configure --target=linux
%make_build

%install
%make_install

install -Dm 0644 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
install -Dm 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 0644 %{SOURCE3} %{buildroot}%{_mandir}/man1/%{name}.1
install -Dm 0644 %{SOURCE4} %{buildroot}%{_mandir}/fr/man1/%{name}.1

%files
%doc ChangeLog README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
