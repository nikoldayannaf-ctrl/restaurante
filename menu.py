class Menu:
    def __init__(self, controlador):
        # controlador: objeto de ControladorRestaurante
        self.controlador = controlador

    def mostrar(self):
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Listar pedidos")
        print("2. Filtrar pedidos por categoría")
        print("3. Total vendido por mes")
        print("4. Ventas por mesero")
        print("5. Buscar pedido por ID")
        print("0. Salir")

    def ejecutar(self):
        while True:
            self.mostrar()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.controlador.listar_pedidos()

            elif opcion == "2":
                self.controlador.filtrar_por_categoria()

            elif opcion == "3":
                self.controlador.total_por_mes()

            elif opcion == "4":
                self.controlador.ventas_por_mesero()

            elif opcion == "5":
                self.controlador.buscar_pedido()

            elif opcion == "0":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida, intenta de nuevo.")
