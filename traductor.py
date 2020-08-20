from syl_module import silabizer

s = silabizer()
p = "esto traduce un texto a jeringozo"
l = s(p)
print(l)
res = ""

for sil in l:
	ger = str(sil).strip()
	#print(ger)
	if "a" in ger:
		res += ger
		res += "pa "

	elif "e" in ger:
		res += ger
		res += "pe "
		
	elif "i" in ger:
		res += ger
		res += "pi "
		
	elif "o" in ger:
		res += ger
		res += "po "
		
	elif "u" in ger:
		res += ger
		res += "pu "

print(res)
