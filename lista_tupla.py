lista = [1,2,3,4,8,9,5]
lista1 = [ 'julio', 'marcos', 'sarah', 'kei', 'madu', 'kei', 'tulio']
#print (lista)
novalista = lista * 3
#print (novalista)

if 'douglas' in lista1:
    print('Existe kei na lista.')
else:
    print('Não existe douglas na lista, mas será incluido.')
    lista1.append('douglas')
    print(lista1)

lista1.pop(1)
#print (lista1)

lista1.remove('tulio')
#print(lista1)

lista.sort()
lista1.sort()
#print(lista)
#print(lista1)


lista1 [0] = 'ruan'
print(lista1)

tupla = (1,2,4,6,10)
print (len(tupla))
print (len(lista1))

tupla_lista1 = tuple(lista1)
print(type(tupla_lista1))

tupla_numerica = list (tupla)
print(type(tupla_numerica))

tupla_numerica[4] = 100
print(tupla_numerica)