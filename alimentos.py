class Alimentos:
    def __init__(self, restaurante, carrera, ronda,nombre,precio, inventario):
        self.restaurante = restaurante
        self.carrera = carrera
        self.ronda = ronda
        self.nombre = nombre
        self.precio = precio
        self.inventario = inventario

    def show(self):
        pass

class Comida_rest(Alimentos):
    def __init__(self, restaurante, carrera, ronda,nombre, precio):
        super().__init__(restaurante, carrera, ronda,nombre, precio, 50)
    
    def show(self):
        return(f' {self.nombre} -- {self.precio}  -- {self.restaurante}')

class Comida_rapida(Alimentos):
    def __init__(self, restaurante, carrera, ronda, nombre, precio):
        super().__init__(restaurante, carrera,ronda, nombre, precio,50)

    def show(self):
        return(f' {self.nombre} -- {self.precio}  -- {self.restaurante}')

class Bebida(Alimentos):
    def __init__(self, restaurante, carrera, ronda,nombre, precio):
        super().__init__(restaurante, carrera, ronda, nombre, precio,100)

    def show(self):
        return(f' {self.nombre} -- {self.precio}  -- {self.restaurante}')

class Bebida_alcoholica(Alimentos):
    def __init__(self, restaurante, carrera, ronda, nombre, precio):
        super().__init__(restaurante, carrera, ronda, nombre, precio,100)

    def show(self):
        return(f' {self.nombre} -- {self.precio}  -- {self.restaurante}')
