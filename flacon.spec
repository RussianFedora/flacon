Name:           flacon
Version:        0.9.4
Release:        1%{?dist}
Summary:        Split Compressed Audio CD Image to Tracks

License:        GPLv2+
Url:            http://code.google.com/p/flacon/
Source0:        https://github.com/flacon/%{name}/archive/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  uchardet-devel
BuildRequires:  qt-devel
BuildRequires:  desktop-file-utils


%description
Flacon extracts individual tracks from one big audio file containing
the entire album of music and saves them as separate audio files. To do
this, it uses information from the appropriate CUE file. Besides, Flacon
makes it possible to conveniently revise or specify tags both for all
tracks at once or for each tag separately.

%prep
%setup -q

%build
%cmake .
make %{?_smp_mflags}

%install
%make_install
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
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_mandir}/man1/%{name}.1.gz


%changelog
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
