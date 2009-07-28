%define upstream_name    Template-Plugin-Latex
%define upstream_version 3.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    LaTeX plugin for the Template Toolkit
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(LaTeX::Driver)
BuildRequires: perl(LaTeX::Encode)
BuildRequires: perl(LaTeX::Table)
BuildRequires: perl(Template)
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Moose::Policy) perl(Moose)
BuildRequires: perl(Class::MOP)
BuildRequires: perl(Sub::Identify)
BuildRequires: perl(Devel::GlobalDestruction)
BuildRequires: perl(Sub::Name)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Template::Latex module is a wrapper of convenience around the Template
module, providing additional support for generating PDF, PostScript and DVI
documents from LaTeX templates.

You use the Template::Latex module exactly as you would the Template
module.

    my $tt = Template::Latex->new(\%config);
    $tt->process($input, \%vars, $output)
        || die $t->error();

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README README README Changes
%{_mandir}/man3/*
%perl_vendorlib/*

