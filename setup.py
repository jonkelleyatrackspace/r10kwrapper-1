from setuptools import setup
from sys import path

path.insert(0, '.')

NAME = "r10kwrapper"

if __name__ == "__main__":

    setup(
        name = NAME,
        version = "0.3.1",
        author = "Jon Kelley",
        author_email = "jon.kelley@rackspace.com",
        url = "https://github.com/jonkelleyatrackspace/r10kwrapper",
        license = 'Apache License Version 2.0',
        packages = [NAME],
        package_dir = {NAME: NAME},
        description = "r10kwrapper - a wrapper for r10k",
        entry_points={
            'console_scripts': [ 'r10kwrapper = r10kwrapper.r10kwrapper:main' ],
        }
    )

