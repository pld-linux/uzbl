# TODO:
# - review python deps
# - s,/usr/bin/env python,/usr/bin/python,
Summary:	A keyboard controlled (modal vim-like bindings, or with modifier keys) browser based on Webkit
Summary(hu.UTF-8):	Egy billentyűzettel irányítható (vim-szerű vagy módosító kódok) böngésző Webkit alapokon
Summary(pl.UTF-8):	Minimalistyczna przeglądarka w całości obsługiwana przy użyciu klawiatury
Name:		uzbl
Version:	2013.12.08
Release:	1
License:	GPL v3
Group:		X11/Applications/Networking
# git://github.com/Dieterbe/uzbl.git
# Source0:	https://github.com/Dieterbe/uzbl/archive/%{version}.tar.gz
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	ff21df4ce77829ec35f3632b5232069d
Patch0:		%{name}-build.patch
URL:		http://www.uzbl.org/
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-webkit3-devel >= 1.2.0-4
BuildRequires:	libsoup-devel
BuildRequires:	pkgconfig
BuildRequires:	python3-devel
BuildRequires:	rpm-pythonprov
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	dmenu
Requires:	socat
Requires:	xclip
Requires:	zenity
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The uzbl browser is a keyboard controlled (modal vim-like bindings, or
with modifier keys) browser based on Webkit.

%description -l hu.UTF-8
Egy billentyűzettel irányítható (vim-szerű vagy módosító kódok)
böngésző Webkit alapokon.

%description -l pl.UTF-8
uzbl jest przeglądarką, która może być w całości obsługiwana przy
użyciu klawiatury. Domyślne ustawienia klawiszy są wzorowane na
skrótach klawiszowych programu vim. uzbl wykorzystuje silnik Webkit.

uzbl sam nie obsługuje zakładek, historii, pobierania plików. Funkcje
te są realizowane przez zewnętrzne skrypty. Dzięki temu oraz dzięki
ładowanym na życzenie skryptom JavaScript przeglądarka ta jest bardzo
elastyczna, konfigurowalna i może być w łatwy sposób rozszerzana.

%package core
Summary:	Uzbl core
Summary(pl.UTF-8):	Jądro Uzbl
Group:		X11/Applications/Networking
Requires:	gtk-webkit >= 1.2.0-4
Suggests:	%{name}-event-manager = %{epoch}:%{version}-%{release}
Obsoletes:	uzbl-examples
Obsoletes:	uzbl-scripts

%description core
Main component of uzbl browser. You also need one of UI components
(uzbl or uzbl-tabbed).

%description core -l pl.UTF-8
Jądro przeglądarki uzbl. Aby mieć w pełni funkcjonalną przeglądarkę
potrzebujesz jeszcze jeden z interfejsów graficznych: uzbl lub
uzbl-tabbed.

%package event-manager
Summary:	Uzbl event manager
Summary(pl.UTF-8):	Zarządca zdarzeń dla uzbl
Group:		X11/Applications/Networking

%description event-manager
Uzbl event manager.

%description event-manager -l pl.UTF-8
Zarządca zdarzeń dla uzbl.

%package tabbed
Summary:	Tabs for uzbl
Summary(hu.UTF-8):	Tabok uzbl-hez
Summary(pl.UTF-8):	Taby dla uzbl
Group:		X11/Applications/Networking
Requires:	%{name}-core = %{epoch}:%{version}-%{release}

%description tabbed
Wrapper for uzbl that provides firefox-style tabs.

%description tabbed -l hu.UTF-8
Egy uzbl-wrapper, amely firefox-stílusú tabok használatát teszi
lehetővé.

%description tabbed -l pl.UTF-8
Skrypt, który dodaje do uzbl taby podobne do tych znanych użytkownikom
przeglądarki firefox.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/uzbl/docs

ln -s %{_bindir}/uzbl-browser $RPM_BUILD_ROOT%{_bindir}/uzbl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README docs/*
%attr(755,root,root) %{_bindir}/uzbl
%attr(755,root,root) %{_bindir}/uzbl-browser

%files core
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uzbl-core
%dir %{_datadir}/uzbl
%dir %{_datadir}/uzbl/examples
%{_datadir}/uzbl/examples/config
%dir %{_datadir}/uzbl/examples/data
%dir %{_datadir}/uzbl/examples/data/scripts
#%dir %{_datadir}/uzbl/examples/data/plugins
%attr(755,root,root) %{_datadir}/uzbl/examples/data/scripts/*
#%attr(755,root,root) %{_datadir}/uzbl/examples/data/plugins/*
%{_datadir}/uzbl/examples/data/dforms
%{_datadir}/uzbl/examples/data/bookmarks
%{_datadir}/uzbl/examples/data/per-site-settings
%{_datadir}/uzbl/examples/data/uzbl.png

%{py3_sitescriptdir}/uzbl*.egg-info
%{py3_sitescriptdir}/uzbl

%files event-manager
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uzbl-event-manager

%files tabbed
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uzbl-tabbed
