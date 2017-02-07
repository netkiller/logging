Manual
=====

Firewall
-----
	
	open the file /etc/sysconfig/iptables, and then append following line.
	
	-A INPUT -s <source ip address> -p udp --dport 1210:1230 -j ACCEPT


ucollection
-----

1219 ${LOGDIR}/test.log
1220 /tmp/app/$(date +"%Y-%m-%d.%H:%M:%S").log
1221 /tmp/db/$(date +"%Y-%m-%d")/mysql.log
1222 /tmp/cache/$(date +"%Y")/$(date +"%m")/$(date +"%d")/cache.log
	