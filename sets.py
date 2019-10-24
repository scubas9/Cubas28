#OPERACION1 "CREACION"
#EJER1
st1=set()
print(st1)
#ejer2
st2={2,3,4,5}
print(st2)
#ejer3
st3={"manzana","platano","uva","cerezza"}
print(st3)
#ejer4
st4={"a","b","c","d"}
print(st4)
#ejer5
st5={"loro","oso","pantera"}
print(st5)
#ejer6
st6={"peru","colombia","portugal"}
print(st6)
#ejer7:
st7=set()
print(st7)
#ejer8
st8={"calculadora","usb","lactop","mochila"}
print(st8)
#ejer9:
st9={"chaleadora","motor","despulpadora","machete"}
print(st9)
#ejer19
st10={"legislativo","judicial","ejecutivo"}
print(st10)
#OPERACION 2 "PERTENENCIA":
#EJER1
print("legislativo" in st10)
#ejer2
print("judicial" in st10)
#ejer3
print("chaleadora" not in st9)
#ejer4
print("calculadora" not in st8)
#ejer5
print("oso" in st7)
#ejer6:
print("laptop" in st7)
#ejer7:
print("peru" in st2)
#ejer8
print("cereza" in st3)
#ejer9
print("cerrezza" not in st2)
#ejer10
print("b" in st3)
#OPERACION 3 "COMPARACION
#EJER1
print(st1==st2)
#ejer2
print(st2>st1)
#ejer3
print(st3>st2)
#ejer4
print(st3!=st4)
#ejer5
print(st5==st6)
#ejer6
print(st7!=st8)
#ejer7
print(st10!=st6)
#ejer8
print(st2>st8)
#ejer9
print(st9!=st5)
#ejer10
print(st10==st9)

#OPERACION4 "LONGITUD":
#EJE1
print(len(st1))
#EJER2
print(len(st2))
#EJER3
print(len(st3))
#EJER4
print(len(st4))
#EJER5
print(len(st5))
#EJER6
print(len(st6))
#EJR7
print(len(st7))
print(len(st8))
#EJER8
print(len(st9))
#EJER9
print(len(st9))
#EJER10
print(len(st10))
#OPERACION 5: "ITERACION":
#ejer1
for x in st1:
    print(x)
#ejer2
for x in st2:
    print(x)
#ejer3
for x in st3:
    print(x)
#ejer4
for x in st4:
    print(x)
#ejer5
for x in st5:
    print(x)
#ejer6
for x in st6:
    print(x)
#ejer7
for x in st7:
    print(x)
    #ejer8
for x in st8:
    print(x)
#ejer9
for x in st9:
    print(x)
#ejer10

for x in st10:
    print(x)
#OPERACION 6 "MAX MIN":
#EJER1
st0={"papa","hijos","tios"}
p=max(st0)
print(p)
#EJER2
print(max(st2))
#EJER3
print(max(st3))
#EJER4
print(max(st4))
#EJER5
print(max(st5))
#EJER6
print(min(st6))
#EJER7
st17={"abismado","visitudes","funesto","enteco"}
print(min(st17))
#EJER8
print(min(st8))
#EJER9
print(min(st9))
#EJER10
print(min(st10))
#OPERACION 7 "eliminacion"

#ejer1
artef={"camara","tablet","telivisor","computadora","impresora"}
artef.discard("impresora")
print(artef)
#ejer2
notas={"do","re","mi","fa","sol"}
notas.discard("re")
print(notas)
print(notas)
#ejer3
años={2017,2019,2020,2015,2016}
años.discard(2017)
print(años)
#ejer4
lugares={"cancun","cusco","laguna azul","chan chan","duwai"}
lugares.discard("duwai")
print(lugares)
#jer5
apellidos={"chavez","huaman","vazques","barboza","gerrero"}
apellidos.discard("huaman")
print(apellidos)
#ejer6
profesiones={"doctor","ingeniero","periodista","enfermero","docente"}
profesiones.discard("ingeniero")
print(profesiones)
#ejer7
cantantes={"ozuna","leodan","jose jose","maluma","cholo derrocal"}
cantantes.discard("maluma")
print(cantantes)
#ejer8
intrumentos={"bateria","bajo","tinbales","piano","bateria"}
intrumentos.discard("tinbales")
print(intrumentos)
#ejer9
tios={"juan","pedro","kelvin","alonso","francisco"}
tios.discard("kelvin")
print(tios)
#ejer10
radios={"kariveña","tropicana","incassac","rpp","onda cero"}
radios.discard("onda cero")
print(radios)

#OPERACION8 "AGREGADO"
#EJER1
artef.add("inpresora")
print(artef)
#EJER2
notas.add("re")
print(notas)
#EJER3
años.add(2017)
print(años)
#EJER4
lugares.add("duwai")
print(lugares)
#EJER5
apellidos.add("huaman")
print(apellidos)
#EJER6
profesiones.add("ingeniero")
print(profesiones)
#EJER7
cantantes.add("maluma")
print(cantantes)

