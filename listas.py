#operacion 1 "CREACION"
#ejer1:
j=[]
print(j)
#ejer2:
a=[]
a=["A","B","C"]
print(a)
#ejer3:
animales=["vando_gris","sachavaca","anuje","armadillo"]
print(animales)
#ejer4:
vocales=["a","e","i","o","u"]
print(vocales)
#ejer5:
frutas=["platano","papaya","mandarina","mamey","manzana","uvas"]
print(frutas)
#ejer6:
paises=["italia","alemania","inglaterra","suisa","holanda","francia","portugal","polonia"]
print(paises)
#ejer7:
capitales_sudamericanas=["caracas","quito","asuncion","montevideo","santiago","buenos aires","brasilia","la paz"]
print(capitales_sudamericanas)
#ejer8:
provincias_lamba=["chiclayo","lambayeque","ferreñafe"]
print(provincias_lamba)
#ejer9:
universidades=["unprg","uni","unmsm","unp","uss","usv","alas peruanas"]
print(universidades)
#ejer10:
siglas=["pnp","reniec","jne","sunat","mef","onpe","ong","ugel"]
print(siglas)

#operacion numero2 "pertenencia"
#erjer1
print("pnp" in siglas)
print("tomate"in siglas)
#ejer2
print("elite" not in universidades)
#ejer3
print("papaya" in frutas)
#ejer4
print("rusia" not in paises)
#ejer5
print("mamey" in frutas)
#ejer6
print("anuje" not in animales)
#ejer7
print("armadillo" in animales)
#ejer8
print("lima" not in capitales_sudamericanas)

#ejer9
print("x" in vocales)
#ejer10
print("francia" not in paises)
#OPERACION NUMERO 3 "CONCATENACION":
#ejer1
conc1=a+vocales
print(conc1)
#ejer2
conc2=animales+frutas
print(conc2)
#ejer3
conc3=paises + siglas
print(conc3)
#ejer4
conca4=siglas + vocales
print(conca4)
#ejer5
con5=capitales_sudamericanas+paises
print(con5)
#ejr6
conc6=vocales +frutas
print(conc6)

#ejer7
conc7=a +capitales_sudamericanas
print(conc7)
#ejer8
planetas=["jupiter","saturno","marte","tierra"]
regiones=["costa","sierra","selva","mar peruano"]
conc8=planetas +regiones
print(conc8)
#ejer9
conc9=paises +planetas
print(conc9)
#ejer10
conc10=paises+regiones
print(conc10)

#OPERACION 4: "COMPARACION"
#ejer1
print(animales==paises)
#ejer2
print(paises>animales)
#ejer3
print(capitales_sudamericanas!=paises)
#ejer4
print(frutas>siglas)
#ejer5
print(animales==vocales)
#ejer6
print(vocales!=a)
#ejer7
print(vocales!=siglas)
#ejer8
print(regiones!=paises)
#ejer9
print(planetas==capitales_sudamericanas)
print(animales>planetas)
#ejer10:
print(planetas==a)
#OPERACION DE INDEXACION 5:
#EJER1
A1=animales[2]
print(A1)
#EJER2
A2=animales[3]
print(A2)
#EJER3
A3=animales[0]
print(A3)
#EJER4
FR1=frutas[3]
print(FR1)
#EJER5
FR2=frutas[0]
print(FR2)
#EJER6
FR3=frutas[1]
print(FR3)
#EJER7
VOC1=vocales[0]
print(VOC1)
#EJER8
VOC2=vocales[2]
print(VOC2)
#EJER9
pl1=planetas[0]
print(pl1)
#EJER10
SIG1=siglas[2]
print(SIG1)

