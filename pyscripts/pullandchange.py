#!/usr/bin/env python
import xmltodict

from ncclient import manager

host = "192.168.122.14"
port = "830"
user = "simon"
password = "password123"
platform = "junos"

with manager.connect(host=host, port=830, username=user, password=password,
                     hostkey_verify=False, device_params={'name':platform}) as m:
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % host, 'w') as f:
        print f
        f.write(c)
f.close()

with open("192.168.122.14.xml") as f:
    xml_example = f.read()
xml_dict = xmltodict.parse(xml_example)

print xml_dict

xml_dict['rpc-reply']['data']['configuration']['interfaces']\
    ['interface'][0]['unit']['family']['inet']['address'] = "3.3.3.3/31"
xmlfile = xmltodict.unparse(xml_dict)
print xmlfile

with open("output.xml", "w") as w:
    w.write(xmlfile)

w.close()
quit()
