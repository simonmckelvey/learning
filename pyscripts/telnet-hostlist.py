#!/usr/bin/python
import getpass
import sys
import telnetlib

hosts = [ "192.168.122.11", "192.168.122.12",
          "192.168.122.13"]
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

for host in hosts:
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

