import setuptools
from distutils.core import setup

with open("README.md", 'r', encoding='utf-8') as f:
    long_desc = f.read()

setup(
    name="pytools",
    version="0.0.1",
    description="Some Python Tools.",
    long_description=long_desc,
    author="QWERDF007",
    author_email="595517713@qq.com",
    url="https://github.com/QWERDF007/Pytools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
