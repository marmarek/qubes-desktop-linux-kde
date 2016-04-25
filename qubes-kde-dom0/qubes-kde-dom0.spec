# This is a meta package that makes installing all KDE components easy

%if 0%{?qubes_builder}
%define _sourcedir %(pwd)/qubes-kde-dom0
%endif

Name:    qubes-kde-dom0
Summary: Metapackage for installing all KDE components needed for Qubes Dom0

# Arbitrarily choose 5.0 as the version, as some KDE packages seem to have different
# versioning schemes. 5.0 and above should be fine for Qubes OS upgrades to releases
# above r3.1 as Qubes OS r3.1 had 4.12.3 as the qubes-kde-dom0 package version.
#
# Example KDE package versions from Fedora 23 as of 2016-04-12:
#   plasma-desktop 5.4.2
#   kf5-plasma 5.21.0
#   kde-runtime 15.12.3
Version: 5.0
Release: 1%{?dist}

License: GPL2
URL: http://qubes-os.org

BuildArch: noarch

Requires: kde-settings-plasma
Requires: plasma-workspace
Requires: kde-runtime
Requires: kde-baseapps
Requires: sddm
Requires: sddm-breeze
Requires: sddm-kcm
Requires: ksysguardd
Requires: breeze-cursor-themes
Requires: breeze-icon-theme
# KDE4
Requires: kdelibs

# other 3rd party packages that are useful in Dom0...

# The konsole really looks awful without those fonts:
Requires: dejavu-sans-mono-fonts
Requires: dejavu-sans-fonts

# This is for people who don't use NetVM (i.e. don't have VT-d hardware)
# This should be left to the user IMO
#Requires: knetworkmanager

# Qubes-customized menus
Requires: qubes-menus

# Custom Breeze style for Qubes
Requires: plasma-breeze-qubes
Requires: plasma-breeze-qubes-common
Requires: kde-style-breeze-qubes

Source0: kfileplaces-bookmarks.xml
Source1: kickoffrc
source2: kscreensaverrc

%description
%{summary}.

%install
install -D %{SOURCE0} %{buildroot}%{_sysconfdir}/skel/.kde/share/apps/kfileplaces/bookmarks.xml
install -D %{SOURCE1} %{buildroot}%{_sysconfdir}/skel/.kde/share/config/kickoffrc
install -D %{SOURCE2} %{buildroot}%{_sysconfdir}/skel/.kde/share/config/kscreensaverrc

%files
%defattr (-,root,root,-)
%{_sysconfdir}/skel/.kde/share/apps/kfileplaces/bookmarks.xml
%{_sysconfdir}/skel/.kde/share/config/kickoffrc
%{_sysconfdir}/skel/.kde/share/config/kscreensaverrc
%changelog
* Mon May 24 2010 Joanna Rutkowska <joanna@invisiblethingslab.com>
- spec file adapted to Qubes OS (based on Fedora spec)
- based on the original spec from Fedora 12:

