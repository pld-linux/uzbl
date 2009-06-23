# TODO:
# - Where to place example config files and scripts?
# - unbash example scripts
# - example scripts should use $XDG_DATA_HOME, not tmp nor /usr/share
# - ... rewrite example config and scripts from scratch.

%define		gitdate 20090620

Summary:	A keyboard controlled (modal vim-like bindings, or with modifier keys) browser based on Webkit
Summary(hu.UTF-8):	Egy billentyűzettel irányítható (vim-szerű vagy módosító kódok) böngésző Webkit alapokon
Name:		uzbl
Version:	0
Release:	0.%{gitdate}.1
License:	GPL v3
Group:		X11/Applications/Networking
Source0:	%{name}-%{gitdate}.tar.xz
# Source0-md5:	314bbf2d41bfa2aab9644dd6bced5184
URL:		http://www.uzbl.org/
BuildRequires:	curl-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-webkit-devel
BuildRequires:	libsoup-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The uzbl browser is a keyboard controlled (modal vim-like bindings, or
with modifier keys) browser based on Webkit.

%description -l hu.UTF-8
Egy billentyűzettel irányítható (vim-szerű vagy módosító kódok)
böngésző Webkit alapokon.

%package examples
Summary:	Example config and scripts for uzbl
Summary(hu.UTF-8):	Példa konfigurációs fájlok és szkriptek uzbl-hez
Summary(pl.UTF8):	Przykładowa konfiguracja i skrypty dla uzbl
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bash
Requires:	dmenu
Requires:	zenity

%description examples
Example config files and scripts for uzbl. If you want just try uzbl
install this package and run:

uzbl -c %{_datadir}/uzbl/configs/sampleconfig

%description examples -l hu.UTF-8
Példa konfigurációs fájlok és szkriptek uzbl-hez. Ha ki akarod
próbálni az uzbl-lel, akkor telepítsd ezt a csomagot és a következő
paranccsal indíthatod:

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
%defattr(644,root,root,755)
%dir %{_datadir}/uzbl
%dir %{_datadir}/uzbl/data
%dir %{_datadir}/uzbl/data/uzbl
%dir %{_datadir}/uzbl/data/uzbl/scripts
%attr(755,root,root) %{_datadir}/uzbl/data/uzbl/scripts/*
%{_datadir}/uzbl/data/uzbl/forms
%{_datadir}/uzbl/data/uzbl/bookmarks
%{_datadir}/uzbl/data/uzbl/*.*
%{_datadir}/uzbl/config
