class Carrera:
    def __init__(self,nombre, numero,fecha,circuito, podium, pais,general, vip):
        self.nombre = nombre
        self.numero = numero
        self.fecha = fecha
        self.circuito = circuito
        self.podium = podium
        self.pais = pais
        self.general = general
        self.vip = vip




    def show_carrera(self):

        print (f'    --  {self.nombre}  --   {self.fecha}  --  {self.pais}  --\nCircuito:{self.circuito} \nRonda: {self.numero}')
        
    
    def show_podium(self):
        print (f'\nPodium: ')
        for i, j in self.podium.items():
            print (f'{i.show_nombre()} - {j} puntos')

            
    def show_carrera_venta(self):

        print (f'   {self.numero} -- {self.nombre}  --   {self.fecha}  --  {self.pais}  -- {self.circuito} \n')
        
