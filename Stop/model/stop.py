import random
import uuid
import re

class Jugador:
    def __init__(self,nombre: str) -> None:
        self.nombre: str = nombre
        self.puntaje: float = 0
        self.id: str = uuid.uuid1()

class Categoria:
    def __init__(self, categoria: str, lista_palabras: list):
        self.categoria = categoria
        self.lista_palabras = lista_palabras


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

class Verificacion:
    def __init__(self, Letra: str, palabra_utilizada: str, categoria: Categoria):
        self.letra: str = Letra
        self.palabra = palabra_utilizada
        self.categorias_stop = categoria

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
    
    def verificar_categoria(self):
        if self.palabra not in self.categorias_stop.lista_palabras:
            return False
        else:
            return True


class Multijugador:
    def __init__(self):
        self.lista_jugadores = []
    def crear_jugador(self, nombre: str):
        jugador = Jugador(nombre)
        self.lista_jugadores.append(jugador)
        return self.lista_jugadores
    
class Score:
    def __init__(self, verificado: Verificacion):
        self.verificado = verificado
    def asignar_score(self):
        if self.verificado.contiene_solo_letras() and self.verificado.verificar_categoria() and self.verificado.verificar_letra():
            score = 500
            return score
        else:
            score = 0
            return score

class Global:
    def __init__(self, score: Score, jugador: Jugador):
        self.score = score
        self.jugador = jugador
    def sumar_global(self,jugador_id: str):
        if jugador_id == self.jugador.id:
            self.jugador.puntaje += self.score.score_total()

class Administrador:
    def __init__(self):
        self.contraseña = "PepitA4343"
    def agregar_palabra(self,palabra: str, categoria: Categoria):
        if palabra not in categoria.lista_palabras:
            categoria.lista_palabras.append(palabra)
    def eliminar_palabra(self,palabra: str, categoria: Categoria):
        if palabra in categoria.lista_palabras:
            categoria.lista_palabras.remove(palabra)
    def modificar_palabra(self,palabra: str, categoria: Categoria, modificado: str):
        if palabra in categoria.lista_palabras:
            categoria.lista_palabras.remove(palabra)
            categoria.lista_palabras.append(modificado)
    def agregar_categoria(self, nueva_categoria: Categoria, lista_categorias: list[Categoria]):
        if nueva_categoria not in lista_categorias:
            lista_categorias.append(nueva_categoria)

class Stop:
    def __init__(self) -> None:
        self.jugadores: Multijugador =  []
        self.administrador: Administrador = Administrador()
        self.categorias: list[Categoria] = []
        self.configuracion_juego: Configuracion  = None
        self.verificacion: Verificacion = None
        self.scores_jugador: Score = None
        self.global_jugador: Global = None
    def modificar_palabra(self, palabra:str, lista_categorias: list[Categoria], modificado:str):
        for categoria in lista_categorias:
            self.administrador.modificar_palabra(palabra, categoria, modificado)
    def eliminar_palabra(self, palabra:str, lista_categorias: list[Categoria]):
        for categoria in lista_categorias:
            self.administrador.eliminar_palabra(palabra, categoria)
    def agregar_palabra(self, palabra:str, lista_categorias: list[Categoria]):
        for categoria in lista_categorias:
            self.administrador.agregar_palabra(palabra, categoria)
    def letra_juego(self,dificultad: str):
        return self.configuracion_juego.configurar_partida(dificultad)
    def verificacion_palabras(self,palabra: str,letra:str, categoria: Categoria,tiempo:float):
        total = 0
        for categoria in self.categorias:
            self.verificacion = Verificacion(letra,palabra,categoria)
            score = Score(self.verificacion).asignar_score()
            total += score
        return total-(1*tiempo)
    def total_jugador(self,total: float, jugador: Jugador):
        pass

