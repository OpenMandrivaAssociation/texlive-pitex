Name:		texlive-pitex
Version:	24731
Release:	2
Summary:	Documentation macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/pitex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pitex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pitex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides macros that the author uses when writing
documentation (for example, that of the texapi and yax
packages). The tools could be used by anyone, but there is no
documentation, and the macros are subject to change without
notice.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/pitex/base.ptxlua
%{_texmfdistdir}/tex/plain/pitex/blocks.ptx
%{_texmfdistdir}/tex/plain/pitex/files.ptx
%{_texmfdistdir}/tex/plain/pitex/fonts.ptx
%{_texmfdistdir}/tex/plain/pitex/fonts.ptxlua
%{_texmfdistdir}/tex/plain/pitex/inserts.ptx
%{_texmfdistdir}/tex/plain/pitex/lua.ptx
%{_texmfdistdir}/tex/plain/pitex/output.ptx
%{_texmfdistdir}/tex/plain/pitex/pitex.tex
%{_texmfdistdir}/tex/plain/pitex/references.ptx
%{_texmfdistdir}/tex/plain/pitex/sections.ptx
%{_texmfdistdir}/tex/plain/pitex/verbatim.ptx
%doc %{_texmfdistdir}/doc/plain/pitex/README
%doc %{_texmfdistdir}/doc/plain/pitex/foundry-settings.lua
%doc %{_texmfdistdir}/doc/plain/pitex/i-pitex.lua
%doc %{_texmfdistdir}/doc/plain/pitex/pitex-doc.pdf
%doc %{_texmfdistdir}/doc/plain/pitex/pitex-doc.tex
%doc %{_texmfdistdir}/doc/plain/pitex/pitex-doc.txt

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
