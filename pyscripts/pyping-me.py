#!/usr/bin/python
import pyping

hostip = raw_input("Enter your IP/DNS to ping: ")

response = pyping.ping(hostip)

print "Sent ping to IP address: " + response.destination_ip
if response.ret_code == 0:
    print "Min RTT = " + response.min_rtt
    print "Max RTT = " + response.max_rtt
    print "Packets Lost = " + str(response.packet_lost)
else:
    print "Ping failed for some weird reason"
