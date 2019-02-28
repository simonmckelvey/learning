#!/usr/bin/env python

from ncclient import manager

host = "192.168.122.11"
port = "830"
user = "simon"
password = "cisco"
platform = "csr"

with manager.connect(host=host, port=830, username=user, password=password,
                     hostkey_verify=False, device_params={'name':platform}) as m:
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % host, 'w') as f:
        print f
        f.write(c)

