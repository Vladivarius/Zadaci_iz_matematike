import random
import os

#Napravi txt fajl koji se zove isto kao python skripta
f = open(os.path.basename(__file__)[:-3] + ".txt", "w")

for i in range(1,30):
	a = random.randint(1,9)
	b = random.randint(1, 99)
	b = b/10
	f.write(str(a) + " + " + str(b) + " = " + "\n")

f.close()