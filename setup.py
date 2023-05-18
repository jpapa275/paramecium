from setuptools import setup, find_packages

setup(
    name='csv_to_db',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pandas',
        'sqlalchemy'
    ],
    entry_points={
        'console_scripts': [
            'csv_to_db = csv_to_db:main',
        ],
    },
)