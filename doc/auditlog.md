Auditlog
======


Help
----
	$ auditlog
	Usage: 
	  Homepage: http://netkiller.github.com
	  Author: Neo <netkiller@msn.com>

	Options:
	  -h, --help            show this help message and exit
	  -d, --daemon          run as daemon
	  -l LOGFILE, --logfile=LOGFILE
							log file example: /var/log/message
	  -r REGEX, --regex=REGEX
							regex/regexp example: ^Feb
	  --regular=REGULAR     regular file
	  --debug               Print debug information

Search keyword by regular
--------------
	$ python3 auditlog -l /var/log/syslog -r "\/etc\/cron.hourly\)$"
	Feb 24 07:17:01 ubuntu CRON[28905]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
	Feb 24 08:17:01 ubuntu CRON[29888]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
	Feb 24 09:17:01 ubuntu CRON[31136]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
	Feb 24 10:17:01 ubuntu CRON[32231]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
	Feb 24 11:17:01 ubuntu CRON[841]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
	Feb 24 12:17:01 ubuntu CRON[1977]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
	Feb 24 13:17:01 ubuntu CRON[3059]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
	Feb 24 14:17:01 ubuntu CRON[4263]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
	Feb 24 15:17:01 ubuntu CRON[5335]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
	Feb 24 16:17:01 ubuntu CRON[6573]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
	
	$ python3 auditlog -l /var/log/syslog -r "^Feb"
	Feb 24 06:48:30 ubuntu rsyslogd: [origin software="rsyslogd" swVersion="5.8.11" x-pid="829" x-info="http://www.rsyslog.com"] rsyslogd was HUPed
	Feb 24 06:48:30 ubuntu CRON[27658]: (CRON) info (No MTA installed, discarding output)
	Feb 24 07:09:01 ubuntu CRON[28764]: (root) CMD (  [ -x /usr/lib/php5/maxlifetime ] && [ -x /usr/lib/php5/sessionclean ] && [ -d /var/lib/php5 ] && /usr/lib/php5/sessionclean /var/lib/php5 $(/usr/lib/php5/maxlifetime))
	Feb 24 07:17:01 ubuntu CRON[28905]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
	
	$ auditlog -l /var/log/syslog --regular=syslog.reg
	
	$ auditlog -l /var/log/syslog --regular=syslog.reg -r '^Feb'

Configure
---------

### auditlog.ini 
	[syslog]
	logfile=/var/log/syslog
	;exclude=share/syslog.reg
	include=share/syslog.reg
	
	[dmesg]
	logfile=/var/log/dmesg
	include=share/dmesg.reg
	;exclude=
	
	[dpkg]
	logfile=/var/log/dpkg.log
	include=share/dpkg.reg
	exclude=share/dpkg1.reg

### regular
	$ cat syslog.reg
	^Feb
	:09:	
	
Daemon
------
	$ python3 auditlog -d
