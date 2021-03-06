from setuptools import find_packages, setup


setup(
    name='mypythonlib',
    packages=find_packages(include=['mypythonlib']),
    version='0.2.0',
    description='My first Python library',
    author='Me',
    license='MIT',
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.5'],
    test_suite='tests',
)