%define  version    1.0.0
%define  release    %mkrel 13
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

