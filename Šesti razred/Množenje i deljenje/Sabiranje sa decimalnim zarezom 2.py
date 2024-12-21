import random

for i in range(1,30):
	a = random.randint(1,99)
	a = a/10
	b = random.randint(1, 99)
	b = b/10
	print(str(i) + ") " + str(a) + " + " + str(b) + " = ")