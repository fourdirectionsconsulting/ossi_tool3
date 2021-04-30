from setuptools import setup
import re

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('ossi_tool3/ossit.py').read(),
    re.M
    ).group(1)

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


def readme():
    """ Long description from readme file"""
    with open('README.rst') as f:
        return f.read()

setup(name='ossi_tool3',
      version=version,
      description='Avaya SAT (Communication Manager Site Administration Tool) python emulator, to generate CSV file from command output',
      long_description=long_descr,
      long_description_content_type='text/plain',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Telecommunications Industry',
        'Topic :: Communications :: Telephony',
        'License :: OSI Approved :: ISC License (ISCL)'
        ],
      url='https://github.com/deesnow/ossi_tool3',
      author='Janos Tarjanyi',
      author_email='janos.tarajnyi@gmail.com',
      license='ISC',
      packages=['ossi_tool3'],
      entry_points={
        "console_scripts": ['ossi_tool3 = ossi_tool3.ossit:main']
        },
      install_requires=['pexpect'],
      zip_safe=False)
