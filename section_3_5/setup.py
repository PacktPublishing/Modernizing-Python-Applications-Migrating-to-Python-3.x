from setuptools import setup

setup(
   name='mymodule',
   version='0.0.1',
   description='A very useful module for my code',
   author='Lorem Ipsum',
   author_email='li@example.com',
   packages=['mymodule'],
   install_requires=[],
   python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',
   tests_require=['pytest']
)
