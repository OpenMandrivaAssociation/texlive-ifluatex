# revision 26725
# category Package
# catalog-ctan /macros/latex/contrib/oberdiek/ifluatex.dtx
# catalog-date 2012-05-29 15:13:53 +0200
# catalog-license lppl1.3
# catalog-version 1.3
Name:		texlive-ifluatex
Version:	1.4
Release:	3
Summary:	Provides the \ifluatex switch
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/oberdiek/ifluatex.dtx
License:	LPPL1.3
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


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-4
+ Revision: 812305
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-3
+ Revision: 804850
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 752691
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 718697
- texlive-ifluatex
- texlive-ifluatex
- texlive-ifluatex
- texlive-ifluatex

