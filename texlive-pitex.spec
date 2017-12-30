# revision 24731
# category Package
# catalog-ctan /macros/plain/contrib/pitex
# catalog-date 2011-11-18 01:28:58 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-pitex
Version:	20170414
Release:	1
Summary:	Documentation macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/pitex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pitex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pitex.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111118-2
+ Revision: 754907
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111118-1
+ Revision: 739869
- texlive-pitex

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100908-1
+ Revision: 719263
- texlive-pitex
- texlive-pitex
- texlive-pitex
- texlive-pitex

