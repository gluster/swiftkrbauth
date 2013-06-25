#!/bin/bash

tar -cz --exclude=.svn -f ~/rpmbuild/SOURCES/swiftkerbauth.tar.gz swiftkerbauth

rpmbuild --target noarch --clean -bb swiftkerbauth.spec

rm ~/rpmbuild/SOURCES/swiftkerbauth.tar.gz
