Name:		swiftkerbauth
Version:    	1.0
Release:    	1
Summary:    	Kerberos authentication filter for Swift

Group:	    	System Environment/Base
License:    	GPL
Source:	    	%{name}.tar.gz
BuildRoot:  	%{_tmppath}/%{name}-root

Requires:	gluster-swift >= 1.4.8
Requires:	python-webob1.0 >= 1.0.8

%description
Python script which implements an authentication filter for Swift, the
object-level access layer of Red Hat Storage.

Relies on an external authentication server, which comes with the
apachekerbauth package.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p \
  $RPM_BUILD_ROOT/usr/lib/python2.6/site-packages

install swiftkerbauth.py \
  $RPM_BUILD_ROOT/usr/lib/python2.6/site-packages

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/lib/python2.6/site-packages/swiftkerbauth.py

%post
if ! grep -q "filter:kerbauth" /etc/swift/proxy-server.conf; then
cat >>/etc/swift/proxy-server.conf <<EOF

[filter:kerbauth]
paste.filter_factory = swiftkerbauth:filter_factory
ext_authentication_url = http://AUTHENTICATION_SERVER/cgi-bin/swift-auth
EOF
fi

%changelog
* Fri Apr  5 2013 Carsten Clasohm <clasohm@redhat.com> - 1.0-1
- initial build
