from setuptools import setup
from setuptools.command.install import install

setup(
    name='vespucci',
    version='1.0.0',
    description='A lightweight visualizer for relational databases',
    long_description=open('README.md').read(),
    author='Axel Hadfeg',
    packages=['vespucci'],
    license='GPLv2',
    package_data={'': ['*.json']},
    scripts=['scripts/vespucci'],
    install_requires=[
	'networkx',
	'matplotlib',
	'mysql-connector-python-rf',
    ],
)
