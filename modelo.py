from tkinter import messagebox
import mysql.connector


class InventarioModelo:
    def __init__(self):
        self.conexion = None
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
            messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {error}")
            return None

        return conexion

    # Método que recoge los datos de la Base de Datos y devuelve la lista con el resultado (fetchall())
    def obtener_productos(self):
        conexion=self.conectar()
        cursor = conexion.cursor()
        query= "SELECT * FROM producto"
        cursor.execute(query)
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado

    def anadir_producto(self, nombre, precio, descripcion):
        conexion=self.conectar()
        cursor = conexion.cursor()
        query= "INSERT INTO producto (nombre,precio, descripcion) VALUES (%s, %s, %s)"
        valores = (nombre, precio, descripcion)
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        conexion.close()


    def eliminar_producto(self, id):
        conexion=self.conectar()
        cursor = conexion.cursor()
        query= "DELETE FROM producto WHERE id = %s"
        valores = (id,)
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        conexion.close()

    def buscar_producto(self, nombre):
        conexion=self.conectar()
        cursor = conexion.cursor()
        query="SELECT * FROM producto WHERE nombre LIKE %s"
        valores = (f"%{nombre}%",)
        cursor.execute(query, valores)
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado


    def modificar_producto(self,nombre,precio,descripcion,id):
        conexion=self.conectar()
        cursor = conexion.cursor()
        query= "UPDATE producto SET nombre= %s, precio = %s, descripcion = %s WHERE id = %s"
        valores = (nombre,precio,descripcion,id)
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        conexion.close()

