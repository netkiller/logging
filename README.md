logging
=======

Install
-------

	[root@localhost ~]# pip3 install netkiller-logging
	
	[root@localhost ~]# whereis rlog 
	rlog: /usr/local/bin/rlog

	[root@localhost ~]# rlog 
	Usage: rlog [options] filename

	Options:
	-h, --help            show this help message and exit
	-H localhost, --host=localhost
							push log to remote host
	-p 1214, --port=1214  port
	--sleep=0.05          with -s, sleep  for  approximately S  seconds between
							iterations
	-d, --daemon          run as daemon
	-f, --full            Full text
	--stdin               cat file | prog ...
	-e /tmp/rlog.log, --errlog=/tmp/rlog.log
							error log
	--postion             save postion of log file

	Homepage: http://netkiller.github.io	Author: Neo <netkiller@msn.com>

Source 
------

	$ git clone https://github.com/netkiller/logging.git
	$ cd logging
	$ python3 setup.py sdist
	$ python3 setup.py install
	
	cp init.d/ulog /etc/init.d/
	chkconfig --add ulog
	chkconfig ulog on
	
Example
-----

	$ rlog
	Usage: rlog [options] filename

	Options:
	  -h, --help            show this help message and exit
	  -H localhost, --host=localhost
							push log to remote host
	  -p 1214, --port=1214  port
	  --sleep=0.1           with -s, sleep  for  approximately S  seconds between
							iterations
	  -d, --daemon          run as daemon
	  -f, --full            Full text
	  --stdin               cat file | prog ...

	  Homepage: http://netkiller.github.io	Author: Neo <netkiller@msn.com>

Send logs
-----

	$ rlog /var/log/nginx/access.log
	b'192.168.6.20 - - [11/Dec/2014:15:51:24 +0800] "GET /home/about.html HTTP/1.1" 200 7802 "http://192.168.6.2/home/download.epub.html" "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"\n'
	b'192.168.6.20 - - [11/Dec/2014:15:51:24 +0800] "GET /stylesheet.css HTTP/1.1" 304 0 "http://192.168.6.2/home/about.html" "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"\n'
	
	# Send log to 192.168.2.1
	$ rlog -H192.168.2.1 -p1214 /var/log/nginx/access.log	
	
	# Full text log to 192.168.2.1
	$ rlog -H192.168.2.1 -p1214 -f /var/log/nginx/access.log	
	
	# Daemon mode
	$ rlog -H192.168.2.1 -p1214 -d /var/log/nginx/access.log
	
	# Stdin
	$ cat /var/log/nginx/access.log | rlog -H 127.0.0.1 --stdin

Logs collection
-----
	$ collection 
	Usage: collection [options] module

	Options:
	  -h, --help            show this help message and exit
	  -p 1214, --port=1214  port
	  -l /tmp/test.log, --logfile=/tmp/test.log
							log file
	  --list                show module message
	  -d, --daemon          run as daemon

	  Homepage: http://netkiller.github.io	Author: Neo <netkiller@msn.com>
	
	# show log from port 1214
	$ collection -p 1214
	
	# Save log to file from port 1214
	$ collection -p 1214 -l /tmp/test.log
	
Audit log
------
[Audit log tools](doc/auditlog.md).
