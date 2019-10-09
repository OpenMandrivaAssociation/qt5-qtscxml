%define major 5
%define libname %mklibname qt5scxml %{major}
%define devname %mklibname qt5scxml -d
%define beta beta1

Name: qt5-qtscxml
Version:	5.14.0
%if "%{beta}" != "%{nil}"
%define qttarballdir qtscxml-everywhere-src-%{version}-%{beta}
Source0: http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
Release:	1
%else
%define qttarballdir qtscxml-everywhere-src-%{version}
Source0: http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
Release:	1
%endif
Summary: Qt scxml library
URL: https://github.com/qtproject/qtscxml
License: LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-with-Qt-Company-Qt-exception-1.1
Group: System/Libraries
BuildRequires: qmake5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: qt5-qtquick-private-devel
BuildRequires: qt5-qtdoc
BuildRequires: qt5-qttools
# For the Provides: generator
BuildRequires: cmake >= 3.11.0-1

%description
The Qt SCXML module provides functionality to create state machines from
SCXML files.

This includes both dynamically creating state machines (loading the SCXML
file and instantiating states and transitions) and generating a C++ file
that has a class implementing the state machine. It also contains
functionality to support data models and executable content.

%package -n %{libname}
Summary: Qt scxml library
Group: System/Libraries

%description -n %{libname}
Qt scxml library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package examples
Summary: Example code for the %{name} library
Group: Development/C
Requires: %{devname} = %{EVRD}
BuildRequires: pkgconfig(Qt5Widgets)

%description examples
Example code for the %{name} library.

%prep
%autosetup -n %{qttarballdir} -p1

# https://bugreports.qt.io/browse/QTBUG-76443
rm examples/*.pro

%qmake_qt5 *.pro

%build
%make_build
%make_build docs

%install
%make_install install_docs INSTALL_ROOT="%{buildroot}"

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/qt5/qml/QtScxml

%files -n %{devname}
%{_includedir}/*
%{_libdir}/qt5/bin/qscxmlc
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/Qt5Scxml
%{_libdir}/qt5/mkspecs/modules/*.pri
%{_libdir}/qt5/mkspecs/features/*.prf
%{_libdir}/*.prl
%doc %{_docdir}/qt5/qtscxml.qch
%doc %{_docdir}/qt5/qtscxml

#files examples
#%{_libdir}/qt5/examples/scxml
