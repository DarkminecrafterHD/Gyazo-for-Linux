Name: gyazo
Version: 1.3
Release: 1
Summary: Screen capture tool
License: GPLv3+
Group: Amusements/Graphics
URL: http://gyazo.com/
Source0: %{name}_%{version}.orig.tar.gz
Requires: ruby, ImageMagick

%description
Seriously Instant Screen-Grabbing Gyazo lets you instantly grab the screen and upload the image to the web. You can easily share them on Chat, Twitter, Blog, Tumblr, etc.

%prep
%setup -q
%build
%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/pixmaps
cp src/gyazo.rb %{buildroot}/usr/bin
cp src/gyazo-gnome.rb %{buildroot}/usr/bin
cp src/gyazo.desktop %{buildroot}/usr/share/applications
cp src/gyazo-gnome.desktop %{buildroot}/usr/share/applications
cp icons/gyazo.png %{buildroot}/usr/share/pixmaps

%post
ln -f -s /usr/bin/gyazo.rb /usr/bin/gyazo
ln -f -s /usr/bin/gyazo-gnome.rb /usr/bin/gyazo-gnome

%postun
rm -f /usr/bin/gyazo
rm -f /usr/bin/gyazo-gnome

%clean
%files
/usr/bin/gyazo.rb
/usr/bin/gyazo-gnome.rb
/usr/share/applications/gyazo.desktop
/usr/share/applications/gyazo-gnome.desktop
/usr/share/pixmaps/gyazo.png

%changelog
* Mon Jul 13 2015 Yosuke Tamura <yosuke.tamura.tp8@gmail.com>
- Added this SPEC file to build RPM package.
