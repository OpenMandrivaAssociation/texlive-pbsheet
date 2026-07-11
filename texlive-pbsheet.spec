%global tl_name pbsheet
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Problem sheet class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pbsheet
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pbsheet.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pbsheet.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pbsheet.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class is designed to simplify the typesetting of problem sheets
with Mathematics and Computer Science content. It is currently
customised towards teaching in French (and the examples are in French).

