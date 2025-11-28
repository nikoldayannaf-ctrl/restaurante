from personas import Persona

class ControladorPersonas:
    def __init__(self):
        self.personas = []  # lista donde guardamos los objetos Persona

    def agregar_persona(self):
        print("\n--- Agregar Persona ---")
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        documento = input("Ingrese documento: ")

        # verificar si ya existe
        for persona in self.personas:
            if persona.documento == documento:
                print(" Ya existe una persona con ese documento.")
                return

        nueva = Persona(nombre, apellido, documento)
        self.personas.append(nueva)
        print("✔ Persona agregada correctamente.")

    def buscar_persona(self):
        print("\n--- Buscar Persona ---")
        documento = input("Ingrese documento a buscar: ")

        for persona in self.personas:
            if persona.documento == documento:
                print("✔ Persona encontrada:")
                print(persona)
                return

        print(" No se encontró una persona con ese documento.")

    def actualizar_persona(self):
        print("\n--- Actualizar Persona ---")
        documento = input("Ingrese documento de la persona a actualizar: ")

        for persona in self.personas:
            if persona.documento == documento:
                print("Persona encontrada. Ingrese los nuevos datos:")
                persona.nombre = input("Nuevo nombre: ")
                persona.apellido = input("Nuevo apellido: ")
                persona.documento = input("Nuevo documento: ")

                print("✔ Persona actualizada correctamente.")
                return

        print(" No se encontró una persona con ese documento.")

    def eliminar_persona(self):
        print("\n--- Eliminar Persona ---")
        documento = input("Ingrese documento a eliminar: ")

        for persona in self.personas:
            if persona.documento == documento:
                self.personas.remove(persona)
                print("✔ Persona eliminada correctamente.")
                return

        print(" No se encontró una persona con ese documento.")

    def listar_personas(self):
        print("\n--- Lista de Personas ---")
        if not self.personas:
            print("No hay personas registradas.")
            return

        for persona in self.personas:
            print(persona)