#EJER8
intrumentos.add("tinbales")
print(intrumentos)
#EJER9
tios.add("kelvin")
print(tios)
#EJER10
radios.add("onda cero")
print(radios)

#OPERACION9 "ANULACION"
#EJER1
artef.clear()
print(artef)
#EJER2
notas.clear()
print(notas)
#EJER3
años.clear()
print(años)
#EJR4
lugares.clear()
print(lugares)
#EJER5
apellidos.clear()
print(apellidos)
#EJER6
profesiones.clear()
print(profesiones)
#EJER7
cantantes.clear()
print(cantantes)
#EJER8
intrumentos.clear()
print(intrumentos)
#EJER9
tios.clear()
print(tios)
#EJR10
radios.clear()
print(radios)

#OPERACION10 "CLONADO"
#EJER1
saludos={"hola","hi","buen dia","good afternoon"}
sal=saludos.copy()
print(sal)
#EJE2
empresas={"gloria","alicor","obrainza","odebrect"}
empr=empresas.copy()
#EJER3
numeros={12,34,45,56}
num=numeros.copy()
print(num)
#EJER4
cursos={"ingles","calculo","mate basica","identidad nacional"}
cur=cursos.copy()
print(cur)
#EJER5
ferreteria={"clavos ","martillo","grapas","alambre"}
ferre=ferreteria.copy()
print(ferre)

#EJER6
comedor={"utensillos","olla","sarten","gas","servilleta"}
com=comedor.copy()
print(com)
#EJER7
sala={"sofa","televisor","parlante","vino"}
sa=sala.copy()
print(sa)
#EJER8
deportes={"futbol","basquet","voley","natacion"}
depor=deportes.copy()
print(depor)
#EJER9
fauna={"venado","pava aliblanca","zorro","ardilla"}
faou=fauna.copy()
print(faou)
#EJER10
flora={"quina","cedro","caoba","muena","romerillo","rifar","algarrobo","huacapu"}
flo=flora.copy()
print(flo)
#OPERACION11 "EXTRACION":
#EJER1
flo=flora.pop()
print(flo)
#EJER2
ferre=ferreteria.pop()
print(ferre)


#EJER3
empr=empresas.pop()
print(empr)
#EJER4
num=numeros.pop()
print(num)
#EJER5
sal=saludos.pop()
print(sal)
#EJER6
com=comedor.pop()
print(com)
#EJER7
cur=cursos.pop()
print(cur)
#EJER8
sa=sala.pop()
print(sa)
#EJER9
depor=deportes.pop()
print(depor)
#EJER10
faou=fauna.pop()
print(faou)

#OPERACION12 "ordenado"
#EJER1
platos={"arroz con pato","juanes","tamales"}
print(set(sorted(platos)))
#EJER2
modificadores={"md","mi","od","oi"}
print(set(sorted(modificadores)))
#ejer3
sustantivos={"peru","casa","libro"}
print(set(sorted(sustantivos)))
#ejer4
verbos={"hacer","estudiar","conocer"}
print(set(sorted(verbos)))
#ejer5
abjetivos={"alto","gordo","bonito"}
print(set(sorted(abjetivos)))
#ejer6
pre={"pierola","legia","belaunde"}
print(set(sorted(pre)))
#ejer7
estaciones={"invierno","verano","primavera","otoño"}
print(set(sorted(estaciones)))
#ejer8
climas={"templado","humedo","tropical"}
print(set(sorted(climas)))
#ejer9

lugarex={"cusco","cuela","gran pajaten"}
print(set(sorted(lugarex)))
#ejer10
animales={"guacamayo","loro","pava aliblanca"}
print(set(sorted(animales)))
#OPERACION "UNION"
#EJER1
uni1=animales.union(lugarex)
#EJER2
uni2=lugarex.union(estaciones)
#EJER3
uni3=estaciones.union(cursos)
#EJER4
uni4=empresas.union(cursos)
#EJER5
uni5=estaciones.union(empresas)
#EJER6
uni6=platos.union(pre)
#EJER7
uni7=lugarex.union(abjetivos)
#EJER8
uni8=sustantivos.union(abjetivos)
#EJER9
uni9=abjetivos.union(modificadores)
#EJER10
uni10=modificadores.union(verbos)

#OPERACION "DIFERENCIA"
#EJER1
x=abjetivos-sustantivos
#EJER2
x1=sala-cursos
#EJER3
x2=saludos-sustantivos
#EJER4
x3=lugarex-lugarex
#EJER5
x4=animales-abjetivos
#EJER6
x5=estaciones-empresas
#EJER7
x6=empresas-lugares
#EJER8
x7=años-apellidos
#EJER9
x8=años-animales
#EJER10
x9=radios-platos
#OPERACION "DIFERENCIA SIMETRICA"
x9=radiosplatos



