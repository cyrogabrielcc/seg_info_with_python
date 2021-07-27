import hashlib

a1 = 'a.txt'
a2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(a1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(a2, 'rb').read())


if hash1.digest() != hash2.digest():
    print(f'O arquivo: {a1} é diferente do {a2}')
else:
    print(f'O arquivo: {a1} é igual do {a2}')

print(f'o hash do arquivo 1 é: ', hash1.hexdigest())
print(f'o hash do arquivo 2 é: ', hash2.hexdigest())

