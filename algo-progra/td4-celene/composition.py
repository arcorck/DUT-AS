def composition_chiffre (chiffre) :
    """Cette fonction renvoie un int qui indique le nombre de chiffres qui composent le nombre passé en paramètre"""
    res = 1
    while chiffre > 9 or chiffre < -9:
        res += 1
        chiffre = chiffre // 10
    return res

 
assert composition_chiffre(123456789)
assert composition_chiffre(12345678)
assert composition_chiffre(1234567)
assert composition_chiffre(123456)
assert composition_chiffre(12345)
assert composition_chiffre(1234)
assert composition_chiffre(123)
assert composition_chiffre(12)
assert composition_chiffre(1)
assert composition_chiffre(-1)
assert composition_chiffre(-12)
assert composition_chiffre(-123)
assert composition_chiffre(-1234)
assert composition_chiffre(-12345)
assert composition_chiffre(-123456)
assert composition_chiffre(-1234567)
assert composition_chiffre(-12345678)
assert composition_chiffre(-123456789)   

print(composition_chiffre(123456789))
print(composition_chiffre(12345678))
print(composition_chiffre(1234567))
print(composition_chiffre(123456))
print(composition_chiffre(12345))
print(composition_chiffre(1234))
print(composition_chiffre(123))
print(composition_chiffre(12))
print(composition_chiffre(1))
print(composition_chiffre(-1))
print(composition_chiffre(-12))
print(composition_chiffre(-123))
print(composition_chiffre(-1234))
print(composition_chiffre(-12345))
print(composition_chiffre(-123456))
print(composition_chiffre(-1234567))
print(composition_chiffre(-12345678))
print(composition_chiffre(-123456789))