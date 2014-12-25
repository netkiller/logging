Cisco IOS Configure Version Control
======

Install
-----
	$ git clone https://github.com/netkiller/logging.git
	$ cd logging
	$ python3 setup.py sdist
	$ python3 setup.py install
	
	$ sudo apt-get install expect
	$ sudo chmod +x /usr/local/libexec/*

Help
----
	$ cisco
	Usage: /usr/local/bin/cisco {init|start|stop|status|restart}

Configure
---------
	$ vim /usr/local/bin/cisco
	
	CFGFILE=$BASEDIR/etc/cisco.conf
	BACKUP_DIR=~/.backup

	$ cat /usr/local/etc/cisco.conf 
	192.168.50.1 mgmt EBopQ1X2vMkrl M8YJxvDiddG6QK
	192.168.50.2 mgmt EBopQ1X2vMkrl M8YJxvDiddG6QK
	192.168.50.3 mgmt EBopQ1X2vMkrl M8YJxvDiddG6QK
	192.168.50.4 mgmt EBopQ1X2vMkrl M8YJxvDiddG6QK
	
	$ sudo chmod 600 /usr/local/etc/cisco.conf
	
Initialization
--------------
	# Initialized empty Git repository in local.
	$ cisco init
	
	# Initialized empty Git repository from remote.
	$ cisco init http://xxx.xxx.xxx.xxx/project/xxxx.git
	$ cisco init user@host:/project/xxxx.git

Diff
------
	$ cd your_backup_dir
	$ git diff HEAD HEAD~ route.running-config
