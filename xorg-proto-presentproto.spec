# NOTE: now maintained in xorg-proto-xorgproto.spec
Summary:	Present extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Present
Name:		xorg-proto-presentproto
Version:	1.1
Release:	1.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/proto/presentproto-%{version}.tar.bz2
# Source0-md5:	92f9dda9c870d78a1d93f366bcb0e6cd
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Present extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia Present.

%package devel
Summary:	Present extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Present
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	presentext

%description devel
Present extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia Present.

%prep
%setup -q -n presentproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc ChangeLog presentproto.txt
%{_includedir}/X11/extensions/present*.h
%{_pkgconfigdir}/presentproto.pc
