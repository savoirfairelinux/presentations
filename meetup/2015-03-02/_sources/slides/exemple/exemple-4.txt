
config.xml

:: 

    <globalhttplog>onfail</globalhttplog>
   

lego.xml

::

    <testcases repeat="1">
        <case
            id             = "1"
            description1   = "Lego store home page"
            method         = "get"
            url            = "http://shop.lego.com/fr-CA/"
            verifypositive = "Du Nouveau"
            label          = "homepage"
        />
    </testcases>

Lancement du test

::

    perl bin/webinject.pl -c config.xml lego.xml -r nagios
        
