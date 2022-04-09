def anagramaSolucion2(cadena1,cadena2):
  unaLista1 = list(cadena1)
  print('1')
  unaLista2 = list(cadena2)
  print('2')
  unaLista1.sort()
  print('3')
  unaLista2.sort()
  print('4')
    
  pos = 0
  print('5')
  coincide = True
  print('6')
  while pos < len(cadena1) and coincide:
    print('7 y 8')
    if unaLista1[pos]==unaLista2[pos]:
      print('9')
      pos = pos + 1
      print('10')
    else:
      print('11')
      coincide = False
  print('12')
  return coincide

# *** Test 1 Cobertura de sentencia ***
#print("*** Test 1 ***")
#anagramaSolucion2('pepa', 'pena')
# ***  Caminos 100 %  ***
#1-2-3-4-5-6-7 y 8-9-10-7 y 8-9-10-7 y 8-11-12

# *** Test 2 Cobertura de Desicion ***
#print("*** Test 2 *** Siempre IF")
#anagramaSolucion2('asado', 'osada')
#1-2-3-4-5-6-7 y 8-9-10-7 y 8-9-10-7 y 8-9-10-7 y 8-9-10-7 y 8-9-10-12

# *** Test 3 Cobertura de Desicion ***
#print("*** Test 2 *** Siempre Else")
#anagramaSolucion2('oso', 'ada')
#1-2-3-4-5-6-7 y 8-11-12

# *** Test 3 Cobertura de Desicion ***
#print("*** Test 2 *** Siempre Else")
#anagramaSolucion2('oso', 'ada')
#1-2-3-4-5-6-7 y 8-11-12
