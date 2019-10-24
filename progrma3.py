#programa donde utiliza listas tuplas y set
#realizar un programa que permita la carga de una lista deun set en n cantidad de
#elementos .ordenar alfabeticamente y luego inprimir

se=set()
lista=[]
num=1
for  x in range(num):
    se1=input("ingrese el nombre de un lugar atractivo del peru:")
    atractivo=input("ingrese el lugar mas hermoso que le haya parecido:")
    se.add(se1)
    lista.append(atractivo)
set(sorted(se))
lista.sort()
lista.append("laguna azul")
a=tuple(lista)
print(a)
#iteramos todos los elementos de la tupla
for y in a:
    print(y)
#imprimimos su lugar favorito
print(se)


