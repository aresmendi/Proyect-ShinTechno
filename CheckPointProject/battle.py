import random
class Personaje:
    def __init__(self, nombre, salud, ataque, defensa, usos_magia):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        self.usos_magia = usos_magia
        self.salud_maxima = salud

    def atacar(self, objetivo):
        daño = max(0, self.ataque - objetivo.defensa)
        objetivo.salud -= daño
        print(f"{self.nombre} attacks {objetivo.nombre} and makes {daño} dmg!")

    def defender(self):
        print(f"{self.nombre} defense himself!")

    def curar(self):
        curación = random.randint(3, 10)  # Genera un valor aleatorio entre 3 y 10
        self.salud = min(self.salud_maxima, self.salud + curación)
        print(f"{self.nombre} it cures {curación} HP. ACTUALLY: {self.salud}.")

    def usar_magia(self, objetivo):
        if self.usos_magia > 0:
            daño_magico = self.ataque * 10
            objetivo.salud -= daño_magico
            self.usos_magia -= 1
            print(f"{self.nombre} use magic against {objetivo.nombre} and makes {daño_magico} dmg! Magic uses: {self.usos_magia}.")
        else:
            print(f"{self.nombre} don't have any more magic uses.")

    def esta_vivo(self):
        return self.salud > 0

def pelea(jugador, enemigos):
    while jugador.esta_vivo() and any(enemigo.esta_vivo() for enemigo in enemigos):
        print(f"\nTurn {jugador.nombre}:")
        print(f"Health: {jugador.salud}, Magic Uses: {jugador.usos_magia}")
        accion = input("Choose: 1. Attack, 2. Defend, 3. Health, 4. Use magic: ")

        if accion == "1":
            objetivo = seleccionar_enemigo(enemigos)
            if objetivo is not None:
                jugador.atacar(objetivo)
            else:
                print("Select a valid enemy.")
        elif accion == "2":
            jugador.defender()
        elif accion == "3":
            jugador.curar()
        elif accion == "4":
            objetivo = seleccionar_enemigo(enemigos)
            if objetivo is not None:
                jugador.usar_magia(objetivo)
            else:
                print("Select a valid enemy.")
        else:
            print("Try again.")

        for enemigo in enemigos:
            if enemigo.esta_vivo():
                print(f"\nTurn {enemigo.nombre}:")
                print(f"Health {enemigo.nombre}: {enemigo.salud}")
                
                # Los enemigos se defienden si su salud es menor al 25% de su salud máxima
                if enemigo.salud < 0.25 * enemigo.salud_maxima:
                    enemigo.defender()
                # Los enemigos se curan si su salud es menor al 50% de su salud máxima
                elif enemigo.salud < 0.5 * enemigo.salud_maxima:
                    enemigo.curar()
                else:
                    enemigo.atacar(jugador)
                    
                if not jugador.esta_vivo():
                    break

    if jugador.esta_vivo():
        print("¡You win the fight!")
    else:
        print("Try again, ninja.")


class Personaje:
    def __init__(self, nombre, salud, ataque, defensa, usos_magia):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        self.usos_magia = usos_magia
        self.salud_maxima = salud

    def atacar(self, objetivo):
        daño = max(0, self.ataque - objetivo.defensa)
        # Aplicamos la defensa que reduce el 30% del daño recibido
        daño -= objetivo.defensa * 0.3
        objetivo.salud -= daño
        print(f"{self.nombre} attacks {objetivo.nombre} and makes {daño} dmg!")

    def defender(self):
        print(f"{self.nombre} defend himself. Reduce 50% of the damage next turn.")

    def curar(self):
        curación = random.randint(3, 10)  # Genera un valor aleatorio entre 3 y 10
        self.salud = min(self.salud_maxima, self.salud + curación)
        print(f"{self.nombre} it cures {curación} HP. ACTUALLY: {self.salud}.")

    def usar_magia(self, objetivo):
        if self.usos_magia > 0:
            daño_magico = self.ataque * 10
            objetivo.salud -= daño_magico
            self.usos_magia -= 1
            print(f"{self.nombre} use magic against {objetivo.nombre} and makes {daño_magico} dmg. Magic Uses: {self.usos_magia}.")
        else:
            print(f"{self.nombre} don't have any more magic uses.")

    def esta_vivo(self):
        return self.salud > 0

def seleccionar_enemigo(enemigos):
    print("Select the enemy:")
    for i, enemigo in enumerate(enemigos, 1):
        print(f"{i}. {enemigo.nombre}")
    seleccion = input("Enemy number: ")

    try:
        seleccion = int(seleccion)
        if seleccion < 1 or seleccion > len(enemigos):
            print("Invalid selection. Try again")
            return seleccionar_enemigo(enemigos)  # Recursión en caso de selección inválida
        else:
            return enemigos[seleccion - 1]
    except ValueError:
        print("Please, try again.")
        return seleccionar_enemigo(enemigos)  # Recursión en caso de entrada no numérica

