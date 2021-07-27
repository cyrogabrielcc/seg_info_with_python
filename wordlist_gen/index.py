from itertools import permutations
#Feito o mais simples possível

import itertools

resultado = itertools.permutations('123456789', 4)

for i in resultado:
    print(''.join(i))