%define upstream_name    Template-Plugin-Latex
%define upstream_version 3.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	LaTeX plugin for the Template Toolkit
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(LaTeX::Driver)
BuildRequires:	perl(LaTeX::Encode)
BuildRequires:	perl(LaTeX::Table)
BuildRequires:	perl(Template)
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Moose::Policy) perl(Moose)
BuildRequires:	perl(Class::MOP)
BuildRequires:	perl(Sub::Identify)
BuildRequires:	perl(Devel::GlobalDestruction)
BuildRequires:	perl(Sub::Name)
BuildArch:	noarch

%description
The Template::Latex module is a wrapper of convenience around the Template
module, providing additional support for generating PDF, PostScript and DVI
documents from LaTeX templates.

You use the Template::Latex module exactly as you would the Template
module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README README README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 3.20.0-2mdv2011.0
+ Revision: 658882
- rebuild for updated spec-helper

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 3.20.0-1mdv2010.0
+ Revision: 401606
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 3.02-2mdv2010.0
+ Revision: 375898
- rebuild

* Sat Apr 11 2009 Olivier Thauvin <nanardon@mandriva.org> 3.02-1mdv2009.1
+ Revision: 366351
- buildrequires
- import perl-Template-Plugin-Latex


* Sat Apr 11 2009 cpan2dist 3.02-1mdv
- initial mdv release, generated with cpan2dist

