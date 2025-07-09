#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kio-admin
Version: 25.04.0
Release: %{?git:%{?git:0.%{git}.}0.%{git}.}1
%if 0%{?git:1}
%if 0%{?git:1}
Source0:	https://invent.kde.org/system/kio-admin/-/archive/%{gitbranch}/kio-admin-%{gitbranchd}.tar.bz2#/kio-admin-%{git}.tar.bz2
%else
Source0: https://invent.kde.org/system/kio-admin/-/archive/master/kio-admin-master.tar.bz2
%endif
%else
%if 0%{?git:1}
Source0:	https://invent.kde.org/system/kio-admin/-/archive/%{gitbranch}/kio-admin-%{gitbranchd}.tar.bz2#/kio-admin-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/kio-admin-%{version}.tar.xz
%endif
%endif
Summary: Manage files as administrator using the admin:// KIO protocol.
URL: https://invent.kde.org/system/kio-admin
License: GPL
Group: System/Libraries
BuildRequires: cmake ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: pkgconfig(polkit-qt6-core-1)
BuildRequires: atomic-devel

%description
Manage files as administrator using the admin:// KIO protocol.

%prep
%autosetup -p1 -n kio-admin-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kio5_admin

%files -f kio5_admin.lang
%{_libdir}/libexec/kf6/kio-admin-helper
%{_datadir}/dbus-1/system-services/org.kde.kio.admin.service
%{_datadir}/dbus-1/system.d/org.kde.kio.admin.conf
%{_datadir}/metainfo/org.kde.kio.admin.metainfo.xml
%{_datadir}/polkit-1/actions/org.kde.kio.admin.policy
%{_qtdir}/plugins/kf6/kfileitemaction/kio-admin.so
%{_qtdir}/plugins/kf6/kio/admin.so
