from syl_module import silabizer

s = silabizer()
palabra = "estoy hablando en jeringoso y probando la letra y"
palabraEnSilabas = s(palabra)
print(palabraEnSilabas)
palabraEnJeringoso = ""

for silaba in palabraEnSilabas:
	stringSilaba = str(silaba).strip()
	#print(stringSilaba)
	if "a" in stringSilaba:
		palabraEnJeringoso += stringSilaba
		palabraEnJeringoso += "pa "

	elif "e" in stringSilaba:
		palabraEnJeringoso += stringSilaba
		palabraEnJeringoso += "pe "
		
	elif "i" in stringSilaba:
		palabraEnJeringoso += stringSilaba
		palabraEnJeringoso += "pi "
		
	elif "o" in stringSilaba:
		palabraEnJeringoso += stringSilaba
		palabraEnJeringoso += "po "
		
	elif "u" in stringSilaba:
		palabraEnJeringoso += stringSilaba
		palabraEnJeringoso += "pu "

	elif "y" in stringSilaba:
		palabraEnJeringoso += stringSilaba
		palabraEnJeringoso += "pi "


print(palabraEnJeringoso)
