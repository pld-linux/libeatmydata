Summary:	Library designed to transparently disable fsync and friends
Name:		libeatmydata
Version:	82
Release:	1
License:	GPL v3
Group:		Applications
Source0:	https://www.flamingspork.com/projects/libeatmydata/%{name}-%{version}.tar.gz
# Source0-md5:	56a4d342f209ab75a9ee360236e3e5bc
URL:		https://www.flamingspork.com/projects/libeatmydata/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libeatmydata is a small LD_PRELOAD library designed to (transparently)
disable fsync (and friends, like open(O_SYNC)). This has two
side-effects: making software that writes data safely to disk a lot
quicker and making this software no longer crash safe.

DO NOT use libeatmydata on software where you care about what it
stores. It's called libEAT-MY-DATA for a reason.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la

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
%ghost %attr(755,root,root) %{_libdir}/libeatmydata.so.1
%attr(755,root,root) %{_libdir}/libeatmydata.so.1.*
