Name:       libfontenc
Version:    1.1.8
Release:    1%{?dist}
Summary:    X font encoding library
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/lib/%{name}
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(fontutil) >= 1.1
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(zlib)

%description
X font encoding library.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%license COPYING
%{_includedir}/X11/fonts/fontenc.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/fontenc.pc
