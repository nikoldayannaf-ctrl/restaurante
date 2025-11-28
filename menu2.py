from menu import Menu
from controlador import ControladorPersonas   # esto lo hará Joseph

class App:
    def __init__(self):
        self.controlador = ControladorPersonas()
        self.menu = Menu(self.controlador)

    def iniciar(self):
        self.menu.ejecutar()


if __name__ == "__main__":
    app = App()
    app.iniciar()
