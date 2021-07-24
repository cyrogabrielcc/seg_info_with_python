import os

ip_or_post = input("Escreva o IP ou Host a ser verificado: ")
os.system('ping -n 6 {}'.format(ip_or_post))





















