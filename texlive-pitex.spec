# revision 19883
# category Package
# catalog-ctan /macros/plain/contrib/pitex
# catalog-date 2010-09-08 12:21:11 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-pitex
Version:	20100908
Release:	1
Summary:	Documentation macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/pitex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pitex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pitex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The bundle provides macros that the author uses when writing
documentation (for example, that of the texapi and yax
packages). The tools could be used by anyone, but there is no
documentation, and the macros are subject to change without
notice.

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
%{_texmfdistdir}/tex/plain/pitex/fonts.ptx
%{_texmfdistdir}/tex/plain/pitex/pitex.tex
%{_texmfdistdir}/tex/plain/pitex/sections.ptx
%doc %{_texmfdistdir}/doc/plain/pitex/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
