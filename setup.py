"""Setup for pywave2"""

from setuptools import setup, find_packages

setup(
    name='pywave2',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'lxml',
        'requests'
    ],
    entry_points={
        'console_scripts':
            'pywave2=pywave2.pywave2:main'
    }
)
