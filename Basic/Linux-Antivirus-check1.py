#!/usr/local/bin/python
# Program to check whether ClamAV is installed
import paramiko
import os
import time
file1 = "/home/local/MGMTPROD/baska010/ClamAv-NotInstalled-Status"
file2 = "/home/local/MGMTPROD/baska010/ClamAv-Installed-Status"
Server_List = "/home/local/MGMTPROD/baska010/server.list"
cmd = "rpm -qa | grep clamav"
def ssh_connection(source_server , source_os_password):
    Client = paramiko.SSHClient()
    Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    Client.connect(hostname=source_server, password=source_os_password)
    return Client
def ssh_close_connection(Client):
    Client.close()
def run_command(Client):
    print("Now i'm inside the server {}".format(server))
    Client.invoke_shell()
    #transport = Client.get_transport()
    #session = transport.open_session()
    #session.set_combine_stderr(True)
    #session.get_pty()
    #session.exec_command(cmd)
    #stdin = session.makefile('wb', -1)
    #stdout = session.makefile('rb', -1)
    #stdin.write("L0nd0n$Br1dge" +'\n')
    #stdin.flush()
    stdin, stdout, stderr = Client.exec_command(cmd)
    time.sleep(20)
    exit_code = stdout.read().decode('ascii').strip("\n")
    #print("Stderr = " + stderr.read())
    #print("Exit Code = " + exit_code)
    #print("Stdout = " + stdout.read())
    #print(exit_code)
    #print(stdout.read())
    cmd_out = stdout.readlines()
    #print(type(cmd_out))
    #print("CMD OUT IS " + str(cmd_out))
    #print(str(cmd_out))
    #cmd_out = cmd_out if cmd_out != None else []
    #cmd_out = cmd_out if [] is None else cmd_out
    if len(cmd_out) == 0:
    #if cmd_out is None:
        print ("ClamAV not installed in the server")
        with open(file1,  'a') as wf:
            wf.write("ClamAV not installed in the server -  {}".format(server))
    else:
        print("ClamAV is installed in the server {}".format(server))
        with open(file2,  'a') as wf:
            wf.write("ClamAV installed in the server -  {}".format(server))

def main():
    print ("")
    with open(Server_List,'r') as line:
        for server in line:
            print ("Connecting to the server - {}".format(server))
            global server
            Client = ssh_connection(source_server = server , source_os_password = "L0nd0n$Br1dge")
            #print(Client)
            run_command(Client)
            print("Closing Connection")
            ssh_close_connection(Client)
            print ("Done")
            continue
            print("")
            return
if "__name__ == __main__":
    main() 
