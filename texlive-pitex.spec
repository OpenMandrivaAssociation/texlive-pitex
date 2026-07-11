%global tl_name pitex
%global tl_revision 24731

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Documentation macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/pitex
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pitex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pitex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides macros that the author uses when writing
documentation (for example, that of the texapi and yax packages). The
tools could be used by anyone, but there is no documentation, and the
macros are subject to change without notice.

