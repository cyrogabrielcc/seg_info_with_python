from _typeshed import Self
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Sucess to connect -> Localhost Client")

host = 'localhost'
porta = 5433

mensagem = "Eae server"

try:
    print('Client' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    data, server= s.recvfrom(4096)
    data = data.decode()

    print("client: " + data)
finally:
    print('Client: Closing the connection')
    s.close()

















