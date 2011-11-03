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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package looks for LuaTeX regardless of its mode and
provides the switch \ifluatex; it works with Plain TeX or
LaTeX. The package is part of the oberdiek bundle.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
