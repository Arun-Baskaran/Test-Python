#!/usr/local/bin/python

import paramiko
import subprocess
import os
with open("server.list","r") as f:
    f_contents = f.read()

for x in f_contents:


#SSH_CONNECT to the server

def ssh_connect(ssh):
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect
