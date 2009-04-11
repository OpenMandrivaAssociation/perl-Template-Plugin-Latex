
%define realname   Template-Plugin-Latex
%define version    3.02
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    LaTeX plugin for the Template Toolkit
Source:     http://www.cpan.org/modules/by-module/Template/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(LaTeX::Driver)
BuildRequires: perl(LaTeX::Encode)
BuildRequires: perl(LaTeX::Table)
BuildRequires: perl(Template)

BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

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


