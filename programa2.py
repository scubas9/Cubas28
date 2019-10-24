#programa donde cobine listas tuplas y set
frutas=["mango","pera","uva","mandarina"]
frutas.sort()
#convertiremos la lista ordenada a tupla
A=tuple(frutas)
print(A)
#operacion cortado en la tupla "f"
print(A[0:3])
#ahora convertiremos esa tupla en lista nuevamente
b=list(frutas)
print(b)
#creamos el set:
se={"naranja"}
#operacion de agregado
se.add("mango")
print(len(se))
print(se)




