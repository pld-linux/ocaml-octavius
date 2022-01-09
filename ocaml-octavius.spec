#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Octavius - ocamldoc comment syntax parser
Summary(pl.UTF-8):	Octavius - parser składni komentarzy ocamldoc
Name:		ocaml-octavius
Version:	1.2.2
Release:	1
License:	ISC
Group:		Libraries
#Source0Download: https://github.com/ocaml-doc/octavius/releases
Source0:	https://github.com/ocaml-doc/octavius/archive/v%{version}/octavius-%{version}.tar.gz
# Source0-md5:	72f9e1d996e6c5089fc513cc9218607b
URL:		https://github.com/ocaml-doc/octavius
BuildRequires:	ocaml >= 1:4.03.0
BuildRequires:	ocaml-dune >= 1.11
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Octavius is a library to parse the ocamldoc comment syntax.

This package contains files needed to run bytecode executables using
octavius library.

%description -l pl.UTF-8
Octavius to biblioteka do analizy składni komentarzy ocamldoc.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki octavius.

%package devel
Summary:	Octavius - ocamldoc comment syntax parser - development part
Summary(pl.UTF-8):	Octavius - parser składni komentarzy ocamldoc - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
octavius library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki octavius.

%prep
%setup -q -n octavius-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/octavius/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/octavius

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%attr(755,root,root) %{_bindir}/octavius
%dir %{_libdir}/ocaml/octavius
%{_libdir}/ocaml/octavius/META
%{_libdir}/ocaml/octavius/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/octavius/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/octavius/*.cmi
%{_libdir}/ocaml/octavius/*.cmt
%{_libdir}/ocaml/octavius/*.cmti
%{_libdir}/ocaml/octavius/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/octavius/octavius.a
%{_libdir}/ocaml/octavius/*.cmx
%{_libdir}/ocaml/octavius/*.cmxa
%endif
%{_libdir}/ocaml/octavius/dune-package
%{_libdir}/ocaml/octavius/opam
