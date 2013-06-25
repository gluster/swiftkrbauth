Name:		apachekerbauth
Version:    	1.0
Release:    	3
Summary:    	Kerberos authentication filter for Swift

Group:	    	System Environment/Base
License:    	GPL
Source:	    	%{name}.tar.gz
BuildRoot:  	%{_tmppath}/%{name}-root

Requires:	httpd >= 2.2.15
Requires:	mod_auth_kerb >= 5.4

%description
Python CGI script which is used by the swiftkerbauth package to
authenticate client requests using Kerberos.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p \
  $RPM_BUILD_ROOT/etc/httpd/conf.d \
  $RPM_BUILD_ROOT/var/www/cgi-bin

install -m 644 etc/httpd/conf.d/* \
  $RPM_BUILD_ROOT/etc/httpd/conf.d

install -m 644 var/www/cgi-bin/memcached.py \
  $RPM_BUILD_ROOT/var/www/cgi-bin

install var/www/cgi-bin/swift-auth \
  $RPM_BUILD_ROOT/var/www/cgi-bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config /etc/httpd/conf.d/swift-auth.conf
/var/www/cgi-bin/memcached.py
/var/www/cgi-bin/swift-auth

%changelog
* Fri Apr  5 2013 Carsten Clasohm <clasohm@redhat.com> - 1.0-1
- initial build
