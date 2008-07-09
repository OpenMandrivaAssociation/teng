%define	snap 20080222

%define	major 2
%define	libname %mklibname %{name} %major
%define	develname %mklibname %{name} -d

Summary:	Templating engine writen in C++
Name:		teng
Version:	2.0.4
Release:	%mkrel 0.%{snap}.1
License:	LGPL
Group:		System/Libraries
URL:		http://teng.sourceforge.net/
Source0:	teng.tar.gz
Patch0:		teng-gcc43.diff
BuildRequires:	libtool
BuildRequires:	flex
BuildRequires:	bison
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%setup -q -n %{name}
%patch0 -p1

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%build
sh ./bootstrap.sh

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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
