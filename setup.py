#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='django-oscar-demo',
    version='0.1.0',
    url='https://github.com/django-oscar/django-oscar-demo',
    author="David Winterbottom",
    author_email="david.winterbottom@gmail.com",
    description="Demo site for Django Oscar",
    long_description=open('README.rst').read(),
    keywords="E-commerce, Django, domain-driven",
    license='BSD',
    platforms=['linux'],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=[
        'django==1.8.8',
        'django-oscar==1.1.1',
        'django-oscar-paypal==0.9.1',
        'django-oscar-datacash==0.8.3',
        'django-oscar-stores',

    ],
    dependency_links=[],
    classifiers=[],
)
