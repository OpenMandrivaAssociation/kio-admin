%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kio-admin
Version: 23.08.4
Release: %{?git:0.%{git}.}4
%if 0%{?git:1}
Source0: https://invent.kde.org/system/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
Summary: Manage files as administrator using the admin:// KIO protocol.
URL: https://invent.kde.org/system/%{name}
License: GPL
Group: System/Libraries
BuildRequires: cmake ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: pkgconfig(polkit-qt5-core-1)

%description
Manage files as administrator using the admin:// KIO protocol.

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kio5_admin

%files -f kio5_admin.lang
%{_libdir}/libexec/kf5/kio-admin-helper
%{_datadir}/dbus-1/system-services/org.kde.kio.admin.service
%{_datadir}/dbus-1/system.d/org.kde.kio.admin.conf
%{_datadir}/metainfo/org.kde.kio.admin.metainfo.xml
%{_datadir}/polkit-1/actions/org.kde.kio.admin.policy
%{_libdir}/qt5/plugins/kf5/kfileitemaction/kio-admin.so
%{_libdir}/qt5/plugins/kf5/kio/admin.so
