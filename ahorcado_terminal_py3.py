import os
import platform
import random


ascii_hangman01 = """
             ______
            |_____ |
             |    ||
                  ||
                  ||
                  ||
                 /||
                / ||
          _____/__||___
"""

ascii_hangman02 = """
             ______
            |_____ |
            _|_   ||
            |_|   ||
                  ||
                  ||
                 /||
                / ||
          _____/__||___
"""

ascii_hangman03 = """
             ______
            |_____ |
            _|_   ||
            |_|   ||
             |    ||
             |    ||
                 /||
                / ||
          _____/__||___
"""

ascii_hangman04 = """
             ______
            |_____ |
            _|_   ||
            |_|   ||
            \|/   ||
             |    ||
                 /||
                / ||
          _____/__||___
"""

ascii_hangman05 = """
             ______
            |_____ |
            _|_   ||
            |x|   ||
            \|/   ||
             |    ||
            / \  /||
                / ||
          _____/__||___
"""

ascii_hangman_list = [ascii_hangman01,ascii_hangman02,ascii_hangman03,
			ascii_hangman04,ascii_hangman05]

#None => None
def clear():
	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux":
		os.system("clear")

#String => String		
def no_accents(text):
	changes = {("Á","À","Ä","Â"):"A",
			   ("É","È","Ë","Ê"):"E",
			   ("Í","Ì","Ï","Î"):"I",
			   ("Ó","Ò","Ö","Ô"):"O",
			   ("Ú","Ù","Ü","Û"):"U"}
	no_accents_text = ""
	for word in text.upper():
		if word in sum(changes,()):
			no_accents_text += [v for k,v in changes.items()
									if word in k][0]
		else:
			no_accents_text += word
	return no_accents_text
	
#None => String/False, String
def input_letra():
	try:
		letra = input("\n\nVamos! Dime un Letra: ")
	except KeyboardInterrupt:
		print("\n\nBye!")
		exit()
	except:
		print("\nBye!")
		exit()
	if len(letra) == 1 and letra.isalpha():
		return no_accents(letra),""
	else:
		mensaje = "Debes escribir una letra!"
		return False, mensaje

#None => True/False
def remake():
	try:
		respuesta = input("\n\nQuieres probar suerte otra vez (s/n)?: ")
	except KeyboardInterrupt:
		print("\n\nBye!")
		exit()
	except:
		print("\nBye!")
		exit()
	if respuesta.upper() == "S":
		return True
	elif respuesta.upper() == "N":
		print("\nBye!")
		exit()
	else:
		return False
	
#String, Int, List => None (print)
def show_game(msx,errors,word):
	clear()
	print("\n{0}  H A N G M A N  {0}".format("¿"*8))
	print("\n> "+msx)
	print(ascii_hangman_list[errors])
	print("La palabra oculta es: ",end="")
	for w,v in word:
		if v==1:
			print(w,end=" ")
		else:
			print("_",end=" ")
	print()

#None => String
def load_words():
	file_name = "words.txt"
	file_text = open(file_name,"r", encoding="utf-8").read()
	words = file_text.split()
	word = random.choice(words).upper()
	return [[w,0] for w in word]
	
#None => List, Int, String, List
def cargar_valores():
	return load_words(), 0, "", []
	
def main():
	max_errors = 4
	palabra, errors, mensaje, letras_usadas = cargar_valores()
	while 1:
		show_game(mensaje,errors,palabra)
		#WIN
		if all((v for w,v in palabra)):
			mensaxe = "Enhorabuena! HAS GANADO!"
			show_game(mensaje,errors,palabra)
			if remake():
				palabra, errors, mensaje, letras_usadas = cargar_valores()
		#LOOSE	
		elif errors == max_errors:
			mensaje = "Lo siento, Has perdido..."
			mensaje += "\n  La palabra era: {}".format(
						"".join((w for w,v in palabra)))
			show_game(mensaje,errors,palabra)
			if remake():
				palabra, errors, mensaje, letras_usadas = cargar_valores()
		#STILL GAME	
		else:
			letra,mensaje = input_letra()
			if letra:
				if letra in letras_usadas:
					mensaje = "Ya me has dicho la letra {}!".format(letra)
				elif letra in [no_accents(t[0]) for t in palabra]:
					letras_usadas.append(letra)
					mensaje = "Bien! Descubriste una nueva letra"
					for t in palabra:
						if no_accents(t[0])==letra:
							t[1]=1
					if all([v for k,v in palabra]):
						mensaje = "Enhorabuena, Lo has resuelto!"
				else:
					errors += 1
					letras_usadas.append(letra)
					mensaje = ("Ohhhh... la letra {} no está en la "
								"palabra".format(letra))	

								
if __name__ == "__main__":
	main()
