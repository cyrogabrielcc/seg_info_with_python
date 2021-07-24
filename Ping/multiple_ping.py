import os

with open('hosts.txt') as file:
    dumb = file.read()
    dumb=dumb.splitlines()

    for ip in dumb:
       os.system ('ping -n 20 {}'.format(ip))
 









