from ttkbootstrap.dialogs import Messagebox

class InventarioControlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.usuario = "vendedor"
        self.vista.boton_anadir.config(command=self.anadir_producto)
        self.vista.boton_eliminar.config(command=self.eliminar_producto)
        self.vista.boton_buscar.config(command=self.buscar_productos)
        self.vista.boton_mostrartodo.config(command=self.mostrar_productos)
        self.vista.boton_modificar.config(command=self.modificar_producto)
        self.vista.boton_login.config(command=self.iniciar_sesion)
        self.aplicar_permisos()
        self.mostrar_productos()

    def aplicar_permisos(self):
        if self.usuario == "vendedor":
            self.vista.boton_modificar.config(state="disabled")
            self.vista.boton_eliminar.config(state="disabled")
        else:
            self.vista.boton_modificar.config(state="normal")
            self.vista.boton_eliminar.config(state="normal")

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


    def eliminar_producto(self):
        seleccionado=self.vista.tabla.selection()
        if seleccionado:
            for item in seleccionado:
                valor_fila=self.vista.tabla.item(item)['values']
                id_producto=valor_fila[0]
                self.modelo.eliminar_producto(id_producto)
        self.mostrar_productos()


    def buscar_productos(self):
        buscado=self.vista.entry_buscar.get()
        if buscado == "":
            Messagebox.show_info("No estas buscando nada", "Advertencia")
            return
        for i in self.vista.tabla.get_children():
            self.vista.tabla.delete(i)
        resultado=self.modelo.buscar_producto(buscado)
        for producto in resultado:
            self.vista.tabla.insert("", "end", values=producto)

        self.limpiar_campos()


    def modificar_producto(self):
        seleccionado=self.vista.tabla.selection()
        if seleccionado:
            nombre = self.vista.entry_nombre.get()
            precio = self.vista.entry_precio.get()
            descripcion = self.vista.entry_descripcion.get()
            try:
                precio = float(precio)
            except:
                Messagebox.show_error("Precio tiene que ser un número", "Error")
                return
            for item in seleccionado:
                valor_fila=self.vista.tabla.item(item)['values']
                id_producto=valor_fila[0]
                self.modelo.modificar_producto(nombre, precio, descripcion,id_producto)
            Messagebox.show_info("Producto modificado correctamente", "¡Bien!")
            self.mostrar_productos()
            self.limpiar_campos()
        else:
            Messagebox.show_info("No has seleccionado nada", "¡Vaya!")
            return

    def iniciar_sesion(self):
        from login import InventarioLogin
        self.ventana_login = InventarioLogin(self)

    def validar_usuario(self,usuario,password):
        if self.modelo.validar_usuario(usuario,password):
            self.usuario=usuario
            self.ventana_login.root.destroy()
            self.aplicar_permisos()
        else:
            Messagebox.show_info("Credenciales incorrectas", "Error")
