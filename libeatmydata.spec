Summary:	Library designed to transparently disable fsync and friends
Summary(pl.UTF-8):	Biblioteka do przezroczystego wyłączania fsync itp.
Name:		libeatmydata
Version:	105
Release:	1
License:	GPL v3
Group:		Applications/File
Source0:	https://www.flamingspork.com/projects/libeatmydata/%{name}-%{version}.tar.gz
# Source0-md5:	6681166466e589eb0d71177709361256
# https://github.com/stewartsmith/libeatmydata
URL:		https://www.flamingspork.com/projects/libeatmydata/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libeatmydata is a small LD_PRELOAD library designed to (transparently)
disable fsync (and friends, like open(O_SYNC)). This has two
side-effects: making software that writes data safely to disk a lot
quicker and making this software no longer crash safe.

DO NOT use libeatmydata on software where you care about what it
stores. It's called libEAT-MY-DATA for a reason.

%description -l pl.UTF-8
libeatmydata to mała biblioteka ładowana przez LD_PRELOAD służąca do
(przezroczystego) wyłączania fsync (i podobnych mechanizmów, jak
open(O_SYNC)). Ma to dwa skutki uboczne: programy zapisujące dane na
dysku w sposób bezpieczny robią to dużo szybciej, ale nie są już
odporne na awarie.

NIE NALEŻY używać libeatmydata w przypadkach, kiedy zależy nam na
zapisywanych danych. Biblioteka nazywa się libEAT-MY-DATA (zjedz moje
dane) nie bez powodu.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/eatmydata
%attr(755,root,root) %{_libdir}/eatmydata.sh
%attr(755,root,root) %{_libdir}/libeatmydata.so
