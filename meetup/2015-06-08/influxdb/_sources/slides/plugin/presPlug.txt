* Codé en python

* Utilise python-influxdb pour les requetes (disponible sur pypi)

* Renvoi 12 métriques (parametre MODE) différentes :
	* Consommation de RAM, de ROM
	* Nombre de lecture/ecriture 
	* Nombre de shard (indique le nombre de série)
	

	
	
* Utilisation 

::

	check_influxdb	[-h]  [-w WARNING] [-c CRITICAL] [--mode MODE]
