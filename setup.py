#!/usr/bin/env python

from setuptools import setup
from swiftkerbauth import __version__

setup(
    name='swiftkerbauth',
    version=__version__,
    description='Kerberos authentication filter for Openstack Swift',
    license='Apache License (2.0)',
    author='Red Hat, Inc.',
    author_email='gluster-users@gluster.org',
    url='https://forge.gluster.org/swiftkerbauth',
    packages=['swiftkerbauth'],
    keywords='openstack swift kerberos',
    install_requires=['swift>=1.9.1'],
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
    data_files=[
        ('/var/www/cgi-bin', ['apachekerbauth/var/www/cgi-bin/swift-auth']),
        ('/etc/httpd/conf.d', ['apachekerbauth/etc/httpd/conf.d/swift-auth.conf']),
        ],
    entry_points={
        'paste.filter_factory': [
            'kerbauth=swiftkerbauth.kerbauth:filter_factory',
            ],
        },
    )
