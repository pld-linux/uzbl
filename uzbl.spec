# TODO:
# - Where to place example config files and scripts?
# - unbash example scripts
# - example scripts should use $XDG_DATA_HOME, not tmp nor /usr/share

%define		gitdate 20090526

Summary:	A keyboard controlled (modal vim-like bindings, or with modifier keys) browser based on Webkit
Name:		uzbl
Version:	0
Release:	0.%{gitdate}.2
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

%package examples
Summary:	Example config and scripts for uzbl
Summary(pl.UTF8):	Przykładowa konfiguracja i skrypty dla uzbl
Group:		Documentation
Requires:	bash
Requires:	dmenu
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	zenity

%description examples
Example config files and scripts for uzbl. If you want just try uzbl install
this package and run:

uzbl -c %{_datadir}/uzbl/configs/sampleconfig

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

%files examples
%dir %{_datadir}/uzbl
%dir %{_datadir}/uzbl/scripts
%attr(755,root,root) %{_datadir}/uzbl/scripts/*
%{_datadir}/uzbl/data
%{_datadir}/uzbl/configs
