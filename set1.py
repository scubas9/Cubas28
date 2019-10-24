#un programa donde involucra operaciones con set
frutas={"manzana","lima","durazno","fresa","ciruela","lima"}
frutas_preferidas=frutas.copy()
#agrgaremos otra fruta preferida
frutas_preferidas.add("zapote")
#ahora ordenaremos el set
set(sorted(frutas_preferidas))
print(len(frutas_preferidas))
for x in frutas_preferidas:
    print(x)
