Summary:	Small library to interface with ALSA in the Linux kernel
Summary(pl.UTF-8):	Mała biblioteka do współpracy z podsystemem ALSA w jądrze Linuksa
Name:		tinyalsa
Version:	1.1.1
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/tinyalsa/tinyalsa/releases
Source0:	https://github.com/tinyalsa/tinyalsa/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ec5c1cc175fcb8c9d3d0adcececf10a9
Patch0:		%{name}-opt.patch
URL:		https://github.com/tinyalsa/tinyalsa
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tinyalsa is a small library to interface with ALSA in the Linux
kernel. The aims are:
- Provide a basic PCM and mixer API
- If it's not absolutely needed, don't add it to the API
- Avoid supporting complex and unnecessary operations that could be
  dealt with at a higher level

%description -l pl.UTF-8
tinyalsa to mała biblioteka do współpracy z podsystemem ALSA w jądrze
Linuksa. Jej cele to:
- dostarczenie podstawowego API do PCM i miksera
- jeśli coś nie jest absolutnie konieczne, nie należy dodawać tego do
  API
- unikanie wspierania złożonych i niepotrzebnych operacji, które można
  obsłużyć na wyższym poziomie

%package devel
Summary:	Header files for tinyalsa library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki tinyalsa
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for tinyalsa library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tinyalsa.

%package static
Summary:	Static tinyalsa library
Summary(pl.UTF-8):	Statyczna biblioteka tinyalsa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static tinyalsa library.

%description static -l pl.UTF-8
Statyczna biblioteka tinyalsa.

%package tools
Summary:	Utilities for tinyalsa library
Summary(pl.UTF-8):	Programy narzędziowe do biblioteki tinyalsa
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description tools
Utilities for tinyalsa library.

%description tools -l pl.UTF-8
Programy narzędziowe do biblioteki tinyalsa.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags}" \
%{__make} \
	CC="%{__cc}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%triggerpostun -- tinyalsa < 1.1.0
rm -f %{_libdir}/libtinyalsa.so.1
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NOTICE README.md
%attr(755,root,root) %{_libdir}/libtinyalsa.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtinyalsa.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtinyalsa.so
%{_includedir}/tinyalsa
%{_mandir}/man3/libtinyalsa-mixer.3*
%{_mandir}/man3/libtinyalsa-pcm.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libtinyalsa.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tinycap
%attr(755,root,root) %{_bindir}/tinymix
%attr(755,root,root) %{_bindir}/tinypcminfo
%attr(755,root,root) %{_bindir}/tinyplay
%{_mandir}/man1/tinycap.1*
%{_mandir}/man1/tinymix.1*
%{_mandir}/man1/tinypcminfo.1*
%{_mandir}/man1/tinyplay.1*
