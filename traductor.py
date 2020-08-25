from syl_module import silabizer

s = silabizer()
palabra = "estoy hablando en jeringoso y probando la letra y"
palabraEnSilabas = s(palabra)
print(palabraEnSilabas)
palabraEnJeringozo = ""

for silaba in palabraEnSilabas:
	stringSilaba = str(silaba).strip()
	#print(stringSilaba)
	if "a" in stringSilaba:
		palabraEnJeringozo += stringSilaba
		palabraEnJeringozo += "pa "

	elif "e" in stringSilaba:
		palabraEnJeringozo += stringSilaba
		palabraEnJeringozo += "pe "
		
	elif "i" in stringSilaba:
		palabraEnJeringozo += stringSilaba
		palabraEnJeringozo += "pi "
		
	elif "o" in stringSilaba:
		palabraEnJeringozo += stringSilaba
		palabraEnJeringozo += "po "
		
	elif "u" in stringSilaba:
		palabraEnJeringozo += stringSilaba
		palabraEnJeringozo += "pu "

	elif "y" in stringSilaba:
		palabraEnJeringozo += stringSilaba
		palabraEnJeringozo += "pi "


print(palabraEnJeringozo)
