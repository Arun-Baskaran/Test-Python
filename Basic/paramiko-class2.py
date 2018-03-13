#!/usr/bin/python
import paramiko
import sys
import getpass
import socket
file1 = "/home/local/MGMTPROD/baska010/ClamAv-Status"
file2 = "/home/local/MGMTPROD/baska010/ClamAv-Installed-Status"
Server_List = "/home/local/MGMTPROD/baska010/server.list"


class PySSH(object):
    def __init__(self):
        self.ssh = None
        self.transport = None

    def disconnect(self):
        if self.transport is not None:
            self.transport.close()
        if self.ssh is not None:
            self.ssh.close()

    def connect(self, hostname, passwd, port):
        self.hostname = hostname
        self.passwd = passwd
        self.port = port
        print (passwd)
        # Making Connection to the server
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.load_system_host_keys()
        try:
            self.ssh.connect(hostname=hostname, password=passwd, port=22)
            self.transport = self.ssh.get_transport()
        except (socket.error, paramiko.AuthenticationException) as message:
            print("ERROR: SSH connection to " + self.hostname + " failed: " + str(message))
            sys.exit(1)
        return self.transport is not None

        # Running the commands here

    def run_command(self, cmd, sudoenabled=False):
        if sudoenabled:
            #fullcmd = "echo " + self.passwd + " | sudo -S -p ' ' " + cmd
            #fullcmd="echo " + self.passwd + " |   sudo -S -p '' " + cmd
            #fullcmd="echo " + '***********' + " | sudo -S  " + cmd
            fullcmd = "sudo -k yum list installed clamAv"
            print(fullcmd)
        else:
            fullcmd = cmd
        if self.transport is None:
            return "ERROR: connection was not established"
        session = self.transport.open_session()
        session.set_combine_stderr(True)
        if sudoenabled:
            session.get_pty()
        session.exec_command(fullcmd)
        stdin = session.makefile('wb', -1)
        stdout = session.makefile('rb', -1)
        stdin.write(passwd + '\n')
        # print stdout.read()
        output = stdout.read()
        if len(output) == 0:
            print ("ClamAV not installed in the server")
            with open(file1,  'a') as wf:
                wf.write("ClamAV not installed in the server -  {}".format(server))
        else:
            print("ClamAV is installed in the server {}".format(server))
            with open(file2,  'a') as wf:
                wf.write("ClamAV installed in the server -  {}".format(server))
        session.close()
        return output

#===========================================
# MAIN
#===========================================


def main():
    print("")
    passwd = getpass.getpass("Enter your password : ")
    port = 22
    ssh = PySSH()
    with open(Server_List, 'r') as line:
        for server in line:
            print ("Connecting to the server - {}".format(server))
            global server
            ssh.connect(server, passwd, port)
            output = ssh.run_command('service sshd status', True)
            print("Closing Connection")
            ssh.disconnect()
            print("Disconnected from the server - {0}".format(server))
            continue
            print("")
            return


if __name__ == '__main__':
    #hostname = 'N7PRSERVER0126.starwave.com'
    main()
