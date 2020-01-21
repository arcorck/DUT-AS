def test1 (x,y,z):
	trace = 'je suis passé par'
	if (x<y):
		trace = trace + ' x<y'
	else:
		trace = trace + ' x>=y'
		if (y<z):
			trace = trace + ' y<z'
		else:
			trace = trace + ' z<=y'
			if (x<z):
				trace = trace + ' x<z'
			else:
				trace = trace + ' x>=z'
	return trace

def test2 (x,y,z):
	trace = 'je suis passé par'
	if (x<y):
		trace = trace + ' x<y'
	else:  
		trace = trace + ' x>=y'
	if (y<z):
		trace = trace + ' y<z'
	else:
		trace = trace + ' z<=y'
	if (x<z):
		trace = trace + ' x<z'
	else:
		trace = trace + ' x>=z'
	return trace

print("x = 12, y = 14, z = 18")
print("test 1 : ", test1(12,14,18))
print("test 2 : ", test2(12,14,18), "\n\n")
print("x = 18, y = 12, z = 14")
print("test 1 : ", test1(18,12,14))
print("test 2 : ", test2(18,12,14), "\n\n")
print("x = 14, y = 12, z = 18")
print("test 1 : ", test1(14,12,18))
print("test 2 : ", test2(14,12,18))

#Exercice 1
#1)Dans l'algo test2, on a pas d'imbrication des conditionnelles, 
#ce qui veut dire qu'il va rentrer dans chaque conditionnelle (soit dans le if soit dans le else)
#alors que pour test1 il ne va pas tout tester grâce aux conditionnelles imbriquées