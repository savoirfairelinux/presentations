Manuel

::

	check_influxdb -h
	usage: /home/peyre/Monitoring-tools/envNova/bin/check_influxdb
	      [-h] [-v] [-w WARNING] [-c CRITICAL] [--mode MODE] [--host HOST]
	      [--port PORT] [--timeout TIMEOUT] [--user USER] [--password PASSWORD]
	optional arguments:
	  -h, --help            show this help message and exit
	  -v, --version         show program's version number and exit
	  -w WARNING, --warning WARNING
				Set the warning threshold
	  -c CRITICAL, --critical CRITICAL
				Set the critical threshold
	  --mode MODE, -m MODE  choose type of warning/critical : connection-
				time, uptime, nb-shards, nb-write-total, write-since-last
				, nb-read-total, read-since-last, ROM-allocate, RAM-used
				, ROM-used, continuous-query, routine-go
	  --host HOST, -H HOST  The host of influxdb server.
	  --port PORT, -p PORT  The port of influxdb server.
	  --timeout TIMEOUT, -T TIMEOUT
				timeout de connection
	  --user USER, -u USER  user of the monitoring database
	  --password PASSWORD, -P PASSWORD
				password to access to the monitoring database

