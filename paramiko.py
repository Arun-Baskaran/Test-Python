To make an ssh connection to remote server and scp files from that server through Python script, I used the python package "paramiko". This is a library for making SSH2 connections (client or server). Emphasis is on using SSH2 as an alternative to SSL for making secure connections between python scripts. All major ciphers and hash methods are supported. SFTP client and server mode are both supported too.
 I installed paramiko in my python environment using the following steps -
wget http://pypi.python.org/packages/source/p/paramiko/paramiko-1.7.7.1.zip
unzip  paramiko-1.7.7.1.zip
cd paramiko-1.7.7.1
python setup.py build
python setup.py install
Now check whether the installation was successful or not -
python
>>> import paramiko

I added the script below where I created functions to open ssh connection, find required directory in remote machine and close that ssh connection.
#!/usr/bin/python -tt
import sys
import commands
import paramiko
import os
import re
import shutil

def open_ssh_connection():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=source_server, username=source_os_user, password=source_os_password)
    return ssh

def find_backup_dir(ssh):    
  #Change directory to remote server and list the directories
  stdin, stdout, stderr = ssh.exec_command('cd /BACKUP; ls')
  cmd_out = stdout.readlines()
  #Make tuple to string
  cmd_out= ','.join(cmd_out)
  #Find backup directories like backup_020612, here backup_dirs is a list
  backup_dirs = re.findall(r'backup_\w+', cmd_out)
  backup_dirs.sort()
  #Select the last backup directory
  backup_dir = backup_dirs[len(backup_dirs)-1]
  backup_dir=source_dbbackupdir + '/' + backup_dir
  return backup_dir 

def close_ssh_connection(ssh):
  ssh.close()

def main():
  print ""
  print "Opening connection to source server ..."
  ssh = open_ssh_connection()
  print "Done"
  print ""
  print "Searching for latest backup directory in source server ..."
  source_dbbackupdir = find_backup_dir(ssh)
  print "Lastest backup directory =", source_dbbackupdir
  print "Done"
  print ""
  print "Closing connection with the source server..."
  close_ssh_connection(ssh)
  print "Done"
  print ""
  return

if __name__ == '__main__':
 main()
