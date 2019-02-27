#!/usr/bin/python
import getpass
import sys
import telnetlib

user = raw_input("Enter your remote account: ")
outputfilename = raw_input("Enter output filename: ")
password = getpass.getpass()

hostfile = open("hosts.txt")
outputfile = open(outputfilename,"a")
hosts = hostfile.readlines()

for host in hosts:
    print host
    tn = telnetlib.Telnet(host)
    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
    tn.write("terminal length 0\n")
    tn.write("show version\n")
    tn.write("exit\n")
    outputfile.write(tn.read_all())
    tn.close()

outputfile.close()
