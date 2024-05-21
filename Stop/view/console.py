import tkinter as tk
import model.stop as st
from tkinter import messagebox

class StopGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego Stop")
        self.master.geometry("900x500")
        self.stop = st.Stop()
        
        self.bienvenida()
        
    def bienvenida(self):
        self.config_frame = tk.Frame(self.master)
        self.config_frame.pack()
        
        tk.Label(self.config_frame, text="Bienvenido al juego de stop").pack()
        
        tk.Label(self.config_frame, text="Elige alguna opcion: ").pack()
        
        self.start_button = tk.Button(self.config_frame, text="Iniciar Juego", command=self.ejecucion_juego)
        self.start_button.pack()
        self.admin_button = tk.Button(self.config_frame, text="Administrador", command=self.admin_confi)
        self.admin_button.pack()
        self.exit_button = tk.Button(self.config_frame, text="Iniciar Juego", command=self.cerrar_juego)
        self.exit_button.pack()
        
    def ejecucion_juego(self):
        self.config_frame.pack_forget()
        self.name_frame = tk.Frame(self.master)
        self.name_frame.pack(pady=20)
        tk.Label(self.name_frame, text="Ingrese la cantidad de jugadores").pack()
        self.lbl_cantidad = tk.Entry(self.name_frame)
        self.lbl_cantidad .pack()
        self.continue_button = tk.Button(self.name_frame, text="Siguiente", command=self.cerrar_juego)
        self.continue_button.pack()

    def nombre_jugadores(self):
        self.name_frame.pack_forget()
        self.entrada_frame = tk.Frame(self.master)
        self.entrada_frame.pack(pady=20)
        numero_jugadores = int(self.lbl_cantidad.get())
        for i in range(numero_jugadores):
            tk.Label(self.name_frame, text="Ingrese la cantidad de jugadores").pack()
            self.lbl_cantidad = tk.Entry(self.name_frame)
            self.lbl_cantidad .pack()
    
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
        self.agregar_categoria_button = tk.Button(self.agregar_categoria_frame, text="Agregar categoria", command= lambda: self.agregar_categoria)
        self.agregar_categoria_button.pack()
        self.regresar_button = tk.Button(self.agregar_categoria_frame, text="Regresar", command= lambda: self.retornar_admin(self.agregar_categoria_frame))
        self.regresar_button.pack()

    def ventana_admin(self):
        self.admin_frame.pack_forget()
        self.ventana_admin_frame = tk.Frame(self.master)
        self.ventana_admin_frame.pack(pady=20)
        self.lista_categorias: list[st.Categoria] = []
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

    def stop_game(self):
        pass
    def cerrar_juego(self):
        pass