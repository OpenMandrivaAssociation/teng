%define	name	teng
%define	version	1.0.10
%define	release %mkrel 2

%define	major	1
%define	libname	%mklibname %name %major

%define	Summary	Templating engine writen in C++

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
License:	LGPL
Group:		Development/C++
URL:		http://teng.sourceforge.net/
Source0:	%name-%version.tar.bz2
Patch0:		teng-gcc4_fix.patch
BuildRoot:	%_tmppath/%name-buildroot

%description
Teng is a general purpose templating engine writen in C++ (i.e. library). It is
also available as Python module or PHP extension. The main idea of teng is to
strictly separate application logic from presentation layer. Widely used on
dynamic web sites.

%package	-n %libname
Summary:	Teng libraries
Group:		Development/C++

%description	-n %libname
Teng libraries

%package	-n %libname-devel
Summary:	Development files from Teng
Group:		Development/C++
Provides:	lib%name-devel
Requires:	%libname = %version

%description	-n %libname-devel
Development files from Teng.

%prep
%setup -q

# patch is already in cvs, in next release this should be removed
%patch0 -p0 -b .gcc4_fix

%build
%configure
%make

%install
rm -rf %buildroot
%makeinstall

%clean
rm -rf %buildroot

%post -n %libname -p /sbin/ldconfig -n %{libname}

%postun -n %libname -p /sbin/ldconfig -n %{libname}

%files	-n %libname
%defattr(0644,root,root,0755)
%doc COPYING README INSTALL AUTHORS
%{_libdir}/lib%name.so.*

%files	-n %libname-devel
%defattr(0644,root,root,0755)
%{_includedir}/*
%{_libdir}/lib%name.so
%{_libdir}/lib%name.a
%{_libdir}/lib%name.la

