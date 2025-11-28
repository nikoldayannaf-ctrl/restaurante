class Menu:
    def __init__(self, controlador):
    #controlador: es un objeto de la clase que Joseph creará.Aquí solo lo recibimos para poder llamar sus funciones.
        self.controlador = controlador

    def mostrar(self):
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Agregar persona")
        print("2. Buscar persona")
        print("3. Actualizar persona")
        print("4. Eliminar persona")
        print("5. Listar personas")
        print("0. Salir")

    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.controlador.agregar_persona()

            elif opcion == "2":
                self.controlador.buscar_persona()

            elif opcion == "3":
                self.controlador.actualizar_persona()

            elif opcion == "4":
                self.controlador.eliminar_persona()

            elif opcion == "5":
                self.controlador.listar_personas()

            elif opcion == "6":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida, intenta de nuevo.")
