from setuptools import setup, find_packages

setup(
    name = 'JMaths',
    version = '0.3.2',  # Bump this
    packages = find_packages(),
    install_requires=[
        'pandas',
        'openpyxl',
    ]
)