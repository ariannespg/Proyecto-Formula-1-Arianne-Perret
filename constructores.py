class Constructor:
    def __init__(self, nombre, id_equipo, nacionalidad, pilotos, puntos):
        self.nombre = nombre
        self.id_equipo = id_equipo
        self.nacionalidad = nacionalidad
        self.pilotos = pilotos
        self.puntos = puntos

    def show_constructor(self):
        piloto_1 = self.pilotos[0]
        piloto_2 = self.pilotos[1]

        return (f'     Escuderia {self.nombre} --  ID: {self.id_equipo} - Nacionalidad: {self.nacionalidad} \n\n- Pilotos:\n  -> {piloto_1}\n  -> {piloto_2} \n')
    
    def show_nombre(self):
        return(f' Escuderia {self.nombre}')