def anagramaSolucion1(cadena1,cadena2):
  unaLista = list(cadena2)
  pos1 = 0
  aunOK = True

  while pos1 < len(cadena1) and aunOK:
    print('into while 1')
    pos2 = 0
    encontrado = False

    while pos2 < len(unaLista) and not encontrado:
      print('into while 2')
      if cadena1[pos1] == unaLista[pos2]:
        print('into while 2 -> if')
        encontrado = True
      else:
        print('into while 2 -> else')
        pos2 = pos2 + 1

    if encontrado:
      print('into while 1 -> if')
      unaLista[pos2] = None
    else:
      print('into while 1 -> else')
      aunOK = False

    pos1 = pos1 + 1
  return aunOK


# *** Test 1 Cobertura de sentencia ***
print("*** Test 1 ***")
anagramaSolucion1('pepe', 'pera')
# ***  Caminos 100 %  ***