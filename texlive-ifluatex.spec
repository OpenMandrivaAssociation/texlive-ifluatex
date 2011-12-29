# revision 22180
# category Package
# catalog-ctan /macros/latex/contrib/oberdiek/ifluatex.dtx
# catalog-date 2010-03-04 00:36:20 +0100
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-ifluatex
Version:	1.3
Release:	1
Summary:	Provides the \ifluatex switch
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/oberdiek/ifluatex.dtx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifluatex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifluatex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifluatex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package looks for LuaTeX regardless of its mode and
provides the switch \ifluatex; it works with Plain TeX or
LaTeX. The package is part of the oberdiek bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/oberdiek/ifluatex.sty
%doc %{_texmfdistdir}/doc/latex/oberdiek/ifluatex.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/ifluatex-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/ifluatex-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/ifluatex-test3.tex
#- source
%doc %{_texmfdistdir}/source/latex/oberdiek/ifluatex.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
