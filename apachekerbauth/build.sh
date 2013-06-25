#!/bin/bash

tar -cz --exclude=.svn -f ~/rpmbuild/SOURCES/apachekerbauth.tar.gz apachekerbauth

rpmbuild --target noarch --clean -bb apachekerbauth.spec

rm ~/rpmbuild/SOURCES/apachekerbauth.tar.gz
