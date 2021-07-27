import hashlib 
result = hashlib.md5(b'Python Secyrity')

palavra = input("Digite alguma parada ai: ")

menu = input('''ESCOLHA O TIPO DE HASH: 
                1-MD5
                2-SHA1
                3-SHA256
                2-SHA512
            Digite o que tu quer: ''')


if menu == 1:
    result = hashlib.md5(palavra.encode('utf-8'))
    print('O hash da string é md5: ', result.hexdigest())
elif menu== 2: 
    result = hashlib.sha1(palavra.encode('utf-8'))
    print('O hash da string é sha1: ', result.hexdigest())
elif menu== 3: 
    result = hashlib.sha256(palavra.encode('utf-8'))
    print('O hash da string é sha256: ', result.hexdigest())
elif menu== 4: 
    result = hashlib.sha512(palavra.encode('utf-8'))
    print('O hash da string é sha512: ', result.hexdigest())








