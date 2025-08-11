# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import random, time
 
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
    
    time.sleep(0.5)
    #os.system("clear")
    letra = input("\nEscoge una letra: ").lower()

    if letra in letraescogida:
        print("\nYa intentaste con esa letra")
        continue

    letraescogida.append(letra)

    if letra in word:
        print("\nAcertaste!")
    else:
        print("\nNo, esa letra es incorrecta")
        vidas -= 1

    pcompleta = True
    print()
    for i in word:
        if i in letraescogida:
            print(i, end="")
        else:
            print("_ ", end="")
            pcompleta = False
    print()
 
    if pcompleta:
        time.sleep(0.5)
        print(f"\nGanaste y te quedaron {vidas} vidas!")
        break
     
    if vidas<=0:
        time.sleep(0.5)
        print(f"\nPerdiste! La respuesta es {word}")
        print(DIBUJOSAHORCADO[6])
        break
    else:
        time.sleep(0.5)
        
        if vidas ==6:
            print(f"\nTe quedan {vidas} vidas")
            print(DIBUJOSAHORCADO[0])
        elif vidas ==5:
            print(f"\nTe quedan {vidas} vidas")
            print(DIBUJOSAHORCADO[1])
        elif vidas ==4:
            print(f"\nTe quedan {vidas} vidas")
            print(DIBUJOSAHORCADO[2])
        elif vidas ==3:
            print(f"\nTe quedan {vidas} vidas")
            print(DIBUJOSAHORCADO[3])
        elif vidas ==2:
            print(f"\nTe quedan {vidas} vidas")
            print(DIBUJOSAHORCADO[4])
        elif vidas ==1:
            print(f"\nTe queda {vidas} vida")
            print(DIBUJOSAHORCADO[5])
        
            
   