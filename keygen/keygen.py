import random, string
import os

tam = int(input('digite o tamanho da senha: '))
chars = string.ascii_letters + string.digits + '-+*#$%&()_-='
rnd = random.SystemRandom()

print("_"*60)
print()
print(''.join(rnd.choice(chars) for i in range(tam)))
print("_"*60)













