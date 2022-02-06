class Universidad():
    def __init__(self, nombre):
        self.nombreUni = nombre

class Carrera():
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("nombre: {}, edad: {}, universidad: {}, especialidad: {}".format(self.nombre, self.edad, self.nombreUni, self.especialidad))

persona = Estudiante("Sabana")
persona.carrera("sistemas")
persona.datos("carlos", 28)
