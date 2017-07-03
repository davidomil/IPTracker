#!/usr/bin/env python3
import gzip
import os
from urllib.request import urlopen, urlretrieve
from json import loads
import time

import errno
from helper import *

import pygeoip


def exists(path):
    """Test whether a path exists.  Returns False for broken symbolic links"""
    try:
        st = os.stat(path)
    except os.error:
        return False
    return True


def ensure_dir(dirname):
    """
    Ensure that a named directory exists; if it does not, attempt to create it.
    """
    try:
        os.makedirs(dirname)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def download_database():
    """ Download ip location Database
    :return:
    """
    ensure_dir(Save_URL)
    try:
        urlretrieve(Database_URL, Save_URL + "GeoLiteCity.dat.gz")
    except Exception:
        raise CouldNotDownload()


def extract_database():
    ''' Extract Downloaded database
    :return:
    '''
    try:
        with gzip.open(Save_URL + 'GeoLiteCity.dat.gz', 'rb') as infile:
            with open(Save_URL + 'GeoLiteCity.dat', 'wb') as outfile:
                for line in infile:
                    outfile.write(line)
    except Exception:
        raise CouldNotExtract()
    delete_file(Save_URL + 'GeoLiteCity.dat.gz')


def delete_file(url):
    ''' Deletes file
    :param url: path to file to be deleted
    :return:
    '''
    try:
        os.remove(url)
    except Exception:
        raise CouldNotDelete


def get_myIP():
    """ Gets this computers public ip address
    :return: public ip address
    """
    return loads(urlopen('https://api.ipify.org/?format=json').read().decode('utf8'))['ip']


def print_ip_info(data, ip):
    ''' Prints ip data
    :param data: ip data
    :return:
    '''
    print('New IP: %s' % (ip))
    for key, val in data.items():
        print("%s: %s" % (key, val))
    print('\n')


def main(args):
    if not exists(Save_URL + 'GeoLiteCity.dat'):
        if str(input('Database was not found. Do you want me to download it for you? [y/n]')).lower() == 'y':
            try:
                download_database()
            except CouldNotDownload:
                print('Download Failed. Exiting!')
                quit()
            try:
                extract_database()
            except CouldNotExtract:
                print('Extraction Failed. Exiting!')
                quit()
            except CouldNotDelete:
                print('File deletion Failed. Exiting!')
                quit()
        else:
            print('Database was not downloaded. Exiting!')
            quit()

    gip = pygeoip.GeoIP(Save_URL + 'GeoLiteCity.dat')  # import database
    last_ip = ''
    try:
        while True:
            ip = get_myIP()
            rec = gip.record_by_addr(ip)
            if ip != last_ip:
                last_ip = ip
                print_ip_info(rec, ip)
            time.sleep(Delay_ms / 1000)

    except KeyboardInterrupt:
        pass
