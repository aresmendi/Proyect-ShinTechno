from battle import Personaje, pelea
import time

def introducir_juego():
    print("###################################################################")
    print("##                                                               ##")
    print("##                                                               ##")
    print("##                                                               ##")
    print("##                                                               ##")
    print("##                        The Path of the                        ##")
    print("##                             NINJA                             ##")
    print("##                                                               ##")
    print("##                                                               ##")
    print("##                                                               ##")
    print("##                                           ARESMENDI DEL TERRY ##")
    print("###################################################################")
    print()
    input("         To doubt it's to lose. To press enter is get in       ")
    print() 
    print()

def seleccionar_casa(nombre_jugador):
    casas = ["Dragon's House", "Monkey's House"]
    for i, casa in enumerate(casas, 1):
        print(f"{i}. {casa}")
    seleccion = int(input("Introduce the Ninja House Number: "))

    if seleccion < 1 or seleccion > len(casas):
        print("Check Again.That's a non valid selection")
        return seleccionar_casa(nombre_jugador)  # Recursión en caso de selección inválida
    else:
        casa_seleccionada = casas[seleccion - 1]
        print(f"That's the history of '{nombre_jugador} from {casa_seleccionada}'.")
        return casa_seleccionada

def describir_casa(casa_seleccionada):
    if casa_seleccionada == "Dragon's House":
        print("Your story begins in the north of ShinTechno, in a mountainous and complex land where wild boar meat is common, but cereal is scarce.")
    elif casa_seleccionada == "Monkey's House":
        print("You come from the fertil lands of the East, in touch with the Wet Sea, wich is fullfillet with the rivers from the north mountains.")
def crear_personaje(nombre_jugador, casa_seleccionada):
    stats_casas = {"Dragon's House": {"salud": 120, "ataque": 15, "defensa": 10, "usos_magia": 2},
                   "Monkey's House": {"salud": 80, "ataque": 25, "defensa": 5, "usos_magia": 3}}
    
    stats_jugador = stats_casas[casa_seleccionada]
    jugador = Personaje(nombre_jugador, stats_jugador["salud"], stats_jugador["ataque"], stats_jugador["defensa"], stats_jugador["usos_magia"])
    return jugador

def preparar_pelea(enemigos, mensaje):
    respuesta = input(mensaje).lower()
    if respuesta == "yes":
        for enemigo in enemigos:
            enemigo.salud -= 20  # Reducir la salud de los enemigos si se elige preparar la pelea
            print(f"{enemigo.nombre} starts with {enemigo.salud} health.")
    return enemigos
# Escenas para la Casa del Dragón
def escenas_del_dragon(jugador):
    print("Wardrums are playing in the mountains, your people are going to conquer the Eastern lands!")
    time.sleep(1.5)
    print(f"You have been selected because of your health ({jugador.salud}) and your command skills to lead the first line attack.")

    while True:
        print("Will you accept, or will you leave the war plans to another and stay eating boars?")
        respuesta = input("Type 'yes' to accept or 'no' to refuse: ").lower()
        if respuesta == "yes":
            print("You have accepted the challenge of war! Together with 3 other adventurers, you set off.")
            time.sleep(1.5)
            print("But before that, the Shogun's sister approaches and places her lips on yours.")
            
            while True:
                beso = input("Will you allow such audacity? (yes/no): ").lower()
                if beso == "yes":
                    jugador.usos_magia += 1  # Incrementa el valor de usos_magia en 1
                    print(f"The Shogun looks puzzled at his sister, but then looks at you with a haughty expression, wishes you a good trip, and gives you an extra fire grenade ({jugador.usos_magia}).")
                    break  # Salir del bucle del beso después de una respuesta válida
                elif beso == "no":
                    print("Shogun's don't forget. It's never a good thing to reject a present from the family...")
                    break  # Salir del bucle del beso después de una respuesta válida
                else:
                    print("Invalid response. Please type 'yes' or 'no'.")
            break  # Salir del bucle principal después de procesar la decisión del jugador
        elif respuesta == "no":
            print("You chose not to go to war. You stay in the mountains, living a peaceful life.")
            return False
        else:
            print("Invalid response. Please type 'yes' or 'no'.")
        
        # Añadir opción para observar el terreno
    print("\nYou're going to the east, when you feel the silence around you.")
    time.sleep(1.5)
    observar_terreno = input("Do you want to stop and observe the terrain? (yes/no): ").lower()
    if observar_terreno == "yes":
        print("You stop and observe the terrain. Quicly you see an arrow flying throught the wind.\n") 
        print("You advise your companions, and they manage to doge and go ahead against the enemy.\n")
        print("They fall, but arrive to weaken the enemies before dying.")
        time.sleep(1.5)
        enemigo1 = Personaje("Monkey Ninja 1", 50, 15, 5, 0)
        enemigo2 = Personaje("Monkey Ninja 2", 40, 18, 6, 0)
    else:
        print("Your mates fall down; It's an ambush!")
        enemigo1 = Personaje("Monkey Ninja 1", 60, 15, 5, 0)
        enemigo2 = Personaje("Monkey Ninja 2", 50, 18, 6, 0)
    enemigos = [enemigo1, enemigo2]
    pelea(jugador, enemigos)
    if not jugador.esta_vivo():
        print("Fin del juego.")
        return False

    print("\nAfter the fight, you walk until you see the Shogun of the East")
    jefe = Personaje("Shougun Monkey's House", 90, 15, 10, 0)
    enemigos = [jefe]

    enemigos = preparar_pelea(enemigos, "Do you want to set a trap for the rival Shogun? (yes/no): ")
    pelea(jugador, enemigos)
    if not jugador.esta_vivo():
        print("Fin del juego.")
        return False

    return True  # Retorna True para indicar que la escena se completó

