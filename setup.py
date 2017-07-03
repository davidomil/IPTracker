from distutils.core import setup

requirements = ["pygeoip"]

setup(
    name='IPTracker',
    version='1.0.0',
    packages=['iptracker'],
    url='https://github.com/davidomil/IPTracker',
    license='LICENSE.txt',
    author='David Miler',
    author_email='david@orrisystems.com',
    long_description=open('README.md').read(),
    requires=requirements,
    include_package_data=True,
    description='Utility to track IP change in realtime'
)
