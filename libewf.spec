%define	major 1
%define libname	%mklibname ewf %{major}
%define develname %mklibname -d ewf

Summary:	Utils for use with the Expert Witness Compression Format (EWF)
Name:		libewf
Version:	20070512
Release:	%mkrel 1
Group:		System/Libraries
License:	BSD
URL:		https://www.uitwisselplatform.nl/projects/libewf/
Source0:	https://www.uitwisselplatform.nl/frs/download.php/303/%{name}-%{version}.tar.gz
BuildRequires:	openssl-devel
BuildRequires:	e2fsprogs-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal; autoconf --force; autoheader; automake

export CFLAGS="%{optflags} -fPIC"

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/ewfacquire
%{_bindir}/ewfacquirestream
%{_bindir}/ewfalter
%{_bindir}/ewfexport
%{_bindir}/ewfinfo
%{_bindir}/ewfverify
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS TESTS
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*
