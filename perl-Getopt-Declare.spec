#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	Declare
Summary:	Getopt::Declare - Declaratively Expressed Command-Line Arguments via Regular Expressions
Summary(pl):	Getopt::Declare - wyra¿one deklaracyjnie przez wyra¿enia regularne argumenty linii polecenia
Name:		perl-Getopt-Declare
Version:	1.11
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2bbc6f770af28d5b9511be071a9ab03e
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Parse-RecDescent
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt::Declare is yet another command-line argument parser, one which
is specifically designed to be powerful but exceptionally easy to use.

%description -l pl
Getopt::Declare jest jeszcze jednym parserem argumentów linii poleceñ,
o wielkich mozliwo¶ciach, a jednocze¶nie wyj±tkowo ³atwym w u¿yciu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install demo* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Getopt/Declare.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
