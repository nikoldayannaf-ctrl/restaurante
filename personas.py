class Persona:
    def _init_(self, nombre, apellido, documento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento

    def _str_(self):
        return f"{self.nombre} {self.apellido} - Documento: {self.documento}"