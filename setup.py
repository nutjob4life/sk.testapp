# encoding: utf-8

from codecs import open
from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    readme = f.read()

requirements = [
    'setuptools',
]

setup(
    name='sk.testapp',
    version='0.0.0',
    description="Test App for Packaging",
    long_description=readme,
    author=u'Sean Kelly',
    author_email=u'kelly@seankelly.biz',
    packages=find_packages(exclude=['docs']),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': ['testapp=sk.testapp.main:main']
    },
    package_data={
        '': ['*.txt', '*.rst']
    },
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
    ]
)
