import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('The socket is created')

host = 'localhost'
porta = 5432

message = 'Servidor: Eae Clientin'

s.bind((host, porta))

while 1: 
    data, end = s.recvfrom(4096)

if data:
    print('servidor enviando mensagem...')
    s.sendto(data+(message.encode(), end))



