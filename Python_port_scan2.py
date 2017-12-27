#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:13:28 2017

@author: root
"""

import optparse
from socket import *

def connScan(tgtHost, tgtPort): 
    try: 
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        print '[+]%d/tcp open'% tgtPort
        connSkt.close()
    except: 
        print '[-]%d/tcp closed'% tgtPort
        
def portScan(tgtHost, tgtPorts):
    try: 
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unkown host"%tgtHost
        return 
    try: 
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for: ' +tgtName[0]
    except: 
        print '\n[+] Scan Results for: ' +tgtIP
    setdefaulttimeout(1)
    for tgtPort in tgtPorts: 
        print 'Scanning port ' + tgtPort
        connScan(tgtHost, int(tgtPort))