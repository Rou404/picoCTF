import re
alph = [x for x in "abcdefghijklmnopqrstuvwxyz"]

result = []

def rot13decoder(mystring):
	for i in range(len(alph)):
		if i < 13:
			result.append(alph[26-abs(i-13)])
		else:
			result.append(alph[i-13])
	return "".join(result)

print(rot13decoder("cvpbPGS"))