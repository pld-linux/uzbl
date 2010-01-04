# TODO:
# - unbash example scripts

Summary:	A keyboard controlled (modal vim-like bindings, or with modifier keys) browser based on Webkit
Summary(hu.UTF-8):	Egy billentyűzettel irányítható (vim-szerű vagy módosító kódok) böngésző Webkit alapokon
Summary(pl.UTF-8):	Minimalistyczna przeglądarka w całości obsługiwana przy użyciu klawiatury
Name:		uzbl
Version:	2009.12.22
Release:	1
License:	GPL v3
Group:		X11/Applications/Networking
# git://github.com/Dieterbe/uzbl.git
Source0:	http://github.com/Dieterbe/uzbl/tarball/2009.12.22
# Source0-md5:	8cf1bd7c2fe6c14345b1671160f0214f
Patch0:		%{name}-config.patch
Patch1:		%{name}-dmenu.patch
URL:		http://www.uzbl.org/
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
BuildRequires:	curl-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-webkit-devel
BuildRequires:	libsoup-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
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
skrótach klawiszowych programu vim. Uzbl może działać w modalnym
trybie podobnie jak vim albo w trybie przypominającym działanie
emacsa. uzbl wykorzystuje silnik Webkit.

uzbl sam nie obsługuje zakładek, historii, pobierania plików.  Funkcjonalności
te są realizowane przez zewnętrzne skrypty. Dzięki temu przeglądarka ta jest
bardzo elastyczna, konfigurowalna i może być w łatwy sposób rozszerzana.

%package core
Summary:	Uzbl core
Summary(pl.UTF-8):	Jądro Uzbl
Group:		X11/Applications/Networking
Suggests:	%{name}-cookie-daemon = %{epoch}:%{version}-%{release}
Suggests:	%{name}-event-manager = %{epoch}:%{version}-%{release}

%description core
Main component of uzbl browser. You also need one of UI components
(uzbl or uzbl-tabbed).

%description core -l pl.UTF-8
Jądro przeglądarki uzbl. Aby mieć w pełni funkcjonalną przeglądarkę
potrzebujesz jeszcze jeden z interfejsów graficznych: uzbl lub uzbl-tabbed.

%package event-manager
Summary:	Uzbl event manager
Summary(pl.UTF-8):	Zarządca zdarzeń dla uzbl
Group:		X11/Applications/Networking

%description event-manager
Uzbl event manager.

%description event-manager
Zarządca zdarzeń dla uzbl.

%package cookie-daemon
Summary:	Uzbl cookie daemon
Summary(pl.UTF-8):	Serwer ciasteczek dla uzbl
Group:		X11/Applications/Networking

%description cookie-daemon
uzbl-cookie-daemon provides http cookies for uzbl.

%description cookie-daemon -l pl.UTF-8
Obsługa ciasteczek http (coockies) dla przeglądarki uzbl.

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

%package scripts
Summary:	Scripts for uzbl
Summary(pl.UTF-8):	Skrypty rozszerzające funkcjonalność uzbl
Group:		X11/Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description scripts
Scripts for uzbl that handles cookies, downloads, history, etc.

%description scripts -l pl.UTF-8
Skrypty dodające do uzbl obsługę cookies, pobierania plików, historii
i tym podobnych.

%package examples
Summary:	Example configs
Summary(hu.UTF-8):	Példa konfigurációs fájlok
Summary(pl.UTF-8):	Przykładowa konfiguracja dla uzbl
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bash
Requires:	dmenu
Requires:	socat
Requires:	zenity

%description examples
Example config files for uzbl. If you want just try uzbl install this
package and run:

uzbl -c %{_examplesdir}/%{name}-%{version}/config

%description examples -l hu.UTF-8
Példa konfigurációs fájlok. Ha ki akarod próbálni az uzbl-lel, akkor
telepítsd ezt a csomagot és a következő paranccsal indítsd:

uzbl -c %{_examplesdir}/%{name}-%{version}/config

%description examples -l pl.UTF-8
Przykładowa konfiguracja przeglądarki uzbl. Jeżeli chcesz po prostu
wypróbować uzbl, zainstaluj ten pakiet i wykonaj komendę:

uzbl -c %{_examplesdir}/%{name}-%{version}/config

%prep
%setup -q -n Dieterbe-uzbl-4994115

%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

# most important scripts
install -d $RPM_BUILD_ROOT%{_datadir}/uzbl/scripts
mv $RPM_BUILD_ROOT%{_datadir}/uzbl/examples/data/uzbl/scripts $RPM_BUILD_ROOT%{_datadir}/uzbl

rm -r $RPM_BUILD_ROOT%{_datadir}/uzbl/docs

ln -s %{_bindir}/uzbl-browser $RPM_BUILD_ROOT%{_bindir}/uzbl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README docs/*
%attr(755,root,root) %{_bindir}/uzbl
%attr(755,root,root) %{_bindir}/uzbl-browser
%dir %{_datadir}/uzbl

%files core
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uzbl-core

%files event-manager
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uzbl-event-manager

%files cookie-daemon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uzbl-cookie-daemon

%files tabbed
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uzbl-tabbed

%files scripts
%defattr(644,root,root,755)
%dir %{_datadir}/uzbl/scripts
%attr(755,root,root) %{_datadir}/uzbl/scripts/*

%files examples
%defattr(644,root,root,755)
%{_datadir}/uzbl/examples
