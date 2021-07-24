import socket
import sys

def main():
    try:
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
    except socket.error as error:
        print("The connect is failed: {}".format(error))
        sys.exit()
    
    print("Success!!!")
    target_host = input("Digite o host a ser conectado: ")
    door_host = input("Digite a porta aser conectada: ")


    try:
        s.connect((target_host, int(door_host)))
        print("Cliente conectado com sucesso: " + target_host + " e na porta: " + door_host)
        s.shutdown()


    except socket.error as error:
        print("Não foi possível conectar no host especificado")
        print("The connect is failed: {}".format(error))
        sys.exit()

if __name__ == "__main__":
    main()

















