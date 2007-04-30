#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Template
%define	pnam	Provider-Encoding
Summary:	Template::Provider::Encoding - Explicitly declare encodings of your templates
#Summary(pl.UTF-8):	
Name:		perl-Template-Provider-Encoding
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Template/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a2af735582d141d49810f1ede78d4da3
URL:		http://search.cpan.org/dist/Template-Provider-Encoding/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Template-Toolkit >= 2.1
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

# %description -l pl.UTF-8
# TODO

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
