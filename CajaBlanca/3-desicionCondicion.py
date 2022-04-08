def anagramaSolucion2(cadena1,cadena2):
  unaLista1 = list(cadena1)
  unaLista2 = list(cadena2)

  unaLista1.sort()
  unaLista2.sort()

  print(unaLista1)
  print(unaLista2)
  
  pos = 0
  coincide = True

  while pos < len(cadena1) and coincide:
    print("into while")
    if unaLista1[pos]==unaLista2[pos]:
      print("into while -> if")
      print(unaLista1[pos])
      print(unaLista2[pos])
      pos = pos + 1
    else:
      coincide = False
      print("into while -> else ")
  return coincide

# *** Test 1 Cobertura de sentencia ***
print("*** Test 1 ***")
anagramaSolucion2('pepa', 'pena  ')
# ***  Caminos 100 %  ***