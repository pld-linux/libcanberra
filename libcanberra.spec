Summary:	libcanberra - the portable sound event library
Name:		libcanberra
Version:	0.5
Release:	1
Group:		Libraries
Source0:	http://0pointer.de/public/%{name}-%{version}.tar.gz
# Source0-md5:	1d8abd71613764650a0e2359584d7cdb
License:	LGPLv2+
URL:		http://git.0pointer.de/?p=libcanberra.git;a=summary
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	pulseaudio-devel >= 0.9.11-1
Requires:	pulseaudio-libs >= 0.9.11-1
Requires:	sound-theme-freedesktop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small and lightweight implementation of the XDG Sound Theme
Specification (http://0pointer.de/public/sound-theme-spec.html).

%package gtk2
Summary:	Gtk+ Bindings for libcanberra
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk2
Gtk+ bindings for libcanberra

%package devel
Summary:	Development Files for libcanberra Client Development
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk-doc
Requires:	gtk2-devel
Requires:	pkgconfig

%description devel
Development Files for libcanberra Client Development

%package apidocs
Summary:	libcanberra API documentation
Summary(pl.UTF-8):	Dokumentacja API libcanberra
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libcanberra API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libcanberra.

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post gtk2 -p /sbin/ldconfig
%postun gtk2 -p /sbin/ldconfig

%prep
%setup -q

%build
%{__libtoolize}
%{__autoheader}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--disable-rpath \
	--enable-pulse \
	--enable-alsa \
	--enable-null \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.la
rm $RPM_BUILD_ROOT%{_libdir}/libcanberra/libcanberra-multi.so
rm $RPM_BUILD_ROOT%{_libdir}/libcanberra/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LGPL
%attr(755,root,root) %{_libdir}/libcanberra.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcanberra.so.0
%dir %{_libdir}/libcanberra
%{_libdir}/libcanberra/libcanberra-alsa.so
%{_libdir}/libcanberra/libcanberra-pulse.so
%{_libdir}/libcanberra/libcanberra-null.so

%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcanberra-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcanberra-gtk.so.0
%{_libdir}/gtk-2.0/modules/libcanberra-gtk-module.so
%attr(755,root,root) %{_bindir}/canberra-gtk-play
%{_datadir}/gnome/autostart/libcanberra-login-sound.desktop
%{_datadir}/gnome/shutdown/libcanberra-logout-sound.sh

%files devel
%defattr(644,root,root,755)
%{_includedir}/canberra-gtk.h
%{_includedir}/canberra.h
%attr(755,root,root) %{_libdir}/libcanberra-gtk.so
%attr(755,root,root) %{_libdir}/libcanberra.so
%{_libdir}/libcanberra-gtk.la
%{_libdir}/libcanberra.la
%{_pkgconfigdir}/libcanberra-gtk.pc
%{_pkgconfigdir}/libcanberra.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
