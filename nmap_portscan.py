#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 20:42:07 2017

@author: root
"""

import nmap
import optparse

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print "[+] " + tgtHost + " tcp/" +tgtPort + " "+state
    
def main():
    parser=optparse.OptionParser('usage%prog ' +
                                 'H <target Host> -p <target Port>')
    parser.add_option('-H', dest = 'tgtHost', type = 'string', \
                          help = 'specify target host')
    parser.add_option('-p', dest = 'tgtPort', type = 'string', \
                          help = 'specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
        
    if (tgtHost == None) | (tgtPorts[0] == None): 
        print parser.usage
        exit(0)
    for tgtPort in tgtPorts: 
            nmapScan(tgtHost, tgtPort)

if __name__ == '__main__': 
    main()
        