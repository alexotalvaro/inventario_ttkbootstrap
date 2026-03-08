import ttkbootstrap as tb

class InventarioLogin:
    def __init__(self,controlador):
        self.root = tb.Toplevel(controlador.vista.root)
        self.root.title("Login de usuario")
        self.root.minsize(500, 500)
        self.controlador = controlador
        self.crear_interfaz()

    def crear_interfaz(self):
        # El Frame debe expandirse para que se vea
        caja_login = tb.Frame(self.root, padding=20)
        caja_login.pack(fill="both", expand=True)

        tb.Label(caja_login, text="Usuario", font=("Helvetica", 12)).pack(pady=10)
        self.entry_usuario = tb.Entry(caja_login)
        self.entry_usuario.pack(fill="x", padx=20)

        tb.Label(caja_login, text="Password", font=("Helvetica", 12)).pack(pady=10)
        self.entry_password = tb.Entry(caja_login, show="*")
        self.entry_password.pack(fill="x", padx=20)

        # Botón para ejecutar la lógica de validación
        tb.Button(caja_login, text="Iniciar sesión", bootstyle="success",command=self.enviar_datos).pack(pady=20)

    def enviar_datos(self):
        usuario=self.entry_usuario.get()
        password=self.entry_password.get()
        self.controlador.validar_usuario(usuario,password)