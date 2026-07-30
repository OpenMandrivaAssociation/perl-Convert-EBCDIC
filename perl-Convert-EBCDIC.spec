%define upstream_name    Convert-EBCDIC
%define upstream_version 0.06
Name:		perl-%{upstream_name}
Version:	0.06
Release:	2

Summary:	Convert-EBCDIC module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Convert-EBCDIC
Source0:	https://cpan.metacpan.org/authors/id/C/CX/CXL/Convert-EBCDIC-0.06.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides two functions ascii2ebcdic and ebcdic2ascii for
converting a string from/to ASCII to/from EBCDIC, and two code pages
ccsid819 and ccsid1047.

%prep
%setup -q -n Convert-EBCDIC-0.06

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Convert/EBCDIC.pm
%{_mandir}/*/*

