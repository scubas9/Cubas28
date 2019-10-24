#programa que combina listas tuplas y set
pais=[]
nombre=[]
plato_favorito=[]
X=0
for x in range(1):
    pa=input("ingrese el nombre de su pais")
    nom=input("ingrese su nombre:")
    favorito=input("ingrese su plato favorito:")
    pais.append(pa)
    nombre.append(nom)
    plato_favorito.append(favorito)
for x in range(1):
    gastos=(500,200,300,800,345)
    print(nombre[x]+" pais de origen "+str(pais[x])+" plato favorito"+str(plato_favorito[x])+" consumo total"+str(gastos[x]))

