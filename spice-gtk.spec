#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x97D9123DE37A484F (toso@posteo.net)
#
Name     : spice-gtk
Version  : 0.41
Release  : 40
URL      : https://www.spice-space.org/download/gtk/spice-gtk-0.41.tar.xz
Source0  : https://www.spice-space.org/download/gtk/spice-gtk-0.41.tar.xz
Source1  : https://www.spice-space.org/download/gtk/spice-gtk-0.41.tar.xz.sig
Summary  : Lock-free, real-time flight recorder for C or C++ programs
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 GPL-3.0+ LGPL-2.0+ LGPL-2.1 LGPL-3.0
Requires: spice-gtk-bin = %{version}-%{release}
Requires: spice-gtk-data = %{version}-%{release}
Requires: spice-gtk-lib = %{version}-%{release}
Requires: spice-gtk-libexec = %{version}-%{release}
Requires: spice-gtk-license = %{version}-%{release}
Requires: spice-gtk-locales = %{version}-%{release}
Requires: spice-gtk-man = %{version}-%{release}
Requires: clr-hardware-files
BuildRequires : acl-dev
BuildRequires : asciidoc
BuildRequires : buildreq-meson
BuildRequires : buildreq-qmake
BuildRequires : clr-hardware-files
BuildRequires : gobject-introspection-dev
BuildRequires : gst-plugins-bad
BuildRequires : gst-plugins-base-dev
BuildRequires : gst-plugins-good
BuildRequires : gst-plugins-ugly
BuildRequires : gstreamer-dev
BuildRequires : gtk+-dev
BuildRequires : json-glib-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : lz4-dev
BuildRequires : openssl-dev
BuildRequires : opus-dev
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libcacard)
BuildRequires : pkgconfig(libcap-ng)
BuildRequires : pkgconfig(libsasl2)
BuildRequires : pkgconfig(libva-x11)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(spice-protocol)
BuildRequires : pkgconfig(vapigen)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : polkit-dev
BuildRequires : pypi(pyparsing)
BuildRequires : pypi(six)
BuildRequires : pypi-pyparsing
BuildRequires : python3
BuildRequires : usbredir-dev
BuildRequires : vala
Patch1: CVE-2017-12194.nopatch
Patch2: build.patch

%description
Flight recorder for C and C++ programs using printf-like 'record' statements.

%package bin
Summary: bin components for the spice-gtk package.
Group: Binaries
Requires: spice-gtk-data = %{version}-%{release}
Requires: spice-gtk-libexec = %{version}-%{release}
Requires: spice-gtk-license = %{version}-%{release}

%description bin
bin components for the spice-gtk package.


%package data
Summary: data components for the spice-gtk package.
Group: Data

%description data
data components for the spice-gtk package.


%package dev
Summary: dev components for the spice-gtk package.
Group: Development
Requires: spice-gtk-lib = %{version}-%{release}
Requires: spice-gtk-bin = %{version}-%{release}
Requires: spice-gtk-data = %{version}-%{release}
Provides: spice-gtk-devel = %{version}-%{release}
Requires: spice-gtk = %{version}-%{release}

%description dev
dev components for the spice-gtk package.


%package lib
Summary: lib components for the spice-gtk package.
Group: Libraries
Requires: spice-gtk-data = %{version}-%{release}
Requires: spice-gtk-libexec = %{version}-%{release}
Requires: spice-gtk-license = %{version}-%{release}

%description lib
lib components for the spice-gtk package.


%package libexec
Summary: libexec components for the spice-gtk package.
Group: Default
Requires: spice-gtk-license = %{version}-%{release}

%description libexec
libexec components for the spice-gtk package.


%package license
Summary: license components for the spice-gtk package.
Group: Default

%description license
license components for the spice-gtk package.


%package locales
Summary: locales components for the spice-gtk package.
Group: Default

%description locales
locales components for the spice-gtk package.


%package man
Summary: man components for the spice-gtk package.
Group: Default

%description man
man components for the spice-gtk package.


