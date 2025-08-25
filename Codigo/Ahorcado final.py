#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 23:18:18 2025

@author: jorgecano
"""

import sys

def jugar_ahorcado():
    
   import random, time   #Instalé random para escoger la palabra aleatoriamente y la libreria time para controlar un poco el flujo
                         #al momento de presentar el juego
    
   listadepalabras = ["gato", "perro", "naranja", "manzana", "uvas", "computadora", "serpiente"]
   letraescogida= []     #Inicializo una lista vacía en donde se almacenaran las letras correctas proporcionadas por el usuario
   vidas = 6             #Seteo fijo de las vidas en 6 porque es la cantidad de graficos que tengo
    
   word = random.choice(listadepalabras)      #Esta linea escoge aleatoriamente una de las palabras dentro de la lista de palabras

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
       ===''']                     #Creación de una lista con el avance progresivo de los graficos
       

   for i in word: 
       print("_ ", end="")        #Imprimo los espacios disponibles según la palabra escogida
   print()
    
   while True:
       
       time.sleep(0.5)
       #os.system("clear")
       letra = input("\nEscoge una letra: ").lower()            # ya dentro de la estructura repetitiva primero solicito al usuario que ingrese una letra, ya basandose en los espacios disponibles

       if letra in letraescogida:                                  # primero verificamos si la letra que ingresa ha sido ingresada antes, lo cual no le descontará vidas, en el caso que se repita, se vuelve a pedir una letra.
           print("\nYa intentaste con esa letra")
           continue                                           #Continue hace que vuelva al inicio del While

       letraescogida.append(letra)                             #Al no cumplirse la condiciíon de letra repetida, se almacena la letra en la lista vacía

       if letra in word:                                       #Verficiar si la letra ingresada está en la palabra escogida por el programa, si no está, se resta una vida
           print("\nAcertaste!")
       else:
           print("\nNo, esa letra es incorrecta")
           vidas -= 1

       pcompleta = True                                       #Incialicé una variable booleana Que sirva de condición para recorrer la palabra escogida aleatoriamente y compararla con las letras que va proporcionando el usuario
       print()                                                #Si coincide la letra de la cadena de caracteres con la de la lista de letras proporcionadas por el usuario, se muestra la letra en vez del espacio
       for i in word:                                         #Si no coincide, se muestra el espacio y se asigna pcompleta=False, para que siga recorriendo los espacios restantes del str.
           if i in letraescogida:
               print(i, end="")
           else:
               print("_ ", end="")
               pcompleta = False
       print()
    
       if pcompleta:                                            #Al terminar de recorrer la palabra se confirma si se completó correctamente la palabra
           time.sleep(0.5)                                      #Si la variable pcompleta quedo en False, no entra en esta sección y continua a la condición de vidas
           print(f"\nGanaste y te quedaron {vidas} vidas!")
           break                                                #El break termina el juego
        
       if vidas<=0:                                             #Si el usuario se queda sin vidas se muestra el dibujo del ahorcado completo y se termina el juego
           time.sleep(0.5)
           print(f"\nPerdiste! La respuesta es {word}")
           print(DIBUJOSAHORCADO[6])
           break
       else:
           time.sleep(0.5)                                     #Si el usuario todavía tiene vidas disponibles, se muestra un dibujo acorde a la cantidad de vidas que le sobra
           
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


def menu():
    jugada_previa = False  # para que 'Volver a jugar' tenga sentido

    while True:
        print("===== MENÚ AHORCADO =====")
        print("1) Jugar")
        print("2) Volver a jugar")
        print("3) Salir")
        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "1":
            jugar_ahorcado()
            jugada_previa = True

        elif opcion == "2":
            if not jugada_previa:
                print("Aún no has jugado. Iniciando primera partida...\n")
            jugar_ahorcado()
            jugada_previa = True

        elif opcion == "3":
            print("¡Gracias por jugar! 👋")
            sys.exit(0)

        else:
            print("Opción inválida. Intenta de nuevo.\n")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nSalida por teclado. ¡Hasta luego!")
