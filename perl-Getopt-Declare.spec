%include	/usr/lib/rpm/macros.perl
Summary:	Getopt-Declare perl module
Summary(pl):	Modu³ perla Getopt-Declare
Name:		perl-Getopt-Declare
Version:	1.08
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Getopt/Getopt-Declare-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Parse-RecDescent
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt-Declare is yet another command-line argument parser, one which
is specifically designed to be powerful but exceptionally easy to use.

%description -l pl
Getopt-Declare jest jeszcze jednym parserem argumentów linii poleceñ,
o wielkich mozliwo¶ciach, a jednocze¶nie wyj±tkowo ³atwym w u¿yciu.

%prep
%setup -q -n Getopt-Declare-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install demo* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Getopt/Declare.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
