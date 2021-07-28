import ctypes

caminho = input("Digite o caminho a ocultar: (C:/pasta/pasta)")

atributo_ocultar = 0x02

returno = ctypes.windll.kernel32.SetFileAttributesW(caminho, atributo_ocultar) 

if returno:
    print("Ok")
else:
    print("Fail")