#OPERACION 6 "CORTADO":
#EJER1
ANI=animales[2:]
print(ANI)
#EJER2
ANI2=animales[:2]
print(ANI2)
#EJER3
FRU1=frutas[1:3]
print(FRU1)
#EJER4
FRU3=frutas[::-1]
print(FRU3)
#EJER5
FRU4=frutas[::]
print(FRU4)
#EJER6
SIGL0=siglas[0:2]
print(SIGL0)
#EJER7
VOCAL7=vocales[0:3]
print(VOCAL7)
#EJER8
S11=paises[2:4]
print(S11)
#EJER9
PLAN12=planetas[1:3]
print(PLAN12)
#EJER10
CAP13=capitales_sudamericanas[::-1]
print(CAP13)
#OPERACON 6 "LONGITUD":
#EJER1
print(len(animales))
#EJER2
print(len(paises))
#EJER3
print(len(capitales_sudamericanas))
#EJER4
print(len(vocales))
#EJER5
print(len(planetas))
#EJER6
print(len(regiones))
#EJER7
print(len(frutas))
#EJER8
verduras=["cebolla","lechuga","repollo","brocoli","alcachofa"]
print(len(verduras))
#EJER9
rios=["huallaga","marañon","ucayali","mayo","ene","perene"]
print(len(rios))
#EJER10
departamentos=["san martin","cuscu","la libertad","puno","cajamarca","piura","arequipa","tumbes","tacna","huancayo"]
print(len(departamentos))
#OPERACION8 "ITERACION"
#EJER1
for x in verduras:
    print(x)
#EJER2
for p in paises:
    print(p)
#EJER3
for f in frutas:
    print(f)
#EJER4
for a in animales:
    print(a)
#EJER5
for v in vocales:
    print(v)
#EJER6
for pln in planetas:
    print(pln)
#EJER7
for r in rios:
    print(r)
#EJER8
for c in capitales_sudamericanas:
    print(c)
#EJER9
for d in departamentos:
    print(d)
#EJER10
for R in regiones:
    print(R)
#OPERACION9 "BUSQUEDA":
#EJER1
print(frutas.index("platano"))
#EJER2
print(frutas.index("mamey"))
#EJER3
print(planetas.index("jupiter"))
#EJER4
print(rios.index("mayo"))
#EJR5
print(regiones.index("selva"))
#EJER6
print(departamentos.index("san martin"))
#EJER7
print(verduras.index("brocoli"))
#EJER8
print(animales.index("sachavaca"))
#EJER9
print(vocales.index("a"))
#EJER10
print(capitales_sudamericanas.index("asuncion"))
#OPERACION10 #CONTEO
#EJER1
print(frutas.count("platano"))
#EJER2
print(frutas.count("mamey"))
#EJER3
print(planetas.count("jupiter"))
#EJER4
print(rios.count("mayo"))
#EJR5
print(regiones.count("selva"))
#EJER6
print(departamentos.count("san martin"))
#EJER7
print(verduras.count("brocoli"))
#EJER8
print(animales.count("sachavaca"))
#EJER9
print(vocales.count("a"))
#EJER10
print(capitales_sudamericanas.count(""))
#OPERACION11 "MAX MIN":
#EJER1
print(max(verduras))
#EJER2
print(max(frutas))
#EJER3
print(max(paises))
#EJER4
print(max(capitales_sudamericanas))
#EJER5
print(max(planetas))
#EJER6
print(min(frutas))
#EJER7
print(min(verduras))
#EJER8
print(min(animales))
#EJER9
print(min(regiones))
#EJER10
print(min(departamentos))
#OPERACION12 "MULTIPLICASION":
#EJER1
print(animales*2)
#EJER2
print(animales*0)
#EJER3
print(verduras*1)
#EJER4
print(planetas*2)
#EJER5
print(departamentos*3)
#EJER6
print(paises*2)
#EJER7
print(rios*3)
#EJER8
print(regiones*4)
#EJER9
print(vocales*3)
#EJER10
print(capitales_sudamericanas*1)
#OPERACION13 "ELIMINACION":
#EJER1
del frutas[0:1]
frutas[0:1]=[]
print(frutas)
#EJER2
del universidades[0:1]
universidades[0:1]=[]
print(universidades)
#EJER3
del siglas[0:1]
siglas[0:1]=[]
print(siglas)
#EJER4
del animales[0:1]
animales[0:1]=[]
print(animales)
#EJER5
del rios[0:1]
rios[0:1]=[]
print(rios)
#EJER6
del regiones[0:1]
regiones[0:1]=[]
print(regiones)
#EJER7
del planetas[0:1]
planetas[0:1]=[]
print(planetas)
#EJER8
del capitales_sudamericanas[0:1]
capitales_sudamericanas[0:1]=[]
print(capitales_sudamericanas)
#EJER9
del paises[0:1]
paises[0:1]=[]
print(paises)
#EJER10
del verduras[0:1]
verduras[0:1]=[]
print(verduras)
#OPERACION14 "REEMPLAZO"
#EJER1
frutas[0]="banana"
print(frutas)
#EJER2
departamentos[1]="loreto"
print(departamentos)

