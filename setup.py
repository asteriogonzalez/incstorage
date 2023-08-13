#!/usr/bin/env python

"""The setup script."""

# export DISTUTILS_DEBUG=True

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements/base.txt') as requirements_file:
    requirements = requirements_file.readlines()

with open('requirements/testing.txt') as dev_requirements_file:
    dev_requirements = dev_requirements_file.readlines()
    dev_requirements.extend(requirements)

# https://docs.python.org/3/distutils/setupscript.html
setup(
    author="Asterio Gonzalez",
    author_email='asterio.gonzalez@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    description="Incremental Storage",
    entry_points={
        'console_scripts': [
            'incstorage=incstorage.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='incstorage',
    name='incstorage',
    packages=find_packages(include=['incstorage', 'incstorage.*']),
    test_suite='tests',
    tests_require=dev_requirements,
    url='https://github.com/asterio.gonzalez/incstorage',
    version='0.1.0',
    zip_safe=False,
)
