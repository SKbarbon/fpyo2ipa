from setuptools import setup, find_packages

setup(
    name='fpyo2ipa',
    version='1.0',
    author='SKbarbon',
    description='A package tool that allow you to built a python iOS apps with flet UI.',
    long_description="https://github.com/SKbarbon/fpyo2ipa",
    url='https://github.com/SKbarbon/fpyo2ipa',
    install_requires=["briefcase"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ],
)