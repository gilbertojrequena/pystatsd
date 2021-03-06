import os
import re
from setuptools import find_packages, setup


setup(
    name='statsd-influx-tags',
    version='1.0.0',
    description='A simple statsd client with influx tag support.',
    long_description=open('README.rst').read(),
    author='Gilberto J Requena',
    author_email='gilbertojrequena@gmail.com',
    url='https://github.com/gilbertojrequena/pystatsd-telegraf-tags',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['README.rst']},
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
