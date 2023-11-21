from setuptools import setup, find_packages
import codecs
import os


LONG_DESCRIPTION = 'A CLI tool for quickly ecoding/decoding simple ciphers for CTF challenges.'

setup(
    name='pypher',
    version='0.1.0',
    author='mank (Manomay Kagalkar)',
    author_email='nominal_grabs0r@icloud.com',
    description='A CLI tool for ciphers',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    install_requires=[
        'typer',
    ],
    packages=find_packages(),
    keywords=['ciphers', 'ctf', 'cli'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: CLI Users',
        'Topic :: Utilities',
        'License :: Unlicense',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'pypher=pypher.__main__:app',
        ],
    },
)
