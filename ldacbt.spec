#global debug_package %{nil}

Name:           ldacbt
Summary:        AOSP libldac dispatcher
Version:        2.0.2.3
Release:        7%{?dist}
License:        Apache
URL:            https://github.com/EHfive/ldacBT/
Source:	https://github.com/EHfive/ldacBT/releases/download/v%{version}/ldacBT-%{version}.tar.gz
Patch:		lib_fix.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
# Why we need fix conflicts of others third party repos?
Provides:	libldac = %{version}

%description
AOSP libldac dispatcher.

%package        devel
Summary:        Development package for ldacbt
Requires:       %{name} = %{version}-%{release}
Provides:	libldac-devel = %{version}

%description    devel
This package contains development files for ldacbt


%prep

%setup -n ldacBT

%ifarch x86_64
%patch -p1
%endif

%build

mkdir -p %{_target_platform}
%cmake  -B %{_target_platform} -DCMAKE_BUILD_TYPE=Release \
        -DLDAC_SOFT_FLOAT=OFF \

%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}


%files
%{_libdir}/libldacBT_abr.so.2
%{_libdir}/libldacBT_abr.so.2.0.2.3
%{_libdir}/libldacBT_enc.so.2
%{_libdir}/libldacBT_enc.so.2.0.2.3

%files devel
%{_includedir}/ldac/ldacBT.h
%{_includedir}/ldac/ldacBT_abr.h
%{_libdir}/libldacBT_abr.so
%{_libdir}/libldacBT_enc.so
%{_libdir}/pkgconfig/ldacBT-abr.pc
%{_libdir}/pkgconfig/ldacBT-enc.pc


%changelog

* Wed Mar 25 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.0.2.3-7
- Rebuilt

* Mon Feb 18 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.0.2.3-1
- Updated to 2.0.2.3

* Thu Dec 27 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.0.2-1
- Initial build
