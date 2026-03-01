class InventarioControlador():
    def __init__(self,modelo,vista):
        self.modelo = modelo
        self.vista = vista
        self.mostrar_productos()


    def mostrar_productos(self):
        resultado=self.modelo.obtener_productos()
        # Limpia la tabla antes de cargar nuevos datos (asi evitamos duplicados)
        for i in self.vista.tabla.get_children():
            self.vista.tabla.delete(i)
        # Insertamos los datos en la tabla
        for datos in resultado:
            self.vista.tabla.insert("","end",values=datos)

        return resultado
