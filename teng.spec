%define	major 2
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Summary:	Templating engine writen in C++
Name:		teng
Version:	2.1.1
Release:	1
License:	LGPL
Group:		System/Libraries
URL:		http://teng.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/teng/teng-%{version}.tar.gz
BuildRequires:	autoconf automake libtool
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
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname teng 1 -d}

%description -n	%{develname}
Development files from Teng.

%prep

%setup -q

%build
#autoreconf -fi

%configure2_5x

%make

%install

%makeinstall
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc COPYING README INSTALL AUTHORS
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
