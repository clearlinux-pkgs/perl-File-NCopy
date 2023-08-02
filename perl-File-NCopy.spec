#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-File-NCopy
Version  : 0.36
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/File-NCopy-0.36.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/File-NCopy-0.36.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-ncopy-perl/libfile-ncopy-perl_0.36-2.debian.tar.xz
Summary  : Deprecated module. Use File::Copy::Recursive instead. Copy file, file. Copy file[s] | dir[s], dir
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-NCopy-license = %{version}-%{release}
Requires: perl-File-NCopy-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the perl-File-NCopy package.
Group: Development
Provides: perl-File-NCopy-devel = %{version}-%{release}
Requires: perl-File-NCopy = %{version}-%{release}

%description dev
dev components for the perl-File-NCopy package.


%package license
Summary: license components for the perl-File-NCopy package.
Group: Default

%description license
license components for the perl-File-NCopy package.


%package perl
Summary: perl components for the perl-File-NCopy package.
Group: Default
Requires: perl-File-NCopy = %{version}-%{release}

%description perl
perl components for the perl-File-NCopy package.


%prep
%setup -q -n File-NCopy-0.36
cd %{_builddir}
tar xf %{_sourcedir}/libfile-ncopy-perl_0.36-2.debian.tar.xz
cd %{_builddir}/File-NCopy-0.36
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-NCopy-0.36/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-NCopy
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-NCopy/05eed01407d02f3b247b8de9f02ba574a41bb0f6 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::NCopy.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-NCopy/05eed01407d02f3b247b8de9f02ba574a41bb0f6

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
