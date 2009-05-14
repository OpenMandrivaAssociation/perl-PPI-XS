
%define realname   PPI-XS
%define version    0.901
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    (Minor) XS acceleration for PPI
Source:     http://www.cpan.org/modules/by-module/PPI/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(PPI)
BuildRequires: perl(Test::More)



%description
PPI::XS provides XS-based acceleration of the core PPI packages. It
selectively replaces a (small but growing) number of methods throughout PPI
with identical but much faster C versions.

Once installed, it will be auto-detected and loaded in by PPI completely
transparently.

Because the C implementations are linked to the perl versions of the same
function, it is preferable to upgrade PPI::XS any time you do a major
upgrade of PPI itself.

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
%doc LICENSE README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


