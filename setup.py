#!/usr/bin/env python

# Copyright (c) 2013 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup
import os

__version__ = '1.0.0'

with open('README.md') as file:
    long_description = file.read()


# Ugly hack to exclude data_files if running in tox as non root
def include_data_files():
    data = [
        ('/var/www/cgi-bin',
            ['apachekerbauth/var/www/cgi-bin/swift-auth']),
        ('/etc/httpd/conf.d',
            ['apachekerbauth/etc/httpd/conf.d/swift-auth.conf']),
    ]
    if os.geteuid() != 0:
        data = None
    return data


setup(
    name='swiftkerbauth',
    version=__version__,
    description='Kerberos authentication filter for Openstack Swift',
    license='Apache License (2.0)',
    author='Red Hat, Inc.',
    author_email='gluster-users@gluster.org',
    long_description=long_description,
    url='https://github.com/gluster/swiftkrbauth/',
    packages=['swiftkerbauth'],
    keywords='openstack swift kerberos',
    install_requires=['swift>=1.10.0'],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: OpenStack',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    data_files=include_data_files(),
    entry_points={
        'paste.filter_factory': [
            'kerbauth=swiftkerbauth.kerbauth:filter_factory',
        ],
    },
)