#EJER3
regiones[0]="galapagos"
print(regiones)

#EJER4
animales[0]="cuy"
print(animales)

#EJER5
planetas[0]="nepturno"
print(planetas)

#EJER6
universidades[0]="unsm"
print(universidades)


#EJER7
vocales[0]="u"
print(vocales)



#EJER8
capitales_sudamericanas[0]="bogota"
print(capitales_sudamericanas)

#EJER9
paises[0]="canada"
print(paises)

#EJER10
verduras[0]="pepinillo"
print(verduras)
#OPERACION15 "AGREGADO":
#EJER1
verduras.append("culantro")
print(verduras)
#EJER2
regiones.append("bosque tropical del pacifico")
print(regiones)
#EJER3
frutas.append("mango")
print(frutas)
#EJER4
animales.append("gallito de las rocas")
print(animales)
#EJER5
vocales.append("A")
print(vocales)
#EJER6
planetas.append("saturno")
print(planetas)
#EJER7
universidades.append("villareal")
print(universidades)
#EJER8
rios.append("chancay")
print(rios)
#EJER9
capitales_sudamericanas.append("lima")
print(capitales_sudamericanas)
#EJER10
paises.append("dinamarca")
print(paises)
#OPERACION16 "ANULACION":
#EJER1
frutas.clear()
print(frutas)
#EJER2
capitales_sudamericanas.clear()
print(capitales_sudamericanas)
#EJER3
regiones.clear()
print(regiones)
#EJER4
rios.clear()
print(rios)
#EJER5
universidades.clear()
print(universidades)
#EJER6
departamentos.clear()
print(departamentos)
#EJER7
vocales.clear()
print(vocales)
#EJER8
verduras.clear()
print(verduras)
#EJER9
planetas.clear()
print(planetas)
#EJER10
paises.clear()
print(paises)
#OPERACON17 "CLONADO":
#EJER1
A=frutas.copy()
print(A)
#EJER2
B=verduras.copy()
print(B)
#EJER3
C=paises.copy()
print(C)
#EJER4
D=departamentos.copy()
print(D)

#EJER5
E=capitales_sudamericanas.copy()
print(E)
#EJER6
F=animales.copy()
print(F)
#EJER7
G=universidades.copy()
print(G)
#EJER8

H=siglas.copy()
print(H)
#EJER9

I=planetas.copy()
print(I)
#EJER10
J=vocales.copy()
J=vocales[:]
print(J)
#OPERACION18 "EXTENCION":
#EJER1
distritos=["cayalti","reque","ayotun","lagunas","tucume","illimo","mochumi"]
distritos.extend("olmos")
print(distritos)

#EJER2
distritos_moyobamba=["jepelacio","habana","soritor","yantalo","moyobamba"]
distritos_moyobamba.extend("x")
print(distritos)
#EJER3
distritos_rioja=["pocic","yurayacu","awuajun","nva cajamarca","rioja","jerusalen","yorongos"]
distritos_rioja.extend("j")
print(distritos_rioja)
#EJR4
actividades_productivas=["pisicultura","agricultura","ganaderia","silvicultura"]
actividades_productivas.extend("x")
print(actividades_productivas)
#EJER5
organizaciones_mundiales=["bm","apecp","unicef","fao","onu","unasur"]
organizaciones_mundiales.extend("HAYA")
print(organizaciones_mundiales)
#EJER6
ex_presidentes=["Belaunde Terry","Velasco Alvarado","Ramon Castilla","Nicolas de Pierola","Agusto Belegia"]
ex_presidentes.extend("alan garcia")
print(ex_presidentes)
#EJER7
amigos=["pedro","juan","alonso","ramiro","rosa","yuly","elita","martita"]
amigos.extend("julio")
print(amigos)
#EJER8
filosofos=["socrates","pitagoras","platon","decartes","epicuro","aristoteles","kant"]
filosofos.extend("jhon luck")
print(filosofos)
#EJER9
formas_societarias=["irl","sociedades","eirl","unipersonal","colectiva","civil"]
formas_societarias.extend("sac")
print(formas_societarias)
#EJER10
tipos_mercado=["temporal","mayorista","minorista","negro","cerrado","abierto"]
tipos_mercado.extend("controlado")
#OPERACION19 "INSERCION"
#EJER1
tipos_mercado.insert(0,"negro")
print(tipos_mercado)
#EJER2
amigos.insert(0,"alberto")
print(tipos_mercado)

