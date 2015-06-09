Ping 

::

	 check_influxdb -w 3 -c 5

	 OK:all is good for connection-time|'ping='0.006347ms;3.0;5.0;0.0;10.0

Nombre de requete en écriture

::

	check_influxdb -m nb-write-total -w 200 -c 300

	WARNING:nb-write-total > 200|'Number of write queries='218;200;300;0;

Nombre de shards

::

	check_influxdb -m nb-shards -w 200 -c 300

	OK:all is good for nb-shards|'Number of shards='4;200;300;0;
