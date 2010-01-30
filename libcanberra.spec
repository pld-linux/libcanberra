Summary:	libcanberra - the portable sound event library
Summary(pl.UTF-8):	libcanberra - przenośna biblioteka zdarzeń dźwiękowych
Name:		libcanberra
Version:	0.22
Release:	4
License:	LGPL v2+
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/libcanberra/%{name}-%{version}.tar.gz
# Source0-md5:	e24e2f956fedfbcc58edfa40471b18d8
URL:		http://0pointer.de/lennart/projects/libcanberra/
BuildRequires:	GConf2-devel
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	gstreamer-devel >= 0.10.15
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 2:2.2.0
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.11-1
Requires:	pulseaudio-libs >= 0.9.11-1
Requires:	sound-theme-freedesktop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		backenddir	%{_libdir}/libcanberra-%{version}

%description
A small and lightweight implementation of the XDG Sound Theme
Specification (http://0pointer.de/public/sound-theme-spec.html).

%description -l pl.UTF-8
Mała i lekka implementacja specyfikacji XDG Sound Theme
(http://0pointer.de/public/sound-theme-spec.html).

%package devel
Summary:	Header files for libcanberra library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcanberra
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcanberra library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcanberra.

%package static
Summary:	Static libcanberra library
Summary(pl.UTF-8):	Statyczna biblioteka libcanberra
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcanberra library.

%description static -l pl.UTF-8
Statyczna biblioteka libcanberra.

%package gtk
Summary:	GTK+ bindings for libcanberra library
Summary(pl.UTF-8):	Wiązania GTK+ do biblioteki libcanberra
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	libcanberra-gtk2
Obsoletes:	libcanberra-gtk2

%description gtk
GTK+ bindings for libcanberra library.

%description gtk -l pl.UTF-8
Wiązania GTK+ do biblioteki libcanberra.

%package gtk-devel
Summary:	Header files for libcanberra-gtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcanberra-gtk
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.14.0

%description gtk-devel
Header files for libcanberra-gtk library.

%description gtk-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcanberra-gtk.

%package gtk-static
Summary:	Static libcanberra-gtk library
Summary(pl.UTF-8):	Statyczna biblioteka libcanberra-gtk
Group:		X11/Development/Libraries
Requires:	%{name}-gtk-devel = %{version}-%{release}

%description gtk-static
Static libcanberra-gtk library.

%description gtk-static -l pl.UTF-8
Statyczna biblioteka libcanberra-gtk.

%package apidocs
Summary:	libcanberra API documentation
Summary(pl.UTF-8):	Dokumentacja API libcanberra
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libcanberra API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libcanberra.

%package gnome
Summary:	Files required to play login sound in GNOME
Summary(pl.UTF-8):	Pliki potrzebne do odtwarzania dźwięku logowania w GNOME
Group:		Applications
Requires(post,preun):	GConf2
Requires:	%{name}-gtk = %{version}-%{release}

%description gnome
Files required to play login sound in GNOME.

%description gnome -l pl.UTF-8
Pliki potrzebne do odtwarzania dźwięku logowania w GNOME.

%prep
%setup -q

%build
%{__gtkdocize} --docdir gtkdoc/
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--enable-alsa \
	--enable-gstreamer \
	--enable-null \
	--enable-oss \
	--enable-pulse \
	--enable-static \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.{a,la}
rm $RPM_BUILD_ROOT%{backenddir}/*.{a,la}
rm $RPM_BUILD_ROOT%{_datadir}/doc/libcanberra/README

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%post gnome
%gconf_schema_install libcanberra.schemas

%preun gnome
%gconf_schema_uninstall libcanberra.schemas

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libcanberra.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcanberra.so.0
%dir %{backenddir}
%attr(755,root,root) %{backenddir}/libcanberra-alsa.so
%attr(755,root,root) %{backenddir}/libcanberra-gstreamer.so
%attr(755,root,root) %{backenddir}/libcanberra-oss.so
%attr(755,root,root) %{backenddir}/libcanberra-pulse.so
%attr(755,root,root) %{backenddir}/libcanberra-null.so
%attr(755,root,root) %{backenddir}/libcanberra-multi.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcanberra.so
%{_libdir}/libcanberra.la
%{_includedir}/canberra.h
%{_pkgconfigdir}/libcanberra.pc
%{_datadir}/vala/vapi/libcanberra.vapi

%files static
%defattr(644,root,root,755)
%{_libdir}/libcanberra.a

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/canberra-gtk-play
%attr(755,root,root) %{_libdir}/libcanberra-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcanberra-gtk.so.0
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libcanberra-gtk-module.so

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcanberra-gtk.so
%{_libdir}/libcanberra-gtk.la
%{_includedir}/canberra-gtk.h
%{_pkgconfigdir}/libcanberra-gtk.pc
%{_datadir}/vala/vapi/libcanberra-gtk.vapi

%files gtk-static
%defattr(644,root,root,755)
%{_libdir}/libcanberra-gtk.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files gnome
%defattr(644,root,root,755)
%{_sysconfdir}/gconf/schemas/libcanberra.schemas
%{_datadir}/gdm/autostart/LoginWindow/libcanberra-ready-sound.desktop
%{_datadir}/gnome/autostart/libcanberra-login-sound.desktop
%attr(755,root,root) %{_datadir}/gnome/shutdown/libcanberra-logout-sound.sh
