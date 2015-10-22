# -*- coding: utf-8 -*-

from os import system,name
from time import sleep

def clear():
	system("clear") if name == "poxis" else system("cls")
	
def mostrar_titulo():
	clear()
	print "-"*14+"\n"+"|- AHORCADO -|"+"\n"+"-"*14+"\n"

def pintar_monigote(v):
	print "   --------------  "
	print "  |    _________/"
	print "  |   |" if v == 5 else "  |   |        |"
	print "  |   |" if v == 5 else "  |   |       -^-"
	print "  |   |" if v == 5 else "  |   |      (x x)"
	print "  |   |" if v == 5 else "  |   |       ---"
	print "  |   |" if v >= 4 else "  |   |        |----" if v >= 3 else "  |   |    ----|----"
	print "  |   |" if v >= 2 else "  |   |        |"
	print "  |   |" if v >= 2 else "  |   |         \\" if v >= 1 else "  |   |       / \\"
	print "  |   |" if v >= 2 else "  |   |          \\" if v >= 1 else "  |   |      /   \\"
	print " /_____\\"
	print "\n"
	

mostrar_titulo()

print "\nIntroduce a palabra:\n"

palabra = raw_input(">> ").strip().lower()

letras = len(palabra)*"*"

letras_empregadas = []

vida = 5

while(True):

	mostrar_titulo()
	
	print "vida:",vida,"\n"
	
	pintar_monigote(vida)
	
	print " ".join(["".join(l) for l in letras])
	print "_ "*len(palabra)

	if vida > 0 and letras != palabra:
		print "\nEscribe unha letra e pulsa INTRO\n"
	
	if vida > 0 and letras!=palabra:
		letra = raw_input(">> ")
		
	if letra != "":
		letra = letra[0].lower()
		
	if vida > 0 and letras!=palabra:
		if letra not in letras_empregadas and letra != "":
			if letra in palabra:
				letras = "".join(["".join(palabra[nl]) if letra==palabra[nl] or letras[nl]!="*" 
						else "".join("*") for nl in range(len(palabra))])
			
				print "\nNoraboa! A letra esta na palabra"
				letras_empregadas.append(letra)
				
			else:
				print "\nLastima! A letra %r NON esta na palabra" % (letra)
				letras_empregadas.append(letra)
				vida -= 1
				
		elif letra == "":
			print "\nEscribe unha letra!"
			
		else:
			print "\nLetra repetida! Xa escribiches antes esta letra"
			
	elif vida <= 0:
		print "\n"+"*"*15+"\nMorriches!"
		
	else:
		print "\n"+"*"*15+"\nTriunfaches!"
		
	raw_input()
		