%prep
%setup -q -n spice-gtk-0.41
cd %{_builddir}/spice-gtk-0.41
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664906900
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dgtk=enabled \
-Dusbredir=enabled \
-Dvapi=enabled \
-Dusb-ids-path=/usr/share/hwdata/usb.ids \
-Dgtk_doc=disabled  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/spice-gtk
cp %{_builddir}/spice-gtk-%{version}/COPYING %{buildroot}/usr/share/package-licenses/spice-gtk/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/spice-gtk-%{version}/subprojects/keycodemapdb/LICENSE.BSD %{buildroot}/usr/share/package-licenses/spice-gtk/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8 || :
cp %{_builddir}/spice-gtk-%{version}/subprojects/keycodemapdb/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/spice-gtk/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/spice-gtk-%{version}/subprojects/spice-common/COPYING %{buildroot}/usr/share/package-licenses/spice-gtk/3704f4680301a60004b20f94e0b5b8c7ff1484a9 || :
cp %{_builddir}/spice-gtk-%{version}/subprojects/spice-common/common/recorder/COPYING %{buildroot}/usr/share/package-licenses/spice-gtk/a8a12e6867d7ee39c21d9b11a984066099b6fb6b || :
cp %{_builddir}/spice-gtk-%{version}/subprojects/spice-common/common/recorder/scope/COPYING %{buildroot}/usr/share/package-licenses/spice-gtk/12d81f50767d4e09aa7877da077ad9d1b915d75b || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang spice-gtk

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/spicy
/usr/bin/spicy-screenshot
/usr/bin/spicy-stats

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/SpiceClientGLib-2.0.typelib
/usr/lib64/girepository-1.0/SpiceClientGtk-3.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/polkit-1/actions/org.spice-space.lowlevelusbaccess.policy
/usr/share/vala/vapi/spice-client-glib-2.0.deps
/usr/share/vala/vapi/spice-client-glib-2.0.vapi
/usr/share/vala/vapi/spice-client-gtk-3.0.deps
/usr/share/vala/vapi/spice-client-gtk-3.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/spice-client-glib-2.0/channel-cursor.h
/usr/include/spice-client-glib-2.0/channel-display.h
/usr/include/spice-client-glib-2.0/channel-inputs.h
/usr/include/spice-client-glib-2.0/channel-main.h
/usr/include/spice-client-glib-2.0/channel-playback.h
/usr/include/spice-client-glib-2.0/channel-port.h
/usr/include/spice-client-glib-2.0/channel-record.h
/usr/include/spice-client-glib-2.0/channel-smartcard.h
/usr/include/spice-client-glib-2.0/channel-usbredir.h
/usr/include/spice-client-glib-2.0/channel-webdav.h
/usr/include/spice-client-glib-2.0/qmp-port.h
/usr/include/spice-client-glib-2.0/smartcard-manager.h
/usr/include/spice-client-glib-2.0/spice-audio.h
/usr/include/spice-client-glib-2.0/spice-channel.h
/usr/include/spice-client-glib-2.0/spice-client.h
/usr/include/spice-client-glib-2.0/spice-file-transfer-task.h
/usr/include/spice-client-glib-2.0/spice-glib-enums.h
/usr/include/spice-client-glib-2.0/spice-option.h
/usr/include/spice-client-glib-2.0/spice-session.h
/usr/include/spice-client-glib-2.0/spice-types.h
/usr/include/spice-client-glib-2.0/spice-uri.h
/usr/include/spice-client-glib-2.0/spice-util.h
/usr/include/spice-client-glib-2.0/spice-version.h
/usr/include/spice-client-glib-2.0/usb-device-manager.h
/usr/include/spice-client-gtk-3.0/spice-client-gtk.h
/usr/include/spice-client-gtk-3.0/spice-grabsequence.h
/usr/include/spice-client-gtk-3.0/spice-gtk-session.h
/usr/include/spice-client-gtk-3.0/spice-widget-enums.h
/usr/include/spice-client-gtk-3.0/spice-widget.h
/usr/include/spice-client-gtk-3.0/usb-device-widget.h
/usr/lib64/libspice-client-glib-2.0.so
/usr/lib64/libspice-client-gtk-3.0.so
/usr/lib64/pkgconfig/spice-client-glib-2.0.pc
/usr/lib64/pkgconfig/spice-client-gtk-3.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libspice-client-glib-2.0.so.8
/usr/lib64/libspice-client-glib-2.0.so.8.8.1
/usr/lib64/libspice-client-gtk-3.0.so.5
/usr/lib64/libspice-client-gtk-3.0.so.5.1.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/spice-client-glib-usb-acl-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/spice-gtk/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/spice-gtk/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/spice-gtk/12d81f50767d4e09aa7877da077ad9d1b915d75b
/usr/share/package-licenses/spice-gtk/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/spice-gtk/a8a12e6867d7ee39c21d9b11a984066099b6fb6b
/usr/share/package-licenses/spice-gtk/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/spice-client.1

%files locales -f spice-gtk.lang
%defattr(-,root,root,-)

