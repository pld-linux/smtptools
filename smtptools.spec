Summary:	smtptools - tools for the Simple Mail Transfer Protocol
Summary(pl):	narzędzia do przesyłania poczty poprzez SMTP
Name:		smtptools
Version:	0.2.3
Release:	1
Copyright:	GPL
Group:		Applications/Communications
Group(pl):      Aplikacje/Komunikacja
Source:		ftp://ftp.ohse.de/uwe/releases/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This collection of commands contains tools to send and receive
messsages with SMTP.

%description -l pl
To jest kolekcja komand pozwalających na wysyłanie i odbieranie
wiadomości poprzez SMTP.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS ChangeLog NEWS README README.smtpblast README.usmtpd \
	README.tomaildir README.cvs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,README.smtpblast,README.usmtpd}.gz
%doc {README.tomaildir,README.cvs}.gz
%attr(755,root,root) %{_sbindir}/usmtpd
%attr(755,root,root) %{_bindir}/tomaildir
%attr(755,root,root) %{_bindir}/maildirblast
%attr(755,root,root) %{_bindir}/smtpblast
%{_mandir}/man1/*
