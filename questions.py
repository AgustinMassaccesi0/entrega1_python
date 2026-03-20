import random

words = {
    "facil": ["bucle","lista","entero","cadena"],
    "dificil": ["python", "programa", "variable", "funcion"]
}

print('Categorias disponibles:')
for categoria in words:
    print(categoria)
    
print()
categoria_elegida = input('Elegi una categoria:').lower()

while categoria_elegida not in words:
    print("Categoría inválida")
    categoria_elegida = input('Elegi una categoria:').lower()


word = random.choice(words[categoria_elegida])
guessed = []
attempts = 6

puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()


while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        puntaje += 6
        print("¡Ganaste!")
        print(f'Puntaje final: {puntaje}')
        break


    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print()
        print('Entrada no valida')
        print()
        continue
    elif letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")
        puntaje -= 1
        
    print()

else:
        puntaje = 0
        print(f"¡Perdiste! La palabra era: {word}")
        print(f'Puntaje final: {puntaje}')
        
