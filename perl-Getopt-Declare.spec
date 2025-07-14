#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Getopt
%define		pnam	Declare
Summary:	Getopt::Declare - Declaratively Expressed Command-Line Arguments via Regular Expressions
Summary(pl.UTF-8):	Getopt::Declare - wyrażone deklaracyjnie przez wyrażenia regularne argumenty linii polecenia
Name:		perl-Getopt-Declare
Version:	1.14
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7ed52d0279abcb34c366369af8ac8cb8
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Getopt-Declare/
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt::Declare is yet another command-line argument parser, one which
is specifically designed to be powerful but exceptionally easy to use.

%description -l pl.UTF-8
Getopt::Declare jest jeszcze jednym parserem argumentów linii poleceń,
o wielkich możliwościach, a jednocześnie wyjątkowo łatwym w użyciu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

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

cp -p demos/demo* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Getopt/Declare.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
