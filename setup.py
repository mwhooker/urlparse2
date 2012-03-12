
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='urlparse2',
    version='1.0',
    description='urlparse for humans.',
    author="Hooker Avnet Chisholm Toshi0, GmBH",
    url='https://github.com/mwhooker/urlparse2',
    install_requires=[
        'recordtype',
    ],
    license='MIT',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: <= 3.9',
    ),
)
