%define	pdir	Getopt
%define	pnam	Declare
%include	/usr/lib/rpm/macros.perl
Summary:	Getopt-Declare perl module
Summary(pl):	Modu� perla Getopt-Declare
Name:		perl-Getopt-Declare
Version:	1.09
Release:	3

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Parse-RecDescent
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt-Declare is yet another command-line argument parser, one which
is specifically designed to be powerful but exceptionally easy to use.

%description -l pl
Getopt-Declare jest jeszcze jednym parserem argument�w linii polece�,
o wielkich mozliwo�ciach, a jednocze�nie wyj�tkowo �atwym w u�yciu.

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
