import sys
from setuptools import setup, find_packages


with open("requirements.txt") as f:
    deps = [
        dep
        for dep in f.read().split("\n")
        if dep.strip() != "" and not dep.startswith("-e")
    ]
    install_requires = deps


setup(
    name='Calculator service',
    version='1.0',
    description='REST API calculator using python and quart',
    author='Luke Gregory',
    author_email='lukewgregory@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
