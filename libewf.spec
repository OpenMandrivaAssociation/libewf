%define	major 2
%define libname	%mklibname ewf %{major}
%define develname %mklibname -d ewf

Summary:	Utils for use with the Expert Witness Compression Format (EWF)
Name:		libewf
Version:	20120813
Release:	%mkrel 1
Group:		System/Libraries
License:	BSD
URL:		http://libewf.sourceforge.net/
Source0:	http://sourceforge.net/projects/%{name}/files/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	autoconf
BuildRequires:	libtool

%description
Libewf is a library for support of the Expert Witness Compression Format (EWF),
it support both the SMART format (EWF-S01) and the EnCase format (EWF-E01).
Libewf allows you to read and write media information within the EWF files.

This package contains utils for use with the Expert Witness Compression Format
(EWF).

%package -n	%{libname}
Summary:	The Expert Witness Compression Format (EWF) shared library
Group:          System/Libraries

%description -n	%{libname}
Libewf is a library for support of the Expert Witness Compression Format (EWF),
it support both the SMART format (EWF-S01) and the EnCase format (EWF-E01).
Libewf allows you to read and write media information within the EWF files.

%package -n	%{develname}
Summary:	Static library and header files for the libewf library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{develname}
Libewf is a library for support of the Expert Witness Compression Format (EWF),
it support both the SMART format (EWF-S01) and the EnCase format (EWF-E01).
Libewf allows you to read and write media information within the EWF files.

This package contains the static libewf library and its header files.

%prep

%setup -q

%build
#export WANT_AUTOCONF_2_5=1
#rm -f configure
#libtoolize --copy --force; aclocal; autoconf --force; autoheader; automake

export CFLAGS="%{optflags} -fPIC"

%configure2_5x --disable-static

%make

%install
%makeinstall_std

%files
%{_bindir}/ewfacquire
%{_bindir}/ewfacquirestream
#%{_bindir}/ewfalter
%{_bindir}/ewfexport
%{_bindir}/ewfinfo
%{_bindir}/ewfverify
%{_bindir}/ewfmount
%{_bindir}/ewfdebug
%{_bindir}/ewfrecover
%{_mandir}/man1/*

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog NEWS
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*
