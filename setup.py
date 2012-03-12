# encoding: utf-8
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='urlparse2',
    version='1.0',
    description='urlparse for humans.',
    long_description='A drop-in replacement for urlparse with enhancements.'
        'Provides mutable ParseResult fields and error handling for invalid'
        'domains passed to urljoin.',
    author='Matthew Hooker, Jeremy Avnet, Matt Chisholm',
    author_email="mwhooker@gmail.com",
    url='https://github.com/mwhooker/urlparse2',
    install_requires=['recordtype'],
    license='MIT',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
