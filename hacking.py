import nmap
nm = nmap.PortScanner()
print(nm.nmap_version())
ports_to_scan='1-1024'
nm.scan('127.0.0.1',ports_to_scan,'-v --version-all')
print(nm.scaninfo())
print(nm.csv())
print(nm.all_hosts())

nm.scan('192.168.1.73',ports_to_scan,'-sV --version-all')
print(nm.scaninfo())
print(nm.csv())
print(nm.all_hosts())
print(nm['192.168.1.73'].state())
print(nm['192.168.1.73'].all_protocols())
print(nm['192.168.1.73']['tcp'].keys())
print(nm['192.168.1.73'].has_tcp(80))

# There are 65,536 ports. The ports from 0 to 1023 are considers “system ports” and are generally where you will find common services like DNS, SMTP and HTTP. Higher number ports are considered “dynamic” and will be assigned on an as needed basis (or are assigned by the program needing network services).
# There are too many to list in a Quora answer, so I will refer you to the wiki list of common port assignments.
# https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
ports_to_scan='0-65535'
camera_ip='192.168.1.81'
nm.scan(camera_ip,ports_to_scan,'-sV --version-all')
print(nm.scaninfo())
print(nm.csv())
print(nm.all_hosts())
print(nm[camera_ip].state())
print(nm[camera_ip].all_protocols())
print(nm[camera_ip]['tcp'].keys())
print(nm[camera_ip].has_tcp(80))
# >>> nm.command_line()
# 'nmap -oX - -p 22-443 -sV 127.0.0.1'
# >>> nm.scaninfo()
# {'tcp': {'services': '22-443', 'method': 'connect'}}
# >>> nm.all_hosts()
# ['127.0.0.1']
# >>> nm['127.0.0.1'].hostname()
# 'localhost'
# >>> nm['127.0.0.1'].state()
# 'up'
# >>> nm['127.0.0.1'].all_protocols()
# ['tcp']
# >>> nm['127.0.0.1']['tcp'].keys()
# [80, 25, 443, 22, 111]
# >>> nm['127.0.0.1'].has_tcp(22)
# True
# >>> nm['127.0.0.1'].has_tcp(23)
# False
# >>> nm['127.0.0.1']['tcp'][22]
# {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh'}
# >>> nm['127.0.0.1'].tcp(22)
# {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh'}
# >>> nm['127.0.0.1']['tcp'][22]['state']
# 'open'