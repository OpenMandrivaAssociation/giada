Summary:	Music production tool
Name:	giada
Version:	1.5.0
Release:	1
License:	GPLv3+
Group:	Sound/Utilities
Url:		https://giadamusic.com
# Submodules are a pain...
#Source0:	%%{name}-%%{version}.tar.xz
Source0:	https://github.com/monocasual/giada/archive/v%{version}/%{name}-%{version}-src.tar.gz
Patch0:	giada-1.4.0-cmake-exclude-juce-and-fltk-from-all.patch
Patch1:	giada-1.4.0-fmt.patch
BuildRequires:	cmake >= 3.29
BuildRequires:	doxygen
BuildRequires:	make
BuildRequires:	texlive-latex.bin
BuildRequires:	fltk-devel
BuildRequires:	fltk-fluid
BuildRequires:lib64stdc++-static-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(fmt)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libdecor-0)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-simple)
BuildRequires:	pkgconfig(nlohmann_json)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(pangoxft)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(rtaudio)
BuildRequires:	pkgconfig(rtmidi)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(vorbisenc)
BuildRequires:	pkgconfig(vst3sdk)
BuildRequires:	pkgconfig(wayland-client) >= 1.18
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(wayland-protocols) >= 1.15
BuildRequires:	pkgconfig(webkit2gtk-4.1)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(zlib)

%description
Giada is an audio tool for DJs and live performers.
The program is:
* a loop machine: build songs in real time by layering audio tracks or MIDI
	events;
* a sample player: load samples and play them with a computer keyboard or a
	MIDI controller;
* a song editor: write songs from scratch or edit existing live recordings;
* a live recorder: record sounds and MIDI events coming from external devices
	or other apps;
* an FX processor:  process samples or audio/MIDI input with VST instruments;
* a MIDI controller: control other software or synchronize physical MIDI
	devices by using Giada as a MIDI master sequencer.

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_datadir}/applications/com.giadamusic.Giada.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.giadamusic.Giada.svg
%{_datadir}/metainfo/com.giadamusic.Giada.metainfo.xml

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}
# 1.5.0 tarball has an empty fltk submodule; ABF has no network for FetchContent.
# Use the system FLTK we already BuildRequire.
python - <<'PY'
from pathlib import Path
import re
p = Path("CMakeLists.txt")
t = p.read_text()
t2, n = re.subn(
    r"include \(FetchContent\)\s*FetchContent_Declare\(\s*FLTK.*?FetchContent_MakeAvailable\(FLTK\)",
    "find_package(FLTK REQUIRED)",
    t,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit(f"FLTK FetchContent block not found (n={n})")
p.write_text(t2)
PY


%build
# If not set, OBJCXX is set to g++ unconditionally (and used to link).
# Since g++ doesn't like clang++ LTO, make sure OBJCXX is set to the
# system compiler.
export OBJCXX=%{__cxx}
%cmake -DWITH_TESTS=OFF -DWITH_VST=OFF -DWITH_VST3=ON -DCMAKE_CXX_FLAGS="-std=c++17 "
%make_build -j1


%install
%make_install -C build
