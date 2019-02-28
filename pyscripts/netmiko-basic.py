#!/usr/bin/env python
from netmiko import ConnectHandler

CSR1 = {
    'device_type': 'cisco_ios', 'ip': '192.168.122.11','username': 'simon', 'password': 'cisco'}

net_connect = ConnectHandler(**CSR1)
output = net_connect.send_command('show ip interface brief')
print output

config_commands = ['interface loopback 8', 'ip address 172.30.0.1 255.255.255.255', 'ip ospf 1 area 0']
output = net_connect.send_config_set(config_commands)
