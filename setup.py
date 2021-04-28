import os,sys
from setuptools import setup,find_packages
sys.path.insert(0, os.path.abspath('lib'))
#from library import __version__, __author__
#print (__version__)
with open("README.md", "r") as file:
  long_description = file.read()

with open("CHANGES.md", "r") as file:
  changes = file.read()

setup(
	name='netkiller-logging',
	#version=__version__,
	version='0.0.5',
	#author=__author__,
	author_email='netkiller@msn.com',
	description="log send to remote",
	long_description=long_description + '\n\n' + changes,
	long_description_content_type="text/markdown",
	keywords='logging',

	url='http://netkiller.github.io',
	download_url='https://github.com/netkiller/logging',
	license='BSD',
	classifiers=[
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.4',
	],
	#py_modules=[
	#	'library.rsync',
	#	'library.whiptail'
	#],
	
	#package_dir={ '': 'src' },
	packages=find_packages(),
	scripts=[
		'bin/auditlog',
		'bin/rlog',
		'bin/collection',
		'bin/cisco'
	],
	data_files = [
		('etc', ['etc/auditlog.ini']),
		('etc', ['etc/logging.ini']),
		#('log', ['log/auditlog.log']),
		('share', ['share/dmesg.reg']),
		('etc', ['etc/cisco.conf']),
		('libexec', ['libexec/switch.exp', 'libexec/route.exp'])
	]
)
