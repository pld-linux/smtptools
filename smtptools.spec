Summary:	smtptools - tools for the Simple Mail Transfer Protocol
Summary(pl):	Narzêdzia do przesy³ania poczty poprzez SMTP
Name:		smtptools
Version:	0.2.3
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	ftp://ftp.ohse.de/uwe/releases/%{name}-%{version}.tar.gz
# Source0-md5:	16dd9da7b1b9c7462f207695ae323034
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This collection of commands contains tools to send and receive
messsages with SMTP.

%description -l pl
To jest kolekcja komend pozwalaj±cych na wysy³anie i odbieranie
wiadomo¶ci poprzez SMTP.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README README.smtpblast README.usmtpd
%doc README.tomaildir README.cvs
%attr(755,root,root) %{_sbindir}/usmtpd
%attr(755,root,root) %{_bindir}/tomaildir
%attr(755,root,root) %{_bindir}/maildirblast
%attr(755,root,root) %{_bindir}/smtpblast
%{_mandir}/man1/*
