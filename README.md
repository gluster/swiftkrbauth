swiftkerbauth
=============

Kerberos Authentication filter for Openstack Swift
--------------------------------------------------

Carsten Clasohm implemented a new authentication filter for swift
that uses Kerberos tickets for single sign on authentication, and
grants administrator permissions based on the user's group membership
in a directory service like Red Hat Enterprise Linux Identity Management
or Microsoft Active Directory.

Table of Contents
-----------------

1. [Architecture](doc/architecture.md)
2. [IPA Server Guide](doc/ipa_server.md)
3. [IPA Client Guide](doc/ipa_client.md)
4. [Swiftkerbauth Guide](doc/swiftkerbauth_guide.md)
