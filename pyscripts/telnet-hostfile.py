#!/usr/bin/python
import getpass
import sys
import telnetlib

user = raw_input("Enter your remote account: ")
password = getpass.getpass()

hosts = open("hosts.txt")

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
    print tn.read_all()
    tn.close()

