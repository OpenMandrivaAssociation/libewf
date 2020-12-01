%define	major 2
%define libname	%mklibname ewf %{major}
%define develname %mklibname -d ewf

%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	Utils for use with the Expert Witness Compression Format (EWF)
Name:		libewf
Version:	20201129
Release:	1
Group:		System/Libraries
License:	BSD
URL:		https://github.com/libyal/libewf
Source0:	https://github.com/libyal/libewf/releases/download/%{version}/libewf-experimental-%{version}.tar.gz
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	python-devel
BuildRequires:	gettext-devel
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
%autosetup -n %{name}-experimental-%{version} -p1

%build
export CFLAGS="%{optflags} -fPIC -std=gnu89"
#./autogen.sh
%configure --disable-static
%make_build

%install
%make_install

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
