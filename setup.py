from setuptools import setup
from fbaas import VERSION

setup(
    name='fbaas',
    version=VERSION,
    packages=[
        'fbaas'
    ],
    install_requires=[],
    include_package_data=True,
    scripts=[
        'bin/wsgi.py'
    ],
    zip_safe=False,
    author="Rob Lyon",
    author_email="rlyon@kochava.com",
    description="Fizz Buzz Interface API",
    license="AGPLv3",
    url="https://miniproject.ops.kochava.com/miniproject/fbaas",
)