#Escena de la Casa del Mono
def escenas_del_mono(jugador): 
    print("You're peacefully training at your village, when your master call you to make an announcement; You're in war!")
    time.sleep (1.5)
    print("The troups from the north are starting to get in your territory. Would you participate in the defense?")
    while True:
      respuesta = input("Type 'yes' to accept or 'no' to refuse: ").lower()
      if respuesta == "yes":
        print("You has been all your life ready for this. You take your equipment, and go to the bridge to defense your land")
        time.sleep(1.5)
        print("But while you're going, you listen you're mother calling you")

        while True:
            madre= input("Would you stop and go to her? (yes/no)").lower()
            if madre == "yes":
                jugador.salud += 10  # Incrementa el valor de salud en 10
                print(f"Your mother give you the biggest hug of the world. You feel stronger than ever ({jugador.salud}).")
                break
            elif madre == "no":
                print("You go ahead without say goodbye,unknowing if you will see her never again and feeling the sadness at your chest")
                break
            else:
                print("Invalid response. Please type 'yes' or 'no'.")
        break
      elif respuesta == "no":
          print("You decide to runaway and forget all about your duty")
          return False
      else:
          print("Invalid response. Please type 'yes' or 'no'.")

    print("\n You're going to the bridge which connects north and east.")
    print("You see the enemy, just a few kilometers from your position")
    enemigo1 = Personaje("Dragon's Ninja 1", 100, 10, 5, 0)
    enemigo2 = Personaje("Dragon's Ninja 2", 80, 12, 6, 0)
    enemigos = [enemigo1, enemigo2]
    
    enemigos = preparar_pelea(enemigos, "Do you want to set a trap in the bridge? (yes/no): ")
    pelea(jugador, enemigos)
    if not jugador.esta_vivo():
        print("Fin del juego.")
        return False

    print("\nAfter the battle, there is nobody around you, enemy or ally.")
    decisión = input("Do you want to stop and observe the terrain? (yes/no): ").lower()

    if decisión == "yes":
       print("You decide to observe the terrain carefully, but a shadow above you attacks, leaving you injured.")
       jugador.salud -= 10  # El jugador comienza la batalla con -10 de salud
    else:
       print("You decide to move quickly, and just behind you a huge shadows rise.")

    jefe = Personaje("Shougun Dragon's House", 90, 15, 10, 0)
    enemigos = [jefe]
    pelea(jugador, enemigos)
    if not jugador.esta_vivo():
       print("Game Over.")
    return False
    

                 

        



def main():
    introducir_juego()
    nombre_jugador = input("Name your ninja: ")
    casa_seleccionada = seleccionar_casa(nombre_jugador)
    describir_casa(casa_seleccionada)
    
    jugador = crear_personaje(nombre_jugador, casa_seleccionada)
    
    if casa_seleccionada == "Dragon's House":
        if escenas_del_dragon(jugador):
            print("You have completed your mission, great ninja of the Dragon! The East it's now yours.")
    elif casa_seleccionada == "Monkey's House":
        if escenas_del_mono(jugador):
            print("You have completed your mission, great ninja of the Monkey!")

if __name__ == "__main__":
    main()
