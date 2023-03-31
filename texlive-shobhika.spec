Name:		texlive-shobhika
Version:	50555
Release:	2
Summary:	An OpenType Devanagari font designed for scholars
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/shobhika
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shobhika.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shobhika.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a free, open source, Unicode compliant,
OpenType font with support for Devanagari, Latin, and Cyrillic
scripts. It is available in two weights--regular and bold. The
font is designed with over 1600 Devanagari glyphs, including
support for over 1100 conjunct consonants, as well as vedic
accents. The Latin component of the font not only supports a
wide range of characters required for Roman transliteration of
Sanskrit, but also provides a subset of regularly used
mathematical symbols for scholars working with scientific and
technical documents. The project has been launched under the
auspices of the Science and Heritage Initiative (SandHI) at IIT
Bombay, and builds upon the following two fonts for its
Devanagari and Latin components respectively: (i) Yashomudra by
Rajya Marathi Vikas Samstha, and (ii) PT Serif by ParaType. We
would like to thank both these organisations for releasing
their fonts under the SIL Open Font Licence, which has enabled
us to create Shobhika.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/opentype/public/shobhika
%doc %{_texmfdistdir}/doc/fonts/shobhika

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
