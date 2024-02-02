from setuptools import setup, find_packages

setup(
    name='oidc',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
        'djangorestframework>=3.12',
    ]
)