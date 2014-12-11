logging
=======

Install
-------
	$ git clone https://github.com/netkiller/logging.git
	$ cd logging
	$ python3 setup.py sdist
	$ python3 setup.py install
	
Example
-----
	$ rlog /var/log/nginx/access.log
	b'192.168.6.20 - - [11/Dec/2014:15:51:24 +0800] "GET /home/about.html HTTP/1.1" 200 7802 "http://192.168.6.2/home/download.epub.html" "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"\n'
	b'192.168.6.20 - - [11/Dec/2014:15:51:24 +0800] "GET /stylesheet.css HTTP/1.1" 304 0 "http://192.168.6.2/home/about.html" "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"\n'
	
	# Send log to 192.168.2.1
	$ rlog -s -H192.168.2.1 -p1214 /var/log/nginx/access.log	
	
	# Daemon mode
	$ rlog -s -H192.168.2.1 -p1214 -d /var/log/nginx/access.log	


Audit log
------
[Audit log tools](https://github.com/oscm/devops/blob/master/doc/auditlog.md).
