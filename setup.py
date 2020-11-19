from setuptools import setup, find_packages

setup(
    name='homo',
    version='2020.11.18.1',
    description='Homo',
    author='Sebastian Obara',
    author_email='obara.sebastian@gmail.com',
    package_data={},
    dependency_links=[

    ],
    install_requires=[
        'requests == 2.25.0',
        'tldextract == 3.0.2',
        'idna == 2.10',
        'pysocks == 1.7.1'
    ],
)
