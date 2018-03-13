#!/usr/bin/python
# Program to check whether ClamAV is installed
import paramiko
import os
file1 = "/Users/Arun/python/Test-Python/Basic/ClamAv-Status"
Server_List = "/Users/Arun/server.list"


def ssh_connection(source_server, source_os_password):
    Client = paramiko.SSHClient()
    Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=source_server, password=source_os_password)
    return ssh


def ssh_close_connection(ssh):
    ssh.close()


def run_command(ssh):
    stdin, stdout, stderr = ssh.exec_command('ps -aux | grep -i clamAv')
    cmd_out = stdout.readlines()
    if cmd_out == ''
        print ("ClamAV not installed in the server {}".format(source_server))
        with open(file1,  'w') as wf:
            wf.write("ClamAV not installed in the server {}".format(source_server))
    else:
        print("ClamAV is installed in {}".format(source_server))


def main():
    print ("")
    with open(Server_List, 'r') as line:
        for server in line:
            print ("Connecting to the server")
            ssh = ssh_connection(source_server=server, password=*********)
            run_command(ssh)
            print("Closing Connection")
            ssh_close_connection(ssh)
            print ("Done")
            print("")
            return


if "__name__ == __main__":
    main()
