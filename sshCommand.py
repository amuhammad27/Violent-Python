#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 02:13:07 2017

@author: root
"""

import pexpect 
PROMPT = ['# ','>>> ', '> ', '\$ ']

def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before

def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr) 
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, \
                    '[P|p]assword:'])
    if ret == 0:
        print'[-] Error Connecting' 
        return 
    if ret == 1: 
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, \
                            '[P|p]assword:'])
    if ret == 0: 
        print '[-] Error Connecting' 
        return 
    child.sendline(password)
    child.expect(PROMPT)
    return child 
def main():
    host = 'localhost'
    user = 'root'
    password = 'AllisWell27!'
    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root')

if __name__ == '__main__': 
    main()

            