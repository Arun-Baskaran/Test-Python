#!/usr/bin/python
import paramiko
import sys
import getpass
import socket


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
                #fullcmd="echo " + 'L0nd0n$Br1dge' + " | sudo -S  " + cmd
                fullcmd = "sudo -k yum list installed clamAv"
                print(fullcmd)
            else:
                fullcmd = cmd
            if self.transport is None:
               return "ERROR: connection was not established"
            session=self.transport.open_session()
            session.set_combine_stderr(True)
            if sudoenabled:
                session.get_pty()
            session.exec_command(fullcmd)
            stdin = session.makefile('wb', -1)
            stdout = session.makefile('rb', -1)
            stdin.write(passwd +'\n')
            # print stdout.read()
            output=stdout.read()
            session.close()
            return output

#===========================================
# MAIN
#===========================================
def main():
    pass

if __name__ == '__main__':
    hostname = 'N7PRSERVER0126.starwave.com'
    port = 22
    # username = 'admin'
    passwd = getpass.getpass("Enter your password : ")
    ssh = PySSH()
    ssh.connect(hostname,passwd,port)
    #output=ssh.run_command('date')
    #print output
    output=ssh.run_command('service sshd status',True)
    print output
    ssh.disconnect()
