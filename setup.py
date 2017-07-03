from setuptools import setup, find_packages

requirements = ["pygeoip"]

setup(
    name='IPTracker',
    version='1.0.0',
    url='https://github.com/davidomil/IPTracker',
    license='LICENSE.txt',
    author='David Miler',
    author_email='david@orrisystems.com',
    long_description=open('README.md').read(),
    include_package_data=True,
    description='Utility to track public IP change in realtime',
    packages=find_packages(exclude=['examples', 'tests']),
    py_modules=['iptracker'],
    entry_points={
        'console_scripts': [
            'public_ip_tracker = iptracker:startup',
        ]
    },
    platforms='any',
    install_requires=requirements
)
