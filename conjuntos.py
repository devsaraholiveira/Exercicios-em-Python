conjunto = {1,2,3,4,5,5,5,5,5}
conjunto2 = {5,5,6,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
print ('União: {}' .format(conjunto_uniao))

conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença de 1 para 2: {}'  .format(conjunto_diferenca1))
print('Diferença de 2 para 1: {}'  .format(conjunto_diferenca2))

conjuntoa = {1,2,3}
conjuntob = {1,2,3,4,5,6,7,8,9}
conjunto_subset = conjuntoa.issubset(conjuntob)
print ('A é um subconjunto de B: {}'.format(conjunto_subset))

conjunto_superset = conjuntob.issuperset(conjuntoa)
print ('B é um superconjunto de A: {}'.format(conjunto_superset))

lista = ['sarah', 'douglas', 'madu', 'kei', 'madu','ruan', 'luiz']
print (lista)
conjunto_lista = set(lista)
print (conjunto_lista)
lista1 = list(conjunto_lista)
print(lista1)