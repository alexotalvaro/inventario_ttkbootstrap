from ttkbootstrap.dialogs import Messagebox

class InventarioControlador():
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.vista.boton_anadir.config(command=self.anadir_producto)
        self.mostrar_productos()

    def limpiar_campos(self):
        self.vista.entry_nombre.delete(0, "end")
        self.vista.entry_precio.delete(0, "end")
        self.vista.entry_descripcion.delete(0, "end")
        self.vista.entry_buscar.delete(0, "end")

    def mostrar_productos(self):
        resultado = self.modelo.obtener_productos()
        # Limpia la tabla antes de cargar nuevos datos (asi evitamos duplicados)
        for i in self.vista.tabla.get_children():
            self.vista.tabla.delete(i)
        # Insertamos los datos en la tabla
        for datos in resultado:
            self.vista.tabla.insert("", "end", values=datos)

        return resultado

    def anadir_producto(self):
        nombre = self.vista.entry_nombre.get()
        precio = self.vista.entry_precio.get()
        descripcion = self.vista.entry_descripcion.get()
        if nombre == "" or precio == "" or descripcion == "":
            Messagebox.show_error("Rellena todos los campos", "Error")
            return
        try:
            precio = float(precio)
        except:
            Messagebox.show_error("Precio debe ser un número", "Error")

        self.modelo.anadir_producto(nombre, precio, descripcion)
        self.mostrar_productos()
        self.limpiar_campos()

