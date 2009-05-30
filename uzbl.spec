
%define		gitdate 20090526

Summary:	A keyboard controlled (modal vim-like bindings, or with modifier keys) browser based on Webkit
Name:		uzbl
Version:	0
Release:	0.%{gitdate}.1
License:	GPL v3
Group:		X11/Applications/Networking
Source0:	%{name}-%{gitdate}.tar.xz
# Source0-md5:	58a2ccd187b6de901f64b2968c36802d
URL:		http://www.uzbl.org/
BuildRequires:	curl-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-webkit-devel
BuildRequires:	libsoup-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The uzbl browser is a keyboard controlled (modal vim-like bindings, or
with modifier keys) browser based on Webkit.

%prep
%setup -q -n %{name}-%{gitdate}

find examples -type f | xargs sed -i 's,/examples/,/,g'

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/uzbl/examples/* $RPM_BUILD_ROOT%{_datadir}/uzbl
rm -r $RPM_BUILD_ROOT%{_datadir}/uzbl/{docs,examples}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README docs/*
%attr(755,root,root) %{_bindir}/uzbl
%attr(755,root,root) %{_bindir}/uzblctrl
%dir %{_datadir}/uzbl
%dir %{_datadir}/uzbl/scripts
%attr(755,root,root) %{_datadir}/uzbl/scripts/*
%{_datadir}/uzbl/data
%{_datadir}/uzbl/configs
