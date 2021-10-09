%define major 2
%define libname %mklibname ewf %{major}
%define develname %mklibname -d ewf

%global optflags %{optflags} -fPIC -std=gnu89
%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	Utils for use with the Expert Witness Compression Format (EWF)
Name:		libewf
Version:	20140608
Release:	9
Group:		System/Libraries
License:	BSD
URL:		https://github.com/libyal/libewf
Source0:	https://googledrive.com/host/0B3fBvzttpiiSMTdoaVExWWNsRjg/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(python)
BuildRequires:	gettext-devel
BuildRequires:	autoconf
BuildRequires:	libtool

%description
Libewf is a library for support of the Expert Witness Compression Format (EWF),
it support both the SMART format (EWF-S01) and the EnCase format (EWF-E01).
Libewf allows you to read and write media information within the EWF files.

This package contains utils for use with the Expert Witness Compression Format
(EWF).

%package -n %{libname}
Summary:	The Expert Witness Compression Format (EWF) shared library
Group:		System/Libraries

%description -n %{libname}
Libewf is a library for support of the Expert Witness Compression Format (EWF),
it support both the SMART format (EWF-S01) and the EnCase format (EWF-E01).
Libewf allows you to read and write media information within the EWF files.

%package -n %{develname}
Summary:	Static library and header files for the libewf library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n %{develname}
Libewf is a library for support of the Expert Witness Compression Format (EWF),
it support both the SMART format (EWF-S01) and the EnCase format (EWF-E01).
Libewf allows you to read and write media information within the EWF files.

This package contains the static libewf library and its header files.

%prep
%autosetup -p1

%build
%configure \
    --enable-wide-character-type

# Remove rpath from libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build

%install
%make_install

%files
%{_bindir}/ewfacquire
%{_bindir}/ewfacquirestream
%{_bindir}/ewfexport
%{_bindir}/ewfinfo
%{_bindir}/ewfverify
%{_bindir}/ewfmount
%{_bindir}/ewfdebug
%{_bindir}/ewfrecover
%doc %{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS COPYING ChangeLog NEWS
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_mandir}/man3/*
