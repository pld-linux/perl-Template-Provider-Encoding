#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Template
%define	pnam	Provider-Encoding
Summary:	Template::Provider::Encoding - Explicitly declare encodings of your templates
Summary(pl.UTF-8):	Template::Provider::Encoding - jawne określanie kodowań szablonów
Name:		perl-Template-Provider-Encoding
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Template/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fddbc7b4c2033d931932880149cab323
URL:		http://search.cpan.org/dist/Template-Provider-Encoding/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Template-Toolkit >= 2.1
BuildRequires:	perl-Encode
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Template::Provider::Encoding is a Template Provider subclass to decode
template using its declaration. You have to declare encoding of the
template in the head (1st line) of template using (fake) encoding TT
plugin. Otherwise the template is handled as utf-8.

  [% USE encoding 'utf-8' %]
  Here comes utf-8 strings with [% variable %].

%description -l pl.UTF-8
Template::Provider::Encoding to podklasa Template Provider dekodująca
szablony przy użyciu ich deklaracji. Trzeba zadeklarować kodowanie
szablonu w jego nagłówku (1. linii) przy użyciu (fałszywej) wtyczki
kodowania TT. W przeciwnym wypadku szablon jest obsługiwany jako
utf-8. Przykład:

  [% USE encoding 'utf-8' %]
  Tutaj tekst w utf-8 ze [% zmiennymi %].

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
%doc Changes
%{perl_vendorlib}/Template/*/*.pm
%{_mandir}/man3/*
