Summary:	Small library to interface with ALSA in the Linux kernel
Summary(pl.UTF-8):	Mała biblioteka do współpracy z podsystemem ALSA w jądrze Linuksa
Name:		tinyalsa
Version:	0
%define	snap	20140604
Release:	0.%{snap}.2
License:	BSD
Group:		Libraries
Source0:	https://github.com/tinyalsa/tinyalsa/archive/master/%{name}-%{snap}.tar.gz
# Source0-md5:	1d1f052450936f4fa78d73244e25f871
Patch0:		%{name}-make.patch
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

%prep
%setup -q -n tinyalsa-master
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -Wall -c" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

install tinycap tinymix tinypcminfo tinyplay $RPM_BUILD_ROOT%{_bindir}
install libtinyalsa.so $RPM_BUILD_ROOT%{_libdir}
cp -pr include/tinyalsa $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/tinycap
%attr(755,root,root) %{_bindir}/tinymix
%attr(755,root,root) %{_bindir}/tinypcminfo
%attr(755,root,root) %{_bindir}/tinyplay
%attr(755,root,root) %{_libdir}/libtinyalsa.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/tinyalsa
