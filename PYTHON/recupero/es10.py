def ricerca_binaria(lista, target):
  
  sinistra = 0
  destra = len(lista) - 1

  while sinistra <= destra:

    centro = (sinistra + destra) // 2

    if lista[centro] == target:
      return centro
    
    elif lista[centro] < target:
      sinistra = centro + 1

    else:
      destra = centro - 1

  return -1

print(ricerca_binaria([1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9], 6))