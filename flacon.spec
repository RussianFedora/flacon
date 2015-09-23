Name:          flacon
Version:       1.2.0
Release:       1%{?dist}
Summary:       Split Compressed Audio CD Image to Tracks

License:       LGPLv2+
URL:           http://flacon.github.io/
Source0:       https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz

BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: qt5-qttools-devel
BuildRequires: uchardet-devel
# check
BuildRequires: /usr/bin/desktop-file-validate

Requires:      shntool
Requires:      faac
Requires:      flac
Requires:      lame
Requires:      mac
Requires:      mp3gain
Requires:      opus-tools
Requires:      vorbis-tools
Requires:      vorbisgain
Requires:      wavpack

%description
Flacon extracts individual tracks from one big audio file containing
the entire album of music and saves them as separate audio files. To do
this, it uses information from the appropriate CUE file. Besides, Flacon
makes it possible to conveniently revise or specify tags both for all
tracks at once or for each tag separately.

%prep
%setup -q

%build
%cmake . -DBUILD_TESTS=Yes
%make_build

%install
%make_install

%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1.*

%changelog
* Wed Sep 23 2015 Maxim Orlov <murmansksity@gmail.com> 1.2.0-1.R
- update to 1.2.0

* Thu Aug 21 2014 Vasiliy N. Glazov <vascom2@gmail.com> 1.0.1-1.R
- update to 1.0.1

* Tue Mar 11 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.4-1.R
- update to 0.9.4

* Tue Jan 21 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.3-1.R
- update to 0.9.3

* Thu Jan 09 2014 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.2-1.R
- update to 0.9.2

* Thu Aug 01 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 0.8.0-2.R
- corrected make flags
- use more macros

* Fri May 31 2013 Vasiliy N. Glazov <vascom2@gmail.com> 0.8.0-1.R
- update to 0.8.0

* Mon Sep 03 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.2-1.R
- Initial release
