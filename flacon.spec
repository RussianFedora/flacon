Name:           flacon
Version:        0.8.0
Release:        1%{?dist}
Summary:        Split Compressed Audio CD Image to Tracks

License:        GPLv3
Url:            http://code.google.com/p/flacon/
Source0:        http://flacon.googlecode.com/files/%{name}-%{version}.tgz

BuildRequires:  python
BuildRequires:  PyQt4-devel
BuildRequires:  python-chardet
BuildRequires:  shntool
BuildRequires:  qt-devel
BuildRequires:  desktop-file-utils

BuildArch:      noarch


%description
Flacon extracts individual tracks from one big audio file containing
the entire album of music and saves them as separate audio files. To do
this, it uses information from the appropriate CUE file. Besides, Flacon
makes it possible to conveniently revise or specify tags both for all
tracks at once or for each tag separately.

%prep
%setup -q
sed -i -e "s|LRELEASE    = lrelease|LRELEASE    = lrelease-qt4|" "Makefile";

%build
make clean
make

%install
make install DESTDIR=%{buildroot}
%find_lang %{name} --with-qt
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/usr/bin/update-desktop-database &> /dev/null || 
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || 
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*


%changelog
* Fri May 31 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.8.0-1.R
- update to 0.8.0

* Mon Sep 03 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.2-1.R
- Initial release
