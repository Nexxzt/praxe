x = input("Zadej hodnotu: ")
res = {}
dvojte = []
print("\n")
if x.isalpha():
	for i in x:
		res[i] = x.count(i)
	for char in x:
		if x.count(char) > 1:
			if char not in dvojte:
				dvojte.append(char)

	delka = len(x)
	prvni = x[0]
	posledni = x[-1]
	print("První znak je: ",prvni)
	print("Poslední znak je: ",posledni)
	print("Pocet znaku je: ", delka)
	print(f"Znaky a jejich pocet v retezci: {res}")
	print(f"Opakujici se znaky vice nez 1: {dvojte}")
		
else:
	list1 = x.split()

	for i in range(len(list1)):
		list1[i] = int(list1[i])

	print("Suma = ",sum(list1))
	print("Prumer = ",sum(list1)/len(list1))
	print("Maximum z čísel je: ",max(list1))
	print("Minimum z čísel je: ",min(list1))

cisla = sum(c.isdigit() for c in x)
pismena = sum(c.isalpha() for c in x)
mezery  = sum(c.isspace() for c in x)
ostatni  = len(x) - cisla - pismena - mezery

print("Počet číslic v řetězci: ", cisla)
print("Počes písmen v řetězci: ", pismena)
print("Počet mezer v řetězci: ", mezery)
print("Ostatní: ", ostatni)







