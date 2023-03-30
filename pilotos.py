class Piloto():
    def __init__(self, nombre, apellido, fecha_nacimiento, lugar_nacimiento, numero, constructor,puntos):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.numero = numero
        self.constructor = constructor
        self.puntos = puntos

    def show_piloto(self):
        return (f'{self.apellido}, {self.nombre} -- {self.numero} \n - Fecha de nacimiento: {self.fecha_nacimiento} \n - Lugar de nacimiento: {self.lugar_nacimiento}\nPUNTOS: {self.puntos}')
    

    def show_nombre_num(self):
        return (f'{self.apellido}, {self.nombre} -- {self.numero}')
    
    def show_nombre(self):
        return (f'{self.apellido}, {self.nombre}')