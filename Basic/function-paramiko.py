#!/usr/bin/python
# Writing fucntion for paramiko
#import paramiko
# def Server_Connect():
#ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(hostname=source_server, username=source_os_user, password=source_os_password)
# stdin,stdout.sterr
Server_List = "/Users/Arun/server.list"
Node_List = []
with open(Server_List, 'r') as server:
    for line in iter(server):
        Node_List.append(line)
print(Node_List)
for x in Node_List:
    print("Processing the first node")
    ssh_connect()
