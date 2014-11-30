#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	XML
%define		pnam	Filter-Glossary
%include	/usr/lib/rpm/macros.perl
Summary:	XML::Filter::Glossary - SAX2 filter for keyword lookup and replacement
Summary(pl.UTF-8):	XML::Filter::Glossary - filtr SAX2 do poszukiwania i zastępowania słów kluczowych
Name:		perl-XML-Filter-Glossary
Version:	0.2
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	04427a14f8e10e24e9f725439925048d
URL:		http://search.cpan.org/dist/XML-Filter-Glossary/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-SAX >= 0.11
BuildRequires:	perl-XML-SAX-Machines >= 0.38
BuildRequires:	perl-XML-SAX-Writer >= 0.44
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is modelled after the UserLand glossary system where
words, or phrases, wrapped in double-quotes are compared against a
lookup table and are replaced by their corresponding entries.

%description -l pl.UTF-8
Ten pakiet jest modelowany w oparciu o system słownikowy UserLand, w
którym słowa lub frazy umieszczone w cudzysłowach są porównywane z
tablicą wyszukiwania i zastępowane odpowiadającymi im wpisami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/XML/*/*
%{_mandir}/man3/*
