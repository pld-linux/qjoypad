Summary:	Gamepad/joystick events to keypress converter
Name:		qjoypad
Version:	4.1.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/qjoypad/%{name}-%{version}.tar.gz
# Source0-md5:	d4a262c29bd3955c0fe51e9a0d31f619
URL:		http://qjoypad.sourceforge.net/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QJoyPad takes input from a gamepad or joystick and translates it into
key strokes or mouse actions, letting you control any XWindows program
with your game controller. This lets you play all those games that for
some reason don't have joystick support with your joystick. QJoyPad
also gives you the advantage of multiple saved layouts so you can have
a separate setting for every game, or for every class of game! That
way you can play your games the way you want, not the way the
programmers decided, and you can have the same button be "fire" in
every one of your space fighters. QJoyPad gives you the freedom and
flexibility to really take advantage of gaming devices in Linux, and
makes the Linux gaming experience just a little bit nicer.

%prep
%setup -q

%build
cd src
./config \
	--prefix="%{_prefix}" \
	--install-dir="$RPM_BUILD_ROOT"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd src
%{__make} install
rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/%{name}
