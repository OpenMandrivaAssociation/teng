%define	major 2
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Summary:	Templating engine writen in C++
Name:		teng
Version:	2.1.1
Release:	2
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


%changelog
* Sun May 06 2012 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-1
+ Revision: 796984
- 2.1.1

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 2.0.4-0.20080222.2mdv2010.0
+ Revision: 434333
- rebuild

* Wed Jul 09 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.4-0.20080222.1mdv2009.0
+ Revision: 233017
- 2.0.4 (cvs snap 20080222)
- fix build with gcc43 (P0)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Feb 05 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-0.20071219.1mdv2008.1
+ Revision: 162779
- new snap (20071219)
- fix deps

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 13 2007 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-0.20071026.1mdv2008.1
+ Revision: 108440
- 2.0.1 (a recent 20071026 cvs snap)
- new major (2)
- new devel naming


* Wed Jun 15 2005 Tibor Pittich <Tibor.Pittich@mandriva.org> 1.0.10-2mdk
- err, fixed requires

* Wed Jun 15 2005 Tibor Pittich <Tibor.Pittich@mandriva.org> 1.0.10-1mdk
- initial rpm package 
- small gcc4 fix as P0

