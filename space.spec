%define  version    1.0.0
%define release    15
%define name  space

Summary: Desktop backgrounds - Photo and data images from NASA
Name: %{name}
Version: %{version}
Release: %{release}
License: Public domain 
Group: Graphical desktop/Other
Source: %{name}-%{version}.tar.bz2
Source1: README.space
Source2: PHOTO_FAQ.ps

URL: http://www.nasa.gov/gallery/photo/
BuildRoot:%{_tmppath}/%{name}-buildroot
BuildArchitectures: noarch

%description
An extract of more than 500,000 photos and data images from 10 NASA
Centers have been linked together to create a searchable database of
agency imagery covering a variety of NASA programs. The NASA Image
Exchange (http://nix.nasa.gov/) is the first step toward a
comprehensive online imagery collection, and other collections will be
added as they become available. Curators of NASA image collections can
contact the NIX for details on how to join the project.

%prep
rm -rf $RPM_BUILd_ROOT

%setup0 -c

%install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/backgrounds
cd $RPM_BUILD_ROOT%{_datadir}/pixmaps/backgrounds
bzcat %{SOURCE0}|tar xv

cd $RPM_BUILD_SOURCE
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%name-%version
cp %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/%{_docdir}/%name-%version/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_datadir}/pixmaps/backgrounds/space
%_docdir/%name-%version/*



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-14mdv2010.0
+ Revision: 434011
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-13mdv2009.0
+ Revision: 260915
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-12mdv2009.0
+ Revision: 252789
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-10mdv2008.1
+ Revision: 127497
- kill re-definition of %%buildroot on Pixel's request
- import space


* Thu Dec 15 2005 Lenny Cartier <lenny@mandriva.com> 1.0.0-10mdk
- rebuild

* Fri Sep 10 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-9mdk
- rebuild

* Mon Aug 18 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-8mdk
- remove obsoletes & provides

* Wed Jan 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-7mdk
- rebuild

* Tue Oct 08 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-6mdk
- rebuild

* Tue Sep 04 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-5mdk
- s/Copyright/License

* Mon Sep 18 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-4mdk
- BM

* Wed May 03 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-3mdk
- fix group

* Fri Dec 10 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Fix Group

* Wed Nov 24 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Split into several packages

* Fri Apr 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adptations.

* Fri Apr  2 1999 Jonathan Blandford <jrb@redhat.com>
- added propaganda tiles.  Spruced it up a bit
- moved README files out of tarball, and into docs dir.

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- First attempt
