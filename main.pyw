from modelo import InventarioModelo
from vista import InventarioVista
from controlador import InventarioControlador


def iniciar_app():
    #instanciamos el Modelo.
    modelo = InventarioModelo()
    #instanciamos la vista
    vista = InventarioVista()
    #instanciamos el controlador
    controlador = InventarioControlador(modelo, vista)

    vista.root.mainloop()

if __name__ == '__main__':
    iniciar_app()