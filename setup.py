#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''
A tool to count soft-clipped reads in a bam file.
'''

setup(
    name='breakpoint_counter',
    version='0.0.1',
    author='Khalid Mahmood',
    author_email='khalid.mahmood@unimelb.edu.au',
    packages=['breakpoint_counter'],
    package_dir={'breakpoint_counter': 'breakpoint_counter'},
    entry_points={
        'console_scripts': ['breakpoint_counter = breakpoint_counter.breakpoint_counter:main']
    },
    url='https://github.com/khalidm/breakpoint_counter',
    license='LICENSE',
    description=('Count soft-clipped reads in a bam file by position'),
    long_description=(LONG_DESCRIPTION),
    install_requires=["pysam"]
)
