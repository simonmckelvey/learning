#!/usr/bin/python3
import getpass
import telnetlib

host = input("Enter your IP address: ")
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') +b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"terminal length 0\n")
tn.write(b"show run\n")

print(tn.read_all().decode('ascii'))

