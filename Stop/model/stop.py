import random
import uuid
import re

class Jugador:
    def __init__(self,nombre: str) -> None:
        self.nombre: str = nombre
        self.puntaje: float = 0
        self.id: str = uuid.uuid1()
    def agregar_puntaje(self):
        self.puntaje += 100

class Configuracion:
    def __init__(self,dificultad: str) -> None:
        self.dificultad:str = dificultad
    def configurar_partida(self):
        facil = ["A","B","C","D","L","M","P","S"]
        medio = ["E","F","G","I","J","N","O","R","T","U"]
        dificil = ["H","K","Q","V","W","X","Y","Z"]
        if self.dificultad.lower() == "facil":
            Letra = random.choice(facil)
            return Letra 
        elif self.dificultad.lower() == "normal":
            Letra = random.choice(medio)
            return Letra 
        elif self.dificultad.lower() == "dificil":
            Letra = random.choice(dificil)
            return Letra 
        else:
            return False  

class Verificacion:
    def __init__(self, Letra: str, palabra_utilizadas: list):
        self.letra: str = Letra
        self.palabras: list = palabra_utilizadas

    def contiene_solo_letras(self):
        for palabra in self.palabras:
            if not re.match(r'^[a-zA-Z]+$', palabra):
                return False
        return True

    def verificar_letra(self):
        for palabra in self.palabras:
            if not palabra.lower().startswith(self.letra.lower()):
                return False
        return True
    
class Multijugador:
    def __init__(self) -> None:
        pass
    
class Score:
    def __init__(self) -> None:
        pass

class Global:
    def __init__(self) -> None:
        pass

class Comprobar:
    def __init__(self) -> None:
        pass

class Eliminar:
    def __init__(self) -> None:
        pass

class Modificar:
    def __init__(self) -> None:
        pass

class Stop:
    def __init__(self) -> None:
        self.jugador: Jugador = None
        self.configuracion: Configuracion = None
    def registrar_jugador(self, nombre):
        self.jugador = Jugador(nombre)
    def configuracion_partida(self, dificultad:str):
        self.configuracion = Configuracion(dificultad)
        return self.configuracion.configurar_partida()
    def agregar_palabra(self, Letra: str,palabra: str):
        palabras = []
        lista_palabras = Verificacion(Letra, palabras)
        if lista_palabras.contiene_solo_letras():
            if lista_palabras.verificar_letra():
                palabras.append(palabra)
                return palabras
            else:
                return False
        else:
            return False