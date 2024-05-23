import tkinter as tk
import model.stop as st
from tkinter import messagebox
import time as tm
import pickle

class StopGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego Stop")
        self.master.geometry("900x500")
        self.stop = st.Stop()
        self.archivo = st.DatosStop()
        self.index = 0
        self.numero_partida = 1
        self.lista_registro: list[st.Historial]= []
        self.lista_categorias: list[st.Categoria] = []
        self.bienvenida()

    def cargar_Archivos_registro(self):
        with open("datos_guardados_historial.pickle", "rb") as archivo:
            self.lista_registro = pickle.load(archivo)
    def cargar_Archivos_categoria(self):
        with open("datos_guardados_categoria.pickle", "rb") as archivo:
            self.lista_categorias = pickle.load(archivo)

    def bienvenida(self):
        self.config_frame = tk.Frame(self.master)
        self.config_frame.pack()
        # self.cargar_Archivos_categoria()
        # self.cargar_Archivos_registro()
        tk.Label(self.config_frame, text="Bienvenido al juego de stop").pack()
        
        tk.Label(self.config_frame, text="Elige alguna opcion: ").pack()
        
        self.start_button = tk.Button(self.config_frame, text="Iniciar Juego", command=self.ejecucion_juego)
        self.start_button.pack()
        self.admin_button = tk.Button(self.config_frame, text="Administrador", command=self.admin_confi)
        self.admin_button.pack()
        self.historial_button = tk.Button(self.config_frame, text="Historial de partidas", command=self.historial)
        self.historial_button.pack()
        self.exit_button = tk.Button(self.config_frame, text="Iniciar Juego", command=self.master.quit)
        self.exit_button.pack()

        
    def ejecucion_juego(self):
        self.config_frame.pack_forget()
        self.name_frame = tk.Frame(self.master)
        self.name_frame.pack(pady=20)
        tk.Label(self.name_frame, text="Ingrese la cantidad de jugadores").pack()
        self.lbl_cantidad = tk.Entry(self.name_frame)
        self.lbl_cantidad.pack()
        self.continue_button = tk.Button(self.name_frame, text="Siguiente", command=lambda: self.nombre_jugadores)
        self.continue_button.pack()

    def nombre_jugadores(self):
        self.name_frame.pack_forget()
        self.entrada_frame = tk.Frame(self.master)
        self.entrada_frame.pack(pady=20)
        self.lista_nombres = []
        try:
            numero_jugadores = int(self.lbl_cantidad.get())
            for i in range(numero_jugadores):
                tk.Label(self.entrada_frame, text=f"Ingrese el nombre del jugador{i+1}").pack()
                self.nombre_jugador = tk.Entry(self.entrada_frame)
                self.nombre_jugador.pack()
                self.lista_nombres.append(self.nombre_jugador.get())
        except ValueError:
            messagebox.showerror("Error","Ingrese un numero entero porfavor")
        self.continue_button = tk.Button(self.entrada_frame, text="Siguiente", command= lambda: self.configuracion_partida)
        self.continue_button.pack()

    def dificultad(self):
        dificultad = self.lbl_dificultad.get()
        try:
            self.partidas = int(self.lbl_partidas.get())
        except ValueError:
            messagebox.showerror("Error","Ingrese un numero entero porfavor")
        self.letra = st.Stop.configuracion_partida(dificultad)
        self.lista_jugadores = st.Stop.jugadores(self.lista_nombres)
        self.stop_game()
    
    def configuracion_partida(self):
        self.entrada_frame.pack_forget()
        self.configuracion_frame = tk.Frame(self.master)
        self.configuracion_frame.pack(pady=20)
        tk.Label(self.configuracion_frame, text="Ingrese la dificultad del juego (facil,normal,dificil)").pack()
        self.lbl_dificultad= tk.Entry(self.configuracion_frame)
        self.lbl_dificultad.pack()
        tk.Label(self.configuracion_frame, text="Ingrese el numero de partidas que desean jugar").pack()
        self.lbl_partidas= tk.Entry(self.configuracion_frame)
        self.lbl_partidas.pack()
        self.continue_button = tk.Button(self.entrada_frame, text="Siguiente", command= lambda: self.dificultad)
        self.continue_button.pack()
        
    def stop_game(self):
        self.configuracion_frame.pack_forget()
        self.inicio = tm.time()
        self.stop_game_frame = tk.Frame(self.master)
        self.stop_game_frame.pack(pady=20)
        self.listado_palabra = []
        tk.Label(self.stop_game_frame, text=f"Turno del jugador {self.lista_jugadores[self.index].nombre}").pack()
        for categoria in self.lista_categorias:
            tk.Label(self.stop_game_frame, text=f"{categoria.categoria}").pack()
            self.lbl_palabra= tk.Entry(self.stop_game_frame)
            self.lbl_palabra.pack()
            self.listado_palabra.append(self.lbl_palabra.get())
        self.continue_button = tk.Button(self.stop_game_frame, text="Siguiente", command= lambda: self.verificar_palabras)
        self.continue_button.pack()
    
    def verificar_palabras(self):
        self.final = tm.time()
        total_jugador = 0
        for palabra in self.listado_palabra:
            for categoria in self.lista_categorias:
                puntaje = st.Stop.verificacion_palabras(palabra,self.letra,categoria,self.final)
            total_jugador += puntaje
        self.lista_jugadores[self.index].puntaje_parcial = total_jugador
        self.lista_jugadores[self.index].asignar_puntaje_total()
        self.continuar_stop()

    def continuar_stop(self):
        self.stop_game_frame.pack_forget()
        self.index += 1
        if self.index < len(self.lista_jugadores):
            self.stop_game()
        else:
            self.resultado_juego()

    def resultado_juego(self):
        self.resultado_frame = tk.Frame(self.master)
        self.resultado_frame.pack(pady=20)
        self.ganador: st.Jugador = None
        for jugador in self.lista_jugadores:
            jugador.reiniciar_puntaje_parcial()
            if jugador.puntaje_total > self.ganador.puntaje_total:
                self.ganador = jugador
            else:
                continue
        tk.Label(self.resultado_frame, text=f"El ganador de la partida es {self.ganador.nombre}").pack()
        self.siguiente_partida_button = tk.Button(self.resultado_frame, text="Siguiente", command= self.continuacion_juego)
        self.siguiente_partida_button.pack()

    def continuacion_juego(self):
        self.resultado_frame.pack_forget()
        self.numero_partida += 1
        if self.partidas < self.numero_partida:
            self.stop_game()
        else:
            self.cerrar_juego()
    
    def verificar_contraseña(self):
        contraseña = self.contraseña.get()
        self.admin = st.Administrador()
        if self.admin.contraseña == contraseña:
            self.ventana_admin()
        else:
            messagebox.showerror("Error","Contraseña incorrecta, intente nuevamente")
        
    def retornar_principal(self, ventana):
        ventana.pack_forget()
        self.bienvenida() 
    def retornar_admin(self,ventana):
        ventana.pack_forget()
        self.admin_confi()
    def admin_confi(self):
        self.config_frame.pack_forget()
        self.admin_frame = tk.Frame(self.master)
        self.admin_frame.pack(pady=20)
        tk.Label(self.admin_frame, text="Ingrese la contraseña para el acceso:").pack()
        self.contraseña = tk.Entry(self.admin_frame)
        self.contraseña.pack()
        self.confirmar_button = tk.Button(self.admin_frame, text="Confirmar", command=self.verificar_contraseña)
        self.confirmar_button.pack()
        self.regresar_button = tk.Button(self.admin_frame, text="Regresar", command= lambda: self.retornar_principal(self.admin_frame))
        self.regresar_button.pack()

    def modificardor(self):
        modificar = self.modificar.get()
        corregido = self.correccion.get()
        self.stop.modificar_palabra(modificar,self.lista_categorias,corregido)
        messagebox.showinfo("Exito","Su palabra se ha corregido con exito")
    def eliminador(self):
        eliminar = self.eliminar.get()
        self.stop.eliminar_palabra(eliminar,self.lista_categorias)
        messagebox.showinfo("Exito","Su palabra se ha eliminado con exito")
    def agregar(self):
        agregar = self.agregar_palabra.get()
        self.stop.agregar_palabra(agregar,self.lista_categorias)
        messagebox.showinfo("Exito","Su palabra se ha agregado con exito")
    def agregrar_categoria(self):
        nombre = self.nombre_categoria.get()
        lista = self.lista_palabras.get()
        nueva_categoria = st.Categoria(nombre,lista)
        self.admin.agregar_categoria(nueva_categoria, self.lista_categorias)
        messagebox.showinfo("Exito","Su categoria se ha agregado con exito")
        self.archivo.guardar_lista_categorias(self.lista_categorias)

    def ventana_modificar(self):
        self.ventana_admin_frame.pack_forget()
        self.modificar_frame = tk.Frame(self.master)
        self.modificar_frame.pack(pady=20)
        tk.Label(self.modificar_frame, text="Ingrese la palabra a modificar:").pack()
        self.modificar = tk.Entry(self.modificar_frame)
        self.modificar.pack()
        tk.Label(self.modificar_frame, text="Ingrese la palabra corregida:").pack()
        self.correccion = tk.Entry(self.modificar_frame)
        self.correccion.pack()
        self.modificar_button = tk.Button(self.modificar_frame, text="Modificar palabra", command= lambda: self.modificardor)
        self.modificar_button.pack()
        self.regresar_button = tk.Button(self.modificar_frame, text="Regresar", command= lambda: self.retornar_admin(self.modificar_frame))
        self.regresar_button.pack()

    def ventana_eliminar(self):
        self.ventana_admin_frame.pack_forget()
        self.eliminar_frame = tk.Frame(self.master)
        self.eliminar_frame.pack(pady=20)
        tk.Label(self.eliminar_frame, text="Ingrese la palabra a eliminar:").pack()
        self.eliminar = tk.Entry(self.eliminar_frame)
        self.eliminar.pack()
        self.eliminar_button = tk.Button(self.eliminar_frame, text="Eliminar palabra", command= lambda: self.modificardor)
        self.eliminar_button.pack()
        self.regresar_button = tk.Button(self.eliminar_frame, text="Regresar", command= lambda: self.retornar_admin(self.eliminar_frame))
        self.regresar_button.pack()
    def ventana_agregar_palabra(self):
        self.ventana_admin_frame.pack_forget()
        self.agregar_frame = tk.Frame(self.master)
        self.agregar_frame.pack(pady=20)
        tk.Label(self.agregar_frame, text="Ingrese la palabra a eliminar:").pack()
        self.agregar_palabra = tk.Entry(self.agregar_frame)
        self.agregar_palabra.pack()
        self.agregar_button = tk.Button(self.agregar_frame, text="Agregar palabra", command= lambda: self.modificardor)
        self.agregar_button.pack()
        self.regresar_button = tk.Button(self.agregar_frame, text="Regresar", command= lambda: self.retornar_admin(self.agregar_frame))
        self.regresar_button.pack()
    def ventana_agregar_categoria(self):
        self.ventana_admin_frame.pack_forget()
        self.agregar_categoria_frame = tk.Frame(self.master)
        self.agregar_categoria_frame.pack(pady=20)
        tk.Label(self.agregar_categoria_frame, text="Ingrese el nombre de la cateogira").pack()
        self.nombre_categoria = tk.Entry(self.agregar_categoria_frame)
        self.nombre_categoria()
        tk.Label(self.agregar_categoria_frame, text="Ingrese la lista de palabras para la categoria:").pack()
        self.lista_palabras = tk.Entry(self.agregar_categoria_frame)
        self.lista_palabras.pack()
        self.agregar_categoria_button = tk.Button(self.agregar_categoria_frame, text="Agregar categoria", command= lambda: self.agregrar_categoria)
        self.agregar_categoria_button.pack()
        self.regresar_button = tk.Button(self.agregar_categoria_frame, text="Regresar", command= lambda: self.retornar_admin(self.agregar_categoria_frame))
        self.regresar_button.pack()

    def ventana_admin(self):
        self.admin_frame.pack_forget()
        self.ventana_admin_frame = tk.Frame(self.master)
        self.ventana_admin_frame.pack(pady=20)
        self.confirmar_button = tk.Button(self.ventana_admin_frame, text="Modificar palabra", command=self.ventana_modificar)
        self.confirmar_button.pack()
        self.confirmar_button = tk.Button(self.ventana_admin_frame, text="Eliminar Palabra", command=self.ventana_eliminar)
        self.confirmar_button.pack()
        self.confirmar_button = tk.Button(self.ventana_admin_frame, text="Agregar palabra", command=self.ventana_agregar_palabra)
        self.confirmar_button.pack()
        self.confirmar_button = tk.Button(self.ventana_admin_frame, text="Agregar categoria", command=self.ventana_agregar_categoria)
        self.confirmar_button.pack()
        self.regresar_button = tk.Button(self.admin_frame, text="Regresar", command= lambda: self.retornar_principal(self.ventana_admin_frame))
        self.regresar_button.pack()


    def historial(self):
        self.config_frame.pack_forget()
        self.historial_frame = tk.Frame(self.master)
        self.historial_frame.pack(pady=20)
        for registro in self.lista_registro:
            tk.Label(self.historial_frame, text=f"El ganador del juego fue {registro.ganador.nombre}, con un puntajde de {registro.ganador.putaje_total}, con un total de {registro.numero_partidas} partidas jugadas").pack()
        self.regresar_button = tk.Button(self.historial_frame, text="Regresar", command= lambda: self.retornar_principal(self.historial_frame))
        self.regresar_button.pack()

    def guardar_historial_juego(self,ganador_juego: st.Jugador):
        registro = st.Stop.asignar_registro_historial(ganador_juego, self.numero_partida)
        self.lista_registro.append(registro)
        self.archivo.guardar_lista_historial(self.lista_registro)


    def cerrar_juego(self):
        self.final_frame = tk.Frame(self.master)
        self.final_frame.pack(pady=20)
        self.ganador_juego: st.Jugador = None
        for jugador in self.lista_jugadores:
            jugador.reiniciar_puntaje_parcial()
            if jugador.puntaje_total > self.ganador_juego.puntaje_total:
                self.ganador_juego = jugador
            else:
                continue
        tk.Label(self.resultado_frame, text=f"El ganador del juego es {self.resultado_frame}").pack()
        self.guardar_historial_juego(self.ganador_juego)
        self.regresar_button = tk.Button(self.final_frame, text="Volver al inicio", command= lambda: self.retornar_principal(self.final_frame))
        self.regresar_button.pack()
        self.regresar_button = tk.Button(self.final_frame, text="Cerrar", command= self.master.quit)
        self.regresar_button.pack()