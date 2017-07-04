#!/usr/bin/env python3
import ssl

Database_URL = 'http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz'

IP_URL = 'https://api.ipify.org/?format=json'

Save_URL = '~/.iptracler/database/'

Delay_ms = 1000

ssl._create_default_https_context = ssl._create_unverified_context


class CouldNotDownload(ConnectionError):
    pass


class CouldNotExtract(IOError):
    pass


class CouldNotDelete(IOError):
    pass
