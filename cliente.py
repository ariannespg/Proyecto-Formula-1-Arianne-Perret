class Cliente:
    def __init__(self, nombre, cedula, edad, carrera, entradas, codigos, acceso_restaurantes, asiento, gastos, asistencia ):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.carrera = carrera
        self.entrada = entradas
        self.codigos = codigos
        self.acceso_restaurantes = acceso_restaurantes
        self.asiento = asiento
        self.gastos = gastos
        self.asistencia = asistencia

    
    def show(self):

        return (f' CLIENTE --> {self.nombre}  --   ID: {self.cedula}  --  Edad:{self.edad}  -- {self.carrera} -- CODIGO: {self.codigos} -- ASIENTO: {self.asiento} -- ASISTENCIA {self.asistencia}\n')
        

