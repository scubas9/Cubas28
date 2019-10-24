#OPERACION1 "CREACION":
#EJER1
tupla1=()
print(tupla1)
#EJER2
tupla2=(12,34,34)
print(tupla2)

#EJER3
tupla3=("loro","pavo","condor")
print(tupla3)
#EJER4
tupla4=("armadillo","majas")
print(tupla4)
#EJER5
tupla5=("chiclayo","ferreñafe","lambayeque")
print(tupla5)
#EJER6
tupla6=("rios","valles","nevados")
print(tupla6)
#EJER7
tupla7=(3.14,2.718182)
print(tupla7)
#EJER8
tupla8=("san marcos","paytoja","bellavista","nuevo orizonte","alto peru")
print(tupla8)
#EJER9
tupla9=(12,23,45,56)
print(tupla9)
#EJER10
tupla10=("a","e","i","o","u")
print(tupla10)
#OPERACION2 "PERTENENCIA":
#EJER1
tu1=(12,23,34)
print(12 in tu1)
#EJER2
tu2=(123,345,456)
print(33 not in tu2)
#EJER3
tu3=("rosa","juana","maria","marta")
print("rosa" in tu3)
#EJER4
tu4=("pantalon","camisa","corbata")
print("cuchara" in tu4)
#EJER5
tu5=("sandilla","guanabana","tumbo")
print("papaya" not in tu5)
#EJER6
tu6=("paolo","farfan","gallese","cueva")
print("pizarro" not in tu6)
#EJER7
tu7=("guitarra","piano","tinbales","bajo")
print("vocalista" in tu7)
#EJER8
tu8=("bus","traile","fuso","canter","camioneta")
print("zorro" not in tu8)
#EJER9
tu9=("arroz","aceite","azucar")
print("chocolate" in tu9)
#EJER10
tu10=("peru","chile","argentina")
print("polonia" not in tu10)
#OPERACION3 "CONCATENACION"
#EJER1
tup1=("maiz","arroz","cafe","papa")
tup2=("leche","agua","gelatina")
print(tup1+tup2)
#EJER2
tup3=("zapote","mango","cacao")
print(tup3+tup2)
#EJER3
tup4=("profesores","ingenieros","doctores","mecanicos")
print(tup4+tup2)
#EJER4
tup5=("ovejas","venados","caballo","burro")
print(tup1+tup5)
#EJER5
tup6=("quina","cornocopia","vicuña")
print(tup5+tup6)
#EJER6
tup7=("pesos","dolares","libra esterlina","sol")
print(tup7+tup6)
#EJER7
tup8=("boticas","farmacia","clinica","hospitales")
print(tup8+tup7)
#EJER8
tup9=("ventana","puerta","luna")
print(tup9+tup8)
#EJER9
tup10=("motor","chaleadora","finigadora")
print(tup10+tup9)
#EJER10
tup11=("aluminio","cobre","zinc","potasio")
print(tup11+tup10)
#OPERACION4  "COMPARACION":
frutas=("manzana","papaya","tumbo")
verduras=("manzana","papaya","mandarina")
animales=("zorro","ardilla","pato")
paises=("canada","bolivia","surinan")
rios=("ene","perene","ucayaly")
#ejer1
print(frutas==verduras)
#ejer2
print(verduras!=frutas)
#ejer3
print(animales==frutas)
#ejer4
print(paises!=rios)
#ejer5
print(rios!=verduras)
#ejer6
print(rios==verduras)
#ejer7
print(animales>paises)
#ejer8
print(rios<animales)
#ejer9
print(frutas>verduras)
#ejer10
print(animales!=paises)
#OPERACION 5 "INDEXACION"
#EJER1
print(animales[0])
#EJER2
print(frutas[2])
#EJER3
print(paises[2])
#EJER4
print(rios[1])
#EJER5
print(rios[0:2])
#EJER6
print(rios[2:3])
#EJER7
print(verduras[2])
#EJE8
print(verduras[0])
#EJER9
print(animales[2])

#EJER10
print(animales[1:2])
#OPERACION6 "CORTADO"
#EJER1
print(tu1[0:1])
#EJER2
print(tup2[::-1])
#EJER3
print(tu3[::])
#EJER4
print(tup4[1:2])
#EJER5
print(tu5[2:3])
#EJER6
print(tu6[3:4])
#EJER7
print(tup7[2:3])
#EJER8
print(tu9[::-1])
#EJER9
print(tup9[::])
#EJER10
print(tu10[1:2])
#OPERACION 7 "LONGITUD:
#EJER1
print(len(tu1))
#EJER2
print(len(tu2))
#EJER3
print(len(tu3))

#EJER4
print(len(tu4))
#EJER5
print(len(tu5))
#EJER6
print(len(tu6))
#EJER7
print(len(tu7))
#EJER8
print(len(tu8))
#EJER9
print(len(tu9))
#EJR10
print(len(tu10))
#OPERACION 8 "ITERACION"
#EJER1
for a in tu1:
    print(a)
#EJER2
for a in tu2:
    print(a)
#EJER3
for a in tu3:
    print(a)
#EJER4
for a in tu4:
    print(a)
#EJER5
for a in tu5:
    print(a)
#EJER6
for a in tu6:
    print(a)
#EJER7
for a in tu7:
    print(a)
#EJER8
for a in tu8:
    print(a)
#EJER9
for a in tu9:
    print(a)
#EJER10
for a in tu10:
    print(a)
#OPERACION 9 "BUSQUEDA":
#EJER1
print(tu1.index(12))
#EJER2
print(tu2.index(123))

#EJER3
print(tu3.index("rosa"))
#EJER4
print(tu4.index("pantalon"))
#EJER5
print(tu5.index("tumbo"))
#EJER6
print(tu6.index("paolo"))
#EJER7
print(tu7.index("piano"))
#EJER8
print(tu8.index("bus"))
#EJER9
print(tu9.index("azucar"))
#EJER10
print(tu10.index("chile"))
#OPERACION 10 "CONTEO"
#EJER1
TUPLA1=(12,34,45,56,45)
TUPLA1.count(12)
#EJER2
TUPLA2=(23,45,56,67,78)
TUPLA2.count(23)
#EJER3
TUPLA3=(56,67,890,543)
TUPLA3.count(67)
#EJER4
TUPLA4=(234,567,6543)
TUPLA4.count(567)
#EJER5
TULA5=(12,43,56,789)
TULA5.count(789)
#EJER6
TUPLA6=(8976.45,320.23)
TUPLA6.count(320)
#EJER7
TUPLA7=(23,67,78,89)
TUPLA7.count(67)
#EJER8
TUPLA8=(34,567,89,1234)
TUPLA8.count(89)
#EJER9
TUPLA9=(1,2,3,4,5)
TUPLA9.count(4)
#EJER10
TUPLA10=(12,113,14,15)
TUPLA10.count(113)
#OPERACION  "MAXMIN"
#EJER1
max(tu1)
#EJE2
max(tu2)
#EJR3
max(tu3)
#EJE4
max(tu4)
#EJER5
max(tu5)
#EJER6
min(tu6)
#EJER7
min(tu7)
#EJER8
min(tu8)
#EJER9
min(tu9)

#EJE10
min(tu10)

#OPERACION "MULTIPLICASION"
#EJE1
TUPLA1*2
#EJER2
TUPLA2*3
#EJER3
TUPLA3*3
#EJER4
TUPLA4*1
#EJER5
TULA5*2
#EJER6
TUPLA6*1
#EJER7
TUPLA8*2
#EJER8
TUPLA9*3
#EJER9
TUPLA10*1
#EJER10
tu10*2


