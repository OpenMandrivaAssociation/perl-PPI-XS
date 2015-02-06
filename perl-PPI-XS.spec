%define upstream_name    PPI-XS
%define upstream_version 0.902

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    (Minor) XS acceleration for PPI
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/PPI/PPI-XS-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(PPI)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc   Changes
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.901.0-6
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Thu Jul 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.901.0-5mdv2011.0
+ Revision: 556773
- rebuild
- rebuild
- rebuild for perl 5.12
- rebuild for perl 5.12

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.901.0-3mdv2011.0
+ Revision: 551273
- rebuild using %%perl_convert_version

* Thu May 14 2009 Jérôme Quelin <jquelin@mandriva.org> 0.901-2mdv2010.0
+ Revision: 375699
- rebuild

* Thu May 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.901-1mdv2010.0
+ Revision: 372939
- import perl-PPI-XS


* Thu May 07 2009 cpan2dist 0.901-1mdv
- initial mdv release, generated with cpan2dist


