import random
import uuid
import re

class Jugador:
    def __init__(self,nombre: str) -> None:
        self.nombre: str = nombre
        self.puntaje: float = 0
        self.id: str = uuid.uuid1()

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
    def __init__(self, Letra: str, palabra_utilizada: str):
        self.letra: str = Letra
        self.palabra = palabra_utilizada

    def contiene_solo_letras(self):
        if not re.match(r'^[a-zA-Z]+$', self.palabra):
            return False
        else:
            return True

    def verificar_letra(self):
        if not self.palabra.lower().startswith(self.letra.lower()):
            return False
        else:
            return True
    
    def verificar_categoria(self,lista_categoria: list):
        if self.palabra not in lista_categoria:
            return False
        else:
            return True


class Multijugador:
    def __init__(self,numero_jugadores: int):
        self.numero_jugadores = numero_jugadores
    def crear_jugador(self,nombre):
        lista_jugadores = []
        jugador = Jugador(nombre)
        lista_jugadores.append(jugador)
        return lista_jugadores
    
class Score:
    def __init__(self, verificado: Verificacion, tiempo: float):
        self.verificado = verificado
        self.tiempo = tiempo
    def asignar_score(self,lista_categoria: list):
        if self.verificado.contiene_solo_letras() and self.verificado.verificar_categoria(lista_categoria) and self.verificado.verificar_letra():
            score = 500
            return score
        else:
            score = 0
            return score
    def score_total(self):
        total = 0
        total += self.asignar_score()  
        return total - 1*self.tiempo

class Global:
    def __init__(self, score: Score, jugador: Jugador):
        self.score = score
        self.jugador = jugador
    def sumar_global(self,jugador_id: str):
        if jugador_id == self.jugador.id:
            self.jugador.puntaje += self.score.score_total()

class Agregar:
    def __init__(self, palabra: str, categoria: str):
        self.palabra = palabra
        self.categoria = categoria
    def agregar_palabra(self, categorias: list, lista_categoria: list):
        if self.categoria in categorias:
            lista_categoria.append(self.palabra)

class Eliminar:
    def __init__(self, palabra: str, categoria: str):
        self.palabra = palabra
        self.categoria = categoria
    def eliminar_palabra(self, categorias: list, lista_categoria: list):
        if self.categoria in categorias:
            lista_categoria.remove(self.palabra)

class Modificar:
    def __init__(self, palabra: str, categoria: str):
        self.palabra = palabra
        self.categoria = categoria
    def modificar_palabra(self, categorias: list, lista_categoria: list):
        if self.categoria in categorias:
            lista_categoria.remove(self.palabra)
            modificado = input("Agrege la palabra modificada: ")
            lista_categoria.append(modificado)

class Categoria:
    def __init__(self, categoria: str, lista_categoria: list):
        self.categoria = categoria
        self.lista_categoria = lista_categoria
    def agregar_categoria_nueva(self,categorias: list):
        if self.categoria not in categorias:
            categorias.append(self.categoria)
