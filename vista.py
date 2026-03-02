import emoji
import ttkbootstrap as tb

class InventarioVista:
    def __init__(self):
        self.root=tb.Window(themename="darkly")
        self.root.title("Gestion de Inventario")
        self.root.minsize(1100,600)

# Configuramos las columnas para que se estiren por igual
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        # Aqui llamamos a todo
        self._crear_interfaz()

    def _crear_interfaz(self):
        # --- FILA TITULO (titulo) ---
        # Caja Abajo (Fila 1, Columna 0... ¡pero ocupa 2 columnas!)
        caja_titulo = tb.Frame(self.root, bootstyle="primary", padding=10)
        caja_titulo.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        caja_titulo.columnconfigure(0, weight=1)
        tb.Label(caja_titulo, text="Nombre de la empresa", bootstyle="inverse-primary", font="Helvetica").grid(row=0,column=0,sticky="w")
        boton_login=tb.Button(caja_titulo, text="Login "+emoji.emojize("👨‍💻"), bootstyle="submit")
        boton_login.grid(row=0,column=0,sticky="e")

        # --- FILA 0 (Arriba) ---
        # Caja Arriba Izquierda (Fila 0, Columna 0) FORMULARIO
        caja_izq = tb.Frame(self.root, bootstyle="primary", padding=20)
        caja_izq.columnconfigure(0, weight=1)
        caja_izq.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        tb.Label(caja_izq, text="Añadir producto", bootstyle="light", anchor="center", justify="center").grid(row=0,column=0,sticky="nsew",padx=10, pady=10)
        frame_formulario=tb.Frame(caja_izq, bootstyle="primary", padding=20, borderwidth=1, relief="solid")
        frame_formulario.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        frame_formulario.columnconfigure(0, weight=1)
        label_nombre=tb.Label(frame_formulario, text="Nombre", style="primary.Inverse.TLabel")
        label_nombre.grid(row=0,column=0,sticky="w", pady=(5,10))
        self.entry_nombre=tb.Entry(frame_formulario)
        self.entry_nombre.grid(row=0,column=0,sticky="e")
        label_precio=tb.Label(frame_formulario, text="Precio", style="primary.Inverse.TLabel")
        label_precio.grid(row=1,column=0,sticky="w", pady=(10,5))
        self.entry_precio=tb.Entry(frame_formulario)
        self.entry_precio.grid(row=1,column=0,sticky="e", pady=(10,5))
        label_descripcion=tb.Label(frame_formulario, text="Descripcion", style="primary.Inverse.TLabel")
        label_descripcion.grid(row=2,column=0,sticky="w")
        self.entry_descripcion=tb.Entry(frame_formulario)
        self.entry_descripcion.grid(row=2,column=0,sticky="e",pady=(5,10))
        self.boton_anadir=tb.Button(frame_formulario, text="Añadir", bootstyle="[solid_button, dark]")
        self.boton_anadir.grid(row=3,column=0,sticky="ew")

        # Caja Arriba Derecha (Fila 0, Columna 1) BUSCADOR
        caja_der = tb.Frame(self.root, bootstyle="primary", padding=20)
        caja_der.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        caja_der.columnconfigure(0, weight=1)
        tb.Label(caja_der, text="Buscar producto", bootstyle="light", anchor="center", justify="center").grid(row=0,column=0,sticky="nsew", pady=10)

        frame_buscar=tb.Frame(caja_der, bootstyle="primary", padding=20, borderwidth=1, relief="solid")
        frame_buscar.grid(row=1, column=0, sticky="ew", pady=10)
        frame_buscar.columnconfigure(0, weight=1)
        self.entry_buscar=tb.Entry(frame_buscar)
        self.entry_buscar.grid(row=0, column=0, sticky="ew", padx=10)

        frame_botones = tb.Frame(frame_buscar,bootstyle="primary")
        frame_botones.grid(sticky="sew",pady=25)
        frame_botones.columnconfigure(0, weight=1)
        frame_botones.columnconfigure(1, weight=1)
        self.boton_buscar=tb.Button(frame_botones,text="Buscar", bootstyle="dark")
        self.boton_buscar.grid(row=0, column=0, sticky="ew",padx=(10,10))
        self.boton_mostrartodo=tb.Button(frame_botones,text="Mostrar Todos", bootstyle="dark")
        self.boton_mostrartodo.grid(row=0, column=1, sticky="ew", padx=(10,10))

        # --- FILA 1 (Abajo) ---
        # Caja Abajo (Fila 1, Columna 0... ¡pero ocupa 2 columnas!) TABLA
        caja_abajo = tb.Frame(self.root, bootstyle="primary", padding=20)
        caja_abajo.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        # --- Configuración de la Tabla con Scrollbar ---
        frame_tabla = tb.Frame(caja_abajo, bootstyle="primary", padding=10)
        frame_tabla.pack(fill="both", expand=True)

        # Configurar el peso del grid en el frame para que la tabla se estire
        frame_tabla.columnconfigure(0, weight=1)
        frame_tabla.rowconfigure(0, weight=1)

        # 1. Definir columnas
        columnas = ("id", "nombre", "precio", "descripcion")
        self.tabla = tb.Treeview(frame_tabla, bootstyle="secondary", columns=columnas, show="headings", height=5)

        # 2. Configurar Encabezados (Lo que se ve arriba)
        self.tabla.heading("id", text="ID", anchor="center")
        self.tabla.heading("nombre", text="Nombre", anchor="w") # 'w' es alineado a la izquierda
        self.tabla.heading("precio", text="Precio", anchor="w")
        self.tabla.heading("descripcion", text="Descripcion", anchor="center")

        # 3. Ocultamos el ID de la tabla
        self.tabla["displaycolumns"]=("nombre","precio","descripcion")

        # 4. Configurar Columnas (Lo que alinea los datos de abajo)
        # El 'anchor' aquí debe coincidir con el del encabezado para que se vean alineados
        self.tabla.column("id", width=200, anchor="center", stretch=False)
        self.tabla.column("nombre", width=200, anchor="w")
        self.tabla.column("precio", width=200, anchor="w")
        self.tabla.column("descripcion", width=250, anchor="center")
        self.tabla.grid(row=0, column=0, sticky="nsew")

        self.boton_eliminar = tb.Button(caja_abajo,text="Eliminar", bootstyle="dark")
        self.boton_modificar = tb.Button(caja_abajo, text="Modificar", bootstyle="dark")
        self.boton_eliminar.pack(side="left", expand=True,anchor="e", padx=5, pady=10)
        self.boton_modificar.pack(side="left", expand=True,anchor="w", padx=5, pady=10)
