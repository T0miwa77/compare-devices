import re


file = open('devices-06.txt', 'r')

devices_list = []

ip_addr_pattern = re.compile(r'Mgmt:(\df{1,3}\.\d{1,3}\.zd{1,3}\.\d{1,3}')

current_version = 'Version 5.3.1'

print('\nDevices with Incorrect Software Versions')
print('------------------------------------------')


print('\nDevices and their Management IP Addresses')
print('-------------------------------------------')

for line in file:
    device_info_list = line.strip().split(',')


    device_info = {}
    if len(device_info_list) >= 6:
        device_info['do1-is'] = device_info_list[0]
        device_info['ios'] = device_info_list[1]
        device_info['192.168.122.1'] = ip_addr_pattern.search(line).group(1)
        device_info['Version 5.3.1'] = device_info_list[3]
        device_info['cisco'] = device_info_list[4]
        device_info['cisco'] = device_info_list[5]


    device_info = [
        {
            'name': 'do1-is',
            'os-type': 'ios',
            'ipaddresss': '192.168.122.1',
            'version': 'Version 5.3.1',
            'username': 'cisco',
            'password': 'cisco'
        },
        {
            'name': 'do2-is',
            'os-type': 'ios',
            'ipaddresss': '192.168.122.2',
            'version': 'Version 4.22.18',
            'username': 'cisco',
            'password': 'cisco'
        },
        {
            'name': 'do3-nx',
            'os-type': 'nx-os',
            'ipaddresss': '192.168.122.3',
            'version': 'Version 5.3.1',
            'username': 'cisco',
            'password': 'cisco'
        },
        {
            'name': 'do4-nx',
            'os-type': 'nx-os',
            'ipaddresss': '192.168.122.4',
            'version': 'Version 5.3.1',
            'username': 'cisco',
            'password': 'cisco'
        },
        {
            'name': 'do5-xr',
            'os-type': 'ios-xr',
            'ipaddresss': '102.168.122.5',
            'version': 'Version 4.16.9',
            'username': 'cisco',
            'password': 'cisco'
        },
        {
            'name': 'do6-xr',
            'os-type': 'ios-xr',
            'ipaddresss': '192.168.122.6',
            'version': 'Version 5.3.0',
            'username': 'cisco',
            'password': 'cisco'
        },
        {
            'name': 'do7-xe',
            'os-type': 'ios-xe',
            'ipaddresss': '192.168.122.7',
            'version': 'Version 4.16.0',
            'username': 'cisco',
            'password': 'cisco'
        },
        {
            'name': 'do8-xe',
            'os-type': 'ios-xe',
            'ipaddresss': '192.168.122.8',
            'version': 'Version 5.3.0',
            'username': 'cisco',
            'password': 'cisco'
        },
    ]

    devices_list.append(device_info)

    if device_info['version'] != current_version:
        print(f"Device {device_info['name']} Mgmt IP: {device_info['ipaddress']}") 

print(f"\nTotal number of devices checked: {len(devices_list)}")


