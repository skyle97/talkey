import sys
from setuptools import setup, find_packages

def get_version(fname):
    import re
    verstrline = open(fname, "rt").read()
    mo = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", verstrline, re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError("Unable to find version string in %s." % (fname,))

def get_requirements():
    requirements = [
        'langid',
        'requests',
        'audioread',
    ]
    if sys.version_info[0] == 2:
        requirements.append('subprocess32')
    return requirements

def get_test_requirements():
    requirements = [
        'gtts',
    ]
    return requirements

setup(
    name='talkey',
    version=get_version('talkey/__init__.py'),
    description='Simple Test-To-Speech (TTS) interface library with multi-language and multi-engine support.',
    long_description=open('README.rst').read(),
    author='Nickolas Grigoriadis',
    author_email='nagrigoriadis@gmail.com',
    url='https://github.com/grigi/talkey',
    zip_safe=False,
    test_suite='talkey.test_suite',

    # Dependencies
    install_requires=get_requirements(),
    tests_require=get_test_requirements(),

    # Packages
    packages=find_packages(),
    include_package_data=True,

    # Scripts
    scripts=[],

    # Classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft Windows',
        'Operating System :: POSIX :: Linux',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
    ]
)
