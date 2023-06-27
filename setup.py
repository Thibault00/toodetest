from setuptools import setup, find_packages

setup(
    name='toodetest',
    version='0.1.0',
    author='Thibault Jaigu',
    author_email='thibault.jaigu@gmail.com',
    description='Toodetest Library',
    long_description='A library for tracking prompts and responses for Project 1.',
    url='https://github.com/Thibault00/toodetest',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
