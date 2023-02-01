kmh = [40,60,80,100,110,120,140,160,180]
mph = list(map(lambda x: x/1.61,kmh))
print(mph)
mph2 = [x/1.61 for x in kmh]
print(mph2)
caracteres = [i for i in 'Didatica teste']
print(caracteres)