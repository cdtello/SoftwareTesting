def anagramaSolucion4(cadena1,cadena2):
  c1 = [0]*26
  print('1')
  c2 = [0]*26
  print('2')

  for i in range(len(cadena1)):
    print('3')
    pos = ord(cadena1[i])-ord('a')
    print('4')
    c1[pos] = c1[pos] + 1
    print('5')
  for i in range(len(cadena2)):
    print('6')
    pos = ord(cadena2[i])-ord('a')
    print('7')
    c2[pos] = c2[pos] + 1
    print('8')
  j = 0
  print('9')
  aunOK = True
  print('10')
  while j<26 and aunOK:
    print('11 y 12')
    if c1[j]==c2[j]:
      print('13')
      j = j + 1
      print('14')
    else:
      print('15')
      aunOK = False
  print('16')
  return aunOK

# *** Test 1 Cobertura de sentencia ***
print("*** Test 1 ***")
print(anagramaSolucion4('pepe', 'pedro'))
# ***  Caminos 100 %  ***
#1-2-3-4-5-3-4-5-3-4-5-3-4-5-6-7-8-6-7-8-6-7-8-6-7-8-6-7-8-9-10-11-12-13-14-11-12-13-14-11-12-13-14-11-12-15-16