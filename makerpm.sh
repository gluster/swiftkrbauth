#!/bin/sh

# Creates swiftkerbauth RPMs in dist/

rm -rf dist/ swiftkerbauth.egg-info/ build/
python setup.py bdist_rpm --requires="httpd >= 2.2.15, mod_auth_kerb >= 5.4"
rm -rf swiftkerbauth.egg-info/ build/
echo "RPMS are now available in $PWD/dist/"
