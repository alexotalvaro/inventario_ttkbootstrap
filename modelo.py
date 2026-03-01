from tkinter import messagebox

import mysql.connector


class InventarioModelo:
    def __init__(self):
        self.conexion= None
        self.conectar()


    def conectar(self):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="tienda"
            )
            self.conexion = conexion
        except mysql.connector.Error as error:
            messagebox.showerror("Error de conexión",f"No se pudo conectar a la base de datos: {error}")
            return None

        return conexion