Plugin Nagios standard **check_http**

Basique ::

    ./check_http -H shop.lego.com


En spécfiant une IP ::

    ./check_http -H shop.lego.com -I 171.20.70.113


En suivant la redirection web ::

    ./check_http -H shop.lego.com -I 171.20.70.113 -f follow

