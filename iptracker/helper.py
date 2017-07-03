#!/usr/bin/env python3

Database_URL = 'http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz'

Delay_ms = 1000


class CouldNotDownload(ConnectionError):
    pass


class CouldNotExtract(IOError):
    pass


class CouldNotDelete(IOError):
    pass
