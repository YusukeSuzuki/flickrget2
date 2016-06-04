from setuptools import setup, find_packages

setup(
    name = 'flickrget',
    version = 0.1,
    packages = find_packages(),
    scripts = ['bin/flickrget'],
    install_requires = ['appdirs', 'PyYAML', 'flickrapi', 'requests']
)

