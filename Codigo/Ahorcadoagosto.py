# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import random, os, time
 
listadepalabras = ["gato", "perro", "naranja", "manzana", "uvas", "computadora", "serpiente"]
letraescogida= []
vidas = 6
 
word = random.choice(listadepalabras)

DIBUJOSAHORCADO = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
     |
     |
    ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''']

for i in word: 
    print("_ ", end="")
print()
 
while True:
    
    time.sleep(1)
    #os.system("clear")
    print()
    letra = input("Escoge una letra: ").lower()

    if letra in letraescogida:
        print("Ya intentaste con esa letra")
        continue

    letraescogida.append(letra)

    if letra in word:
        print("Acertaste!")
    else:
        print("No, esa no está")
        vidas -= 1

    allLetters = True
    print()
    for i in word:
        if i in letraescogida:
            print(i, end=" ")
        else:
            print("_ ", end="")
            allLetters = False
    print()
 
    if allLetters:
        print()
        time.sleep(0.5)
        print(f"Ganaste y te quedaron {vidas} vidas!")
        break
     
    if vidas<=0:
        print()
        time.sleep(0.5)
        print(f"Perdiste! La respuesta es {word}")
        if vidas ==0:
            print(DIBUJOSAHORCADO[6])
        break
    else:
        time.sleep(0.5)
        
        if vidas ==6:
            print(f"Te quedan {vidas} vidas")
            print(DIBUJOSAHORCADO[0])
        elif vidas ==5:
            print(f"Te quedan {vidas} vidas")
            print(DIBUJOSAHORCADO[1])
        elif vidas ==4:
            print(f"Te quedan {vidas} vidas")
            print(DIBUJOSAHORCADO[2])
        elif vidas ==3:
            print(f"Te quedan {vidas} vidas")
            print(DIBUJOSAHORCADO[3])
        elif vidas ==2:
            print(f"Te quedan {vidas} vidas")
            print(DIBUJOSAHORCADO[4])
        elif vidas ==1:
            print(f"Te queda {vidas} vida")
            print(DIBUJOSAHORCADO[5])
        
            
   