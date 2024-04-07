from Stop.model.stop import Stop
import sys

class UIConsola:
        def __init__(self):
            self.stop: Stop = Stop()

        def ingresar_usuario(self):
            print("Hola, bienvenid@ al juego del Stop o Apuntado")
            nombre: str = input("Ingresa tu nombre para empezar: ")
            jugador = self.stop.registrar_jugador(nombre)
            return jugador
        
        def ejecutar_juego(self):
            self.ingresar_usuario()
            partidas: int = int(input("¿Cuantas partidas quieres jugar?: "))
            dificultad: str = input("Elija la dificultad en la que quiere jugar(facil,normal,dificil): ")
            while partidas > 0:
                letra = self.obtener_configuracion(dificultad)
                palabras = self.agregar_palabra(letra)
                partidas -= 1
                puntaje = self.calcular_puntaje(palabras)
                print("Su puntaje es: ", puntaje)
                self.continuacion()
            self.salir()

        def obtener_configuracion(self,dificultad):
            letra = self.stop.configuracion_partida(dificultad)
            while letra == False:
                dificultad: str = input("Elija la dificultad en la que quiere jugar(facil,normal,dificil): ")
                letra = self.stop.configuracion_partida(dificultad)
            print("Usted va a jugar usando la letra: ", letra)
            return letra
        
        def agregar_palabra(self, letra):
            palabras = []
            palabras_a_pedir = ["Nombre", "Apellido", "Animal", "Ciudad", "Color", "Cosa","Fruta/Verdura"]
            for palabra_a_pedir in palabras_a_pedir:
                while True:
                    palabra = input(f"Ingrese un/a {palabra_a_pedir}: ")
                    if palabra.lower().startswith(letra.lower()):
                        palabras.append(palabra)
                        break
                    else:
                        print(f"La palabra debe empezar con la letra '{letra}'. Inténtelo de nuevo.")
            return palabras
        
        def calcular_puntaje(self, lista_palabras: list):
            return 100*len(lista_palabras)
        def continuacion(self):
            continuar:str = input("¿Desea continuar o quiere salir ya? Si/No: ")
            if continuar.lower() == "si":
                return True
            elif continuar.lower() == "no":
                self.salir()
            else:
                print("Opción no valida")
        def salir(self):
            print("Muchas gracias por jugar")
            sys.exit()