from setuptools import setup

# read the contents of markdown README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='raspiGPIOext',
    url='https://github.com/nerdstoke/raspiGPIOext',
    author='Thomas Cannon',
    author_email='nerdstoke@gmail.com',
    packages=['raspiGPIOext'],
    install_requires=['gpiozero>=1.5.1'],
    version='0.1',
    license='MIT',
    description='An example of a python package from pre-existing code',
    long_description=long_description,
    long_description_content_type='text/markdown',
)