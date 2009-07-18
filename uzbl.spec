# TODO:
# - unbash example scripts

%define		gitdate 20090703

Summary:	A keyboard controlled (modal vim-like bindings, or with modifier keys) browser based on Webkit
Summary(hu.UTF-8):	Egy billentyűzettel irányítható (vim-szerű vagy módosító kódok) böngésző Webkit alapokon
Name:		uzbl
Version:	0
Release:	0.%{gitdate}.1
License:	GPL v3
Group:		X11/Applications/Networking
Source0:	%{name}-%{gitdate}.tar.xz
# Source0-md5:	e90ffe6b73747731a1d9d7c456e3e411
Patch0:		uzbl-config.patch
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

%package tabbed
Summary:	Tabs for uzbl
Summary(hu.UTF-8):	Tabok uzbl-hez
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tabbed
Wrapper for uzbl that provides firefox-style tabs.

%description tabbed -l hu.UTF-8
Egy uzbl-wrapper, amely firefox-stílusú tabok használatát teszi lehetővé.

%package scripts
Summary:	Scripts for uzbl
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description scripts
Scripts for uzbl that handles cookies, downloads, history, etc.

%package examples
Summary:	Example configs
Summary(hu.UTF-8):	Példa konfigurációs fájlok 
Summary(pl.UTF8):	Przykładowa konfiguracja dla uzbl
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bash
Requires:	dmenu
Requires:	zenity

%description examples
Example config files for uzbl. If you want just try uzbl install this package
and run:

uzbl -c %{_examplesdir}/%{name}-%{version}/config

%description examples -l hu.UTF-8
Példa konfigurációs fájlok. Ha ki akarod
próbálni az uzbl-lel, akkor telepítsd ezt a csomagot és a következő
paranccsal indítsd:

uzbl -c %{_examplesdir}/%{name}-%{version}/config

%prep
%setup -q -n %{name}-%{gitdate}

%patch0 -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# tabbed
mv $RPM_BUILD_ROOT%{_datadir}/uzbl/examples/data/uzbl/scripts/uzbl_tabbed.py $RPM_BUILD_ROOT%{_bindir}/uzbl_tabbed

# most important scripts
install -d $RPM_BUILD_ROOT%{_datadir}/uzbl/scripts
mv $RPM_BUILD_ROOT%{_datadir}/uzbl/examples/data/uzbl/scripts $RPM_BUILD_ROOT%{_datadir}/uzbl

# example config
install -d $RPM_BUILD_ROOT%{_examplesdir}/uzbl-%{version}
mv $RPM_BUILD_ROOT%{_datadir}/uzbl/examples/config/uzbl/config $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/config
mv $RPM_BUILD_ROOT%{_datadir}/uzbl/examples/data/uzbl/forms $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/forms
rm -r $RPM_BUILD_ROOT%{_datadir}/uzbl/{docs,examples}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README docs/*
%attr(755,root,root) %{_bindir}/uzbl
%attr(755,root,root) %{_bindir}/uzblctrl
%dir %{_datadir}/uzbl

%files tabbed
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uzbl_tabbed

%files scripts
%dir %{_datadir}/uzbl/scripts
%attr(755,root,root) %{_datadir}/uzbl/scripts/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/uzbl-%{version}
