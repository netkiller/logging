import os,sys
from distutils.core import setup
sys.path.insert(0, os.path.abspath('lib'))
#from library import __version__, __author__
#print (__version__)
readme = open('README.md').read()
changes = open('CHANGES.md').read()

setup(
	name='logging',
	#version=__version__,
	#author=__author__,
	version='0.0.2',
	description="log send to remote",
	long_description=readme + '\n\n' + changes,
	keywords='logging',
	author_email='netkiller@msn.com',
	url='http://netkiller.github.io',
	download_url='https://github.com/netkiller/logging',
	license='BSD',
	classifiers=[
		'Development Status :: Production/Stable',
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
	
	#package_dir={ '': 'library' },
	packages=[
		''
	],
	scripts=[
		'bin/auditlog',
		'bin/rlog',
		'bin/collection'
	],
	data_files = [
		('etc', ['etc/auditlog.ini']),
		('etc', ['etc/logging.ini']),
		('log', ['log/auditlog.log']),
		('share', ['share/example/testing/example.com.ini'])
		#('example/config/testing', ['example/config/testing/www.example.com.ini']),
		#('example/exclude/testing', ['example/exclude/testing/www.example.com.lst'])
		
	]
)

