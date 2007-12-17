%define	snap 20071026

%define	major 2
%define	libname %mklibname %{name} %major
%define	develname %mklibname %{name} -d

Summary:	Templating engine writen in C++
Name:		teng
Version:	2.0.1
Release:	%mkrel 0.%{snap}.1
License:	LGPL
Group:		System/Libraries
URL:		http://teng.sourceforge.net/
Source0:	teng.tar.gz
BuildRequires:	libtool
BuildRequires:	flex
BuildRequires:	bison

%description
Teng is a general purpose templating engine writen in C++ (i.e. library). It is
also available as Python module or PHP extension. The main idea of teng is to
strictly separate application logic from presentation layer. Widely used on
dynamic web sites.

%package -n	%{libname}
Summary:	The shared Teng libraries
Group:		System/Libraries

%description -n	%{libname}
Teng is a general purpose templating engine writen in C++ (i.e. library). It is
also available as Python module or PHP extension. The main idea of teng is to
strictly separate application logic from presentation layer. Widely used on
dynamic web sites.

This package contains the shared Teng libraries.

%package -n	%{develname}
Summary:	Development files from Teng
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Conflicts:	%{mklibname teng 1 -d}

%description -n	%{develname}
Development files from Teng.

%prep

%setup -q -n %{name}

%build
sh ./bootstrap.sh

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files	-n %{libname}
%defattr(0644,root,root,0755)
%doc COPYING README INSTALL AUTHORS
%{_libdir}/lib%{name}.so.*

%files	-n %{develname}
%defattr(0644,root,root,0755)
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.la
