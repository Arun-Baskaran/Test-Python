# Program to check whether ClamAV is installed
import paramiko
import os
import time
file1 = "/home/local/MGMTPROD/baska010/ClamAv-Status"
Server_List = "/home/local/MGMTPROD/baska010/server.list"


def ssh_connection(source_server, source_os_password):
    Client = paramiko.SSHClient()
    Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    Client.connect(hostname=source_server, password=source_os_password)
    return Client


def ssh_close_connection(Client):
    Client.close()


def run_command(Client):
    print("Now i'm inside the server {}".format(server))
    Client.invoke_shell()
    stdin, stdout, stderr = Client.exec_command("ps -ef | grep -i clamAv | grep -v grep")
    time.sleep(20)
    exit_code = stdout.read().decode('ascii').strip("\n")
    print(exit_code)
    print(stdout.read())
    cmd_out = stdout.readlines()
    print(cmd_out)
    if cmd_out is None:
        print ("ClamAV not installed in the server")
        with open(file1,  'w') as wf:
            wf.write("ClamAV not installed in the server {}")
    else:
        print("ClamAV is installed in the server {}".format(server))


def main():
    print ("")
    with open(Server_List, 'r') as line:
        for server in line:
            print ("Connecting to the server - {}".format(server))
            global server
            Client = ssh_connection(source_server=server, source_os_password="L0nd0n$Br1dge")
            # print(Client)
            run_command(Client)
            print("Closing Connection")
            ssh_close_connection(Client)
            print ("Done")
