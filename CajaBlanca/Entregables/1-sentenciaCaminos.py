def anagramaSolucion1(cadena1,cadena2):
  unaLista = list(cadena2)
  print('1')
  pos1 = 0
  print('2')
  aunOK = True
  print('3')
  while pos1 < len(cadena1) and aunOK:
    print('4 y 5')
    pos2 = 0
    print('6')
    encontrado = False
    print('7')
    while pos2 < len(unaLista) and not encontrado:
      print('8 y 9')
      if cadena1[pos1] == unaLista[pos2]:
        print('10')
        encontrado = True
        print('11')
      else:
        pos2 = pos2 + 1
        print('12')

    if encontrado:
      print('13')
      unaLista[pos2] = None
      print('14')
    else:
      aunOK = False
      print('15')

    pos1 = pos1 + 1
    print('16')
  print('17')
  return aunOK


# *** Test 1 Cobertura de sentencia ***
print("*** Test 1 ***")
print(anagramaSolucion1('pepe', 'pera'))
# ***  Caminos 100 %  ***

#1-2-3-4-5-6-7-8-9-10-11-13-14-16-4-5-6-7-8-9-12-8-9-10-11-13-14-16-4-5-6-7-8-9-12-8-9-12-8-9-12-8-9-12-15-16-17

# *** Test 2 Cobertura de Caminos ***
print("*** Test 2 ***")
print(anagramaSolucion1('fresa', 'frase'))
#1-2-3-4-5-6-7-8-9-10-11-13-14-16-4-5-6-7-8-9-12-8-9-10-11-13-14-16-4-5-6-7-8-9-12-8-9-12-8-9-12-8-9-12-8-9-10-11-13-14-16-4-5-6-7-8-9-12-8-9-12-8-9-12-8-9-10-11-13-14-16-4-5-6-7-8-9-12-8-9-12-8-9-10-11-13-14-16-17

# *** Test 3 Cobertura de Caminos ***
print("*** Test 3 ***")
print(anagramaSolucion1('roca', 'caro'))
#1-2-3-4-5-6-7-8-9-12-8-9-12-8-9-10-11-13-14-16-4-5-6-7-8-9-12-8-9-12-8-9-12-8-9-10-11-13-14-16-4-5-6-7-8-9-10-11-13-14-16-4-5-6-7-8-9-12-8-9-10-11-13-14-16-17
# *** Test 4 Cobertura de Caminos ***
print("*** Test 4 ***")
print(anagramaSolucion1('ana', 'oka'))
#1-2-3-4-5-6-7-8-9-12-8-9-12-8-9-10-11-13-14-16-4-5-6-7-8-9-12-8-9-12-8-9-12-15-16-17