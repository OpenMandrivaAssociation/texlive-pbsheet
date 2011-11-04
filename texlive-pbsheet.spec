# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pbsheet
# catalog-date 2007-01-12 23:55:10 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-pbsheet
Version:	0.1
Release:	1
Summary:	Problem sheet class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pbsheet
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbsheet.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbsheet.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbsheet.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This class is designed to simplify the typesetting of problem
sheets with Mathematics and Computer Science content. It is
currently customised towards teaching in French (and the
examples are in French).

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
%{_texmfdistdir}/tex/latex/pbsheet/pbsheet.cls
%doc %{_texmfdistdir}/doc/latex/pbsheet/LPPL
%doc %{_texmfdistdir}/doc/latex/pbsheet/README
%doc %{_texmfdistdir}/doc/latex/pbsheet/pbsheet.pdf
%doc %{_texmfdistdir}/doc/latex/pbsheet/pbsheet.ps
%doc %{_texmfdistdir}/doc/latex/pbsheet/xpl/GNUmakefile
%doc %{_texmfdistdir}/doc/latex/pbsheet/xpl/img/simbin.eps
%doc %{_texmfdistdir}/doc/latex/pbsheet/xpl/img/simbin.pdf
%doc %{_texmfdistdir}/doc/latex/pbsheet/xpl/pbsheet.cls
%doc %{_texmfdistdir}/doc/latex/pbsheet/xpl/pgm/probadis.m
%doc %{_texmfdistdir}/doc/latex/pbsheet/xpl/pgm/rdiscr.m
%doc %{_texmfdistdir}/doc/latex/pbsheet/xpl/pgm/rint.m
%doc %{_texmfdistdir}/doc/latex/pbsheet/xpl/pgm/simbin.m
%doc %{_texmfdistdir}/doc/latex/pbsheet/xpl/xpl-fr.bib
%doc %{_texmfdistdir}/doc/latex/pbsheet/xpl/xpl-fr.pdf
%doc %{_texmfdistdir}/doc/latex/pbsheet/xpl/xpl-fr.tex
#- source
%doc %{_texmfdistdir}/source/latex/pbsheet/pbsheet.dtx
%doc %{_texmfdistdir}/source/latex/pbsheet/pbsheet.ins
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
