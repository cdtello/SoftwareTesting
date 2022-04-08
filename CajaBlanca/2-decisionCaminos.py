def anagramaSolucion4(cadena1,cadena2):
  c1 = [0]*26
  c2 = [0]*26

  for i in range(len(cadena1)):
    print('into for 1')
    pos = ord(cadena1[i])-ord('a')
    c1[pos] = c1[pos] + 1

  for i in range(len(cadena2)):
    print('into for 2')
    pos = ord(cadena2[i])-ord('a')
    c2[pos] = c2[pos] + 1
  
  j = 0
  aunOK = True
  print(c1)
  print(c2)
  while j<26 and aunOK:
    print('into while')
    if c1[j]==c2[j]:
      print('into while -> if')
      j = j + 1
    else:
      print('into while -> else')
      aunOK = False

  return aunOK

# *** Test 1 Cobertura de sentencia ***
print("*** Test 1 ***")
anagramaSolucion4('pepe', 'pedro')
# ***  Caminos 100 %  ***
