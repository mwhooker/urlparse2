# encoding: utf-8
import os.path
import subprocess
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def version():
    cwd = os.path.dirname(os.path.abspath(__file__))
    p = subprocess.Popen('git log --oneline | wc -l',
                         stdout=subprocess.PIPE,
                         cwd=cwd, shell=True)
    lines = int(p.communicate()[0].strip())

    return "0." + "9" * lines


setup(
    name='urlparse2',
    version=version(),
    description='urlparse for humans.',
    author="Hooker Avnet Chisholm Toshi0, GmBH",
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
