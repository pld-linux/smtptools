Summary: smtptools - tools for the Simple Mail Transfer Protocol
Name: smtptools
Version: 0.2.2
Release: 0
Copyright: GPL
Group: Applications/Communications
Source: ftp://ftp.ohse.de/uwe/releases/smtptools-0.2.2.tar.gz
BuildRoot: /var/tmp/smtptools-root

%description
This collection of commands contains tools to send and receive
messsages with SMTP.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr install

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README README.smtpblast README.usmtpd README.tomaildir README.cvs README.systems
/usr/sbin/usmtpd
/usr/bin/tomaildir
/usr/bin/maildirblast
/usr/bin/smtpblast
/usr/man/man1/smtpblast.1
/usr/man/man1/usmtpd.1
/usr/man/man1/maildirblast.1
/usr/man/man1/tomaildir.1

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Dec 21 1998 Uwe Ohse <uwe@ohse.de>
- stole redhats specfile and hacked it.
  Redhat people: "Upgraded to 0.12.14 and changed makefiles so 
  gettext isnt built." is that kind of problem the author would
  have liked to know.

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups 

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Wed Mar 5 1997 msf@redhat.com <Michael Fulbright>
- Upgraded to 0.12.14 and changed makefiles so gettext isnt built.