#EJER3
distritos.insert(0,"lagunas")
print(distritos)

#EJER4
distritos_moyobamba.insert(0,"ucrania")
print(distritos_moyobamba)

#EJER5
distritos_rioja.insert(0,"nueva rioja")
print(distritos_rioja)

#EJER6
actividades_productivas.insert(0,"orfebreria")
print(actividades_productivas)

#EJER7
formas_societarias.insert(0,"encomandita")
print(formas_societarias)

#EJER8
filosofos.insert(0,"democrito")
print(filosofos)


#EJER9
organizaciones_mundiales.insert(0,"union eropea")
print(organizaciones_mundiales)

#EJER10
ex_presidentes.insert(0,"")
print(ex_presidentes)


#OPERACION 20 "EXTRACION"
#EJER1
pro=["alchol","bicarbota de sodio","acido benzoico","oxido de zinc","azucar blanco","amoniaco","acido borico","agua oxigenada"]
x1=pro.pop(0)
#EJER2
x2=pro.pop(1)
#EJER3
x3=pro.pop(2)
#EJER4
x4=pro.pop(3)
#EJER5
fs=["anuje","majas","venado","armadillo"]
x5=fs.pop(0)
#EJER6
x6=fs.pop(2)
#EJER7
x7=fs.pop(1)
#EJER8
hojas=["A1","A2","A3","A4","A5"]
X8=hojas.pop(0)
#EJER9
x9=hojas.pop(1)
#EJER10
x10=hojas.pop(2)

#OPERACION 21 "SEPARACION"
#EJER1
LISTA1=[1,3,45,45]
LISTA1.remove(1)
#EJE2
LISTA2=[12,34,56,67]
LISTA2.remove(12)
#EJER3
LISTA3=[45,23,46,67]
LISTA3.remove(46)
#EJER4
LISTA4=[2,89,67,45]
LISTA4.remove(67)
#EJER5
LISTA5=[7,43,23,45,]
LISTA5.remove(23)
#EJER6
LISTA6=[56,45,123]
LISTA6.remove(123)
#EJER7
LISTA7=[456,23,678]
LISTA7.remove(23)
#EJER8
LISTA8=[2345,6789]
LISTA8.remove(6789)
#EJER9
LISTA9=[12,89.9,23]
LISTA9.remove(89.9)

#EJER10
LISTA10=[5678,4325,567]
LISTA10.remove(567)

#OPERACION 22 "RESERVA"
#EJER1
Y1=LISTA1.reverse()
#EJER2
Y2=LISTA2.reverse()
#EJER3
Y3=LISTA3.reverse()
#EJER4
Y4=LISTA4.reverse()
#EJER5
Y5=LISTA5.reverse()
#EJER6
Y6=LISTA6.reverse()
#EJER7
Y7=LISTA7.reverse()
#EJER8
Y8=LISTA8.reverse()
#EJER9
Y9=LISTA9.reverse()
#EJER10
Y10=LISTA10.reverse()
#OPERACION 23 "SORT
#EJER1
LISTA1.sort()
#EJER2
LISTA2.sort()
#EJER3
LISTA3.sort()
#EJER4
LISTA4.sort()
#EJER5
LISTA5.sort()
#EJER6
LISTA6.sort()
#EJER7
LISTA7.sort()
#EJER8
LISTA8.sort()
#EJER9
LISTA9.sort()
#EJER10
LISTA10.sort()

#FIN ,FIN



