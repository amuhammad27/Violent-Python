#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 02:37:27 2017

@author: root
"""

from pexpect import pxssh 

def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print s.before

def connect(host,user,password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return s
    except: 
        print '[-] Error Connecting'
        exit(0)
        
s = connect('localhost','root','AllisWell27!')
send_command(s, 'cat /etc/shadow | grep root')