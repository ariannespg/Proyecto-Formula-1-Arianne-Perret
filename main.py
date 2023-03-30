import requests
import json
import random

from pilotos import Piloto
from constructores import Constructor
from carrera import Carrera
from circuito import Circuito
from cliente import Cliente
from alimentos import Comida_rapida,Comida_rest,Bebida,Bebida_alcoholica

def bienvenida():
    print ('\n --- Bienvenidos a la Formula 1 --- \n  \n     🚥  🏎️ 🏎️ 💨  🏎️ 🏎️ 🏎️ 💨💨 \n')
    print(' '*25, '🏎️ 🏎️ 🏎️ 💨💨  🏎️ 🏎️ 💨')

#FUNCIONES DE VALIDACION NUMERICA  --------------------------------------------------------------------
 
def numerico_limites(string, menor,mayor):
    option = input(string)
    while True:
        if option.isnumeric() and int(option)>= menor and int(option)<= mayor:
            break
        else:
            option = input ('\n --- Solo introducir caracteres numericos dentro del rango dado ---\n')
    return int(option)

def numerico(string):
    info = input(string)
    while not info.isnumeric():
        info = input("\nIntroduce solo caracteres numericos\n ->")
    return info

#BASES DE DATOS  --------------------------------------------------------------------------------------

def recuperar_clientes(clientes):
    with open("Database_Clientes.txt") as file:
        datos = file.readlines()
        if len(datos) >= 1:
            for dato in datos:
                cliente = dato[:-1].split("@")
                clientes.append(Cliente(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4],cliente[5],cliente[6],cliente[7],cliente[8],cliente[9]))
            file.close()
        elif len(datos) == 0:
            pass

def recuperar_ocupados(clientes,lista_ocupados):
    lista_ocupados = []
    for i in clientes:
        ronda = i.carrera
        asiento = i.asiento
        ocupado = [ronda,asiento]
        lista_ocupados.append(ocupado)    

      
#MODULO 1 ---------------------------------------------------------------------------------------------

#Se crean los objetos y se relacionan los pilotos con los constructores con la info recogida de las APIS y el json
def crear_piloto(nombre, apellido, fecha_nacimiento, lugar_nacimiento, numero, constructor, pilotos_objeto, pilotos):
    nuevo_piloto = Piloto(nombre, apellido, fecha_nacimiento, lugar_nacimiento, numero, constructor, 0)
    pilotos_objeto.append(nuevo_piloto)
    pilotos.append(nuevo_piloto.show_piloto())

def crear_constructor(pilotos, nombre, nacionalidad, id, constructores_objetos, constructores):
    pilotos = emparejar_pilotos_constructores(pilotos, id)
    nuevo_constructor = Constructor(nombre, id, nacionalidad, pilotos, 0)
    constructores_objetos.append(nuevo_constructor)
    constructores.append(nuevo_constructor.show_constructor())
    
def emparejar_pilotos_constructores(pilotos, constructor):
    piloto1_2 = []
    for i in pilotos:
        if getattr(i,'constructor') == constructor:
            piloto1_2.append(i.show_nombre_num()) 
    return piloto1_2
    
#Busqueda de constructores por nacionalidad
def buscar_constructores(constructores):
    nacionalidades = []
    print ('-'*80)
    for constructor in constructores:
        nacionalidades.append(constructor.nacionalidad)
    nacionalidades = list(set(nacionalidades))
    for i, nacionalidad in enumerate(nacionalidades):
        print (f'{i+1} -- {nacionalidad}')
     
    option = numerico_limites('\nIngresa la opcion que deseas\n',1,len(nacionalidades))      

    for constructor in constructores:
        if constructor.nacionalidad == nacionalidades[option-1]:
            print ('-'*80)
            print (constructor.show_constructor())

#Busqueda de pilotos por constructores
def buscar_pilotos(pilotos):
    constructores = []
    print ('-'*80)
    for piloto in pilotos:
        constructores.append(piloto.constructor)
    constructores = list(set(constructores))
    for i, constructor in enumerate(constructores):
        print (f'{i+1} -- {constructor.capitalize()}')
    option = numerico_limites('\nIngresa la opcion que deseas\n', 1, len(constructores))

    for piloto in pilotos:
        if piloto.constructor == constructores[option-1]:
            print ('-'*80)
            print (piloto.show_piloto())

#Se crean los objetos de carreras y circuitos con la info recogida de las APIS y el json
def crear_carrera(nombre, numero,fecha,circuito, pais, carreras_objeto,pilotos, general,vip):
    podio = podium(pilotos)
    nueva_carrera = Carrera(nombre, numero,fecha,circuito, podio,pais,general,vip)
    carreras_objeto.append(nueva_carrera)
    

def crear_circuito(circuit_name,pais,localidad,latitud,longitud, circuitos_objeto):
    nuevo_circuito = Circuito(circuit_name,pais,localidad,latitud,longitud)
    circuitos_objeto.append(nuevo_circuito)

#Funcion que mezcla la lista de pilotos para asignar las posiciones de las carreras, como va iterando a medida que recorre la info del json, la lista siempre es diferente
def podium(pilotos):
    random.shuffle(pilotos)
    posiciones = pilotos[:10]
    podio_ = {posiciones[0]: 25, posiciones[1]: 18,posiciones[2]:15,posiciones[3]:12,posiciones[4]:10,posiciones[5]:8,posiciones[6]:6,posiciones[7]:4, posiciones[8]:2,posiciones[9]:1}
    for key, value in podio_.items():
        key.puntos += value
    return podio_

#Buscar info carreras por pais
def buscar_carreras_circuito(carreras):
    circuitos = []
    print ('-'*80)
    for carrera in carreras:
        circuitos.append(carrera.pais)
    circuitos = list(set(circuitos))
    for i, circuito in enumerate(circuitos):
        print (f'{i+1} -- {circuito}')
    option = numerico_limites('\nIngresa la opcion que deseas\n',1,len(circuitos))     

    for carrera in carreras:
        if carrera.pais == circuitos[option-1]:
            print ('-'*80)
            print (carrera.show_carrera())
            while True:
                opcion_podium = input('Deseas finalizar esta carrera y ver los resultados?\n 1 - SI \n 2 - NO\n')
                if opcion_podium == '1':
                    print (carrera.show_podium())
                    break
                elif opcion_podium == '2':
                    print ('\nTe lo pierdes!!')
                    break
                else:
                    print ('\n --- INTRODUCE UNA OPCION VALIDA ---\n')

#Buscar info carreras por mes
def buscar_mes(carreras):
    opcion = input('Introduce el numero del mes del que deseas obtener informacion\n --> En formato MM, agregar cero si es necesario\n')   
    if len(str(opcion)) == 1:
        opcion = '0'+ str(opcion)
    for i in carreras:                       
        mes_carreras = getattr(i,'fecha')
        if opcion[0] == mes_carreras[5] and opcion[1] == mes_carreras[6]:
            print ('-'*80)
            print (i.show_carrera())
        else:
            pass

#Resultados de competencia de pilotos y constructores mediante la suma de los puntos de las carreras
def resultados(pilotos,constructores):
    p_pilotos = 0
    ganador_p = None
    p_contructores = 0
    ganador_c = None
    for i in pilotos:
        p_aux = getattr(i,'puntos')
        if p_aux > p_pilotos: 
             p_pilotos = p_aux
             ganador_p = i
    print ('-'*80)
    print (f' \n ---> El ganador del campeonato de pilotos es: {ganador_p.show_nombre()} con {p_pilotos} puntos')

    for j in constructores:
        p_aux_c = 0
        equipo = getattr(j,'id_equipo')
        for k in pilotos:
            p_equipo = getattr(k,'constructor')
            if equipo == p_equipo:
                p_aux_c += getattr(k,'puntos')
            if p_aux_c > p_contructores:
                p_contructores = p_aux_c
                ganador_c = j
    print ('-'*80)
    print (f' ---> El ganador del campeonato de constructores es: {ganador_c.show_nombre()}')

#MODULO 2 ---------------------------------------------------------------------------------------------

def get_info_cliente(carreras,clientes,clientes_dict):
    precio = 0
    #Se recogen los datos de identificacion del cliente
    nombre_cliente = input('\nIntroduce tu nombre completo\n -> ')
    cedula_cliente = numerico("\nIntroduce tu numero de cedula\n ->")
    edad_cliente = numerico_limites("\nIntroduce edad\n ->", 1,100)
    
    while True:
        #Se muestran las carreras para que el cliente escoja a la que desea asistir
        print ('A continuacion, las carreras --->\n')
        print ('-'*80)
        for i in carreras:
            i.show_carrera_venta()

        #El cliente podra comprar varias entradas para las diferentes carreras, ya que es un loop, pero mediante pagos diferentes
        carrera_escogida = input('Escoge el numero de la carrera a la que deseas asistir \n ---> Presiona S para salir')
        if carrera_escogida.upper() == 'S' :
            break

        for i in carreras:
            if getattr(i,'numero') == carrera_escogida:
                while True:
                    tipo_de_entrada = input('Escoge el tipo de entrada que deseas adquirir, escribe el numero\n --> 1 - General \n --> 2- VIP\n')
                    if tipo_de_entrada != '1' and tipo_de_entrada != '2':
                        tipo_de_entrada = input ('Introduce una opcion valida\n 1 - SI \n 2 - NO ')
                    else:
                        break
                while True:
                    if tipo_de_entrada == '1':
                        matriz = (getattr(i,'general'))
                        f = matriz[0]
                        c = matriz[1]
                        acceso_rest = False
                        _entrada = 'General'
                        precio = 150
                        precio_iva = precio * 1.16
                        precio_descuento = precio_iva-(precio_iva* ondulado(cedula_cliente))
                        break
                    elif tipo_de_entrada == '2':
                        matriz = (getattr(i,'vip'))
                        f = matriz[0]
                        c = matriz[1]
                        acceso_rest = True
                        _entrada = 'VIP'
                        precio = 340
                        precio_iva = precio * 1.16
                        descuento = (precio_iva* ondulado(cedula_cliente))
                        precio_descuento = precio_iva - descuento
                        break

                mapa = crear_mapa(f,c)
                imprimir_mapa(mapa)
                while True:
                    fila = input('Fila')
                    if fila.isnumeric() and int(fila)<= f and int(fila)>= 1:    #AGREGAR ASIENTOS OCUPADOOOOOOS
                        break
                    else:
                        print('\n Ese numero se encuentra fuera del rango propuesto o es un caracter no numerico')
                
                while True:
                    columna = input('columna')
                    if columna.isnumeric() and int(columna)<= c and int(columna)>= 1:
                        break
                    else:
                        print('\n Ese numero se encuentra fuera del rango propuesto o es un caracter no numerico')

                mapa[int(fila)- 1][int(columna)- 1] = True
                imprimir_mapa(mapa)
                print (f'Has seleccionado el asiento {fila}{columna} con exito')
                while True:
                    proceder = input ('Deseas proceder con la compra (presiona el numero)\n 1 - SI \n 2 - NO ')
                    if proceder != '1' and proceder != '2':
                        proceder = input ('Introduce una opcion valida\n 1 - SI \n 2 - NO ')
                    else:
                        break
                if proceder == '1':
                    factura_entrada(fila,columna,precio,precio_iva,precio_descuento, descuento)
                    codigo = (f'{fila}{columna}-{carrera_escogida}-{cedula_cliente}')
                    asiento = (fila + columna)
                    gastos = 0
                    cliente = Cliente(nombre_cliente, cedula_cliente,edad_cliente,carrera_escogida,_entrada,codigo, acceso_rest, asiento, gastos, False)
                    print (cliente.show())
                    clientes.append(cliente)
                    basededatos_clientes(nombre_cliente, cedula_cliente,edad_cliente,carrera_escogida,_entrada,codigo, acceso_rest, asiento, gastos, False)
                elif proceder == '2':
                    break


#Funcion que crea un mapa a partir de la informacion de la matriz obtenida de la estructura de datos de carreras                                  
def crear_mapa(filas,columnas):
    mapa = []
    for y in range(filas):
        aux = []
        for x in range(columnas):
            aux.append(False)
        mapa.append(aux)
    return mapa

def imprimir_mapa(mapa):
    print ('\n'+"* "*len(mapa[0]) + ' GRADAS '+ " *"*len(mapa[0]))
    print ('\n')
    nums = '   '
    for i,x in enumerate(mapa[0]):
        if i > 8:
            nums += str(i + 1)+"| "
        else:
            nums += str(i + 1)+" |  "
    print (nums)

    for i, x in enumerate(mapa):
        if i > 8:
             aux = str(i +1)
        else:
            aux = str(i +1)+'  '
        for y in x: 
            if y == True:
                aux += "| X  "
            else:
                aux += "|    "
        print('  '+"-"*len(mapa[0]*4))
        print(aux)

#Funcion que imprime la factura con todos los datos de compra
def factura_entrada(fila,columna,total,total_iva,total_descuento, descuento):
    print ('---------- FACTURA ----------\n')
    print (f'Asiento {fila}{columna}')
    print (f'Costo entrada: {total} ')
    print (f'Total con IVA: {total_iva} ')
    print (f'DESCUENTO: {descuento} ')
    print (f'\n --->TOTAL (con descuento): {total_descuento} ')

#Funcion para identificar si la cedula es o no un numero ondulado y asi retornar descuento
def ondulado(numero):
    numero_str = str(numero)
    numeros = []
    es_ondulado = False
    for i in numero_str:
        numeros.append(int(i))
    if len(numero_str) > 0 and len(numero_str) <= 2:
        es_ondulado = True
    else:
        for j in range(len(numeros)-2):
            if numeros[j] != numeros[j+2]:
                es_ondulado = False
            else:
                es_ondulado = True 
    if es_ondulado == True:
        return 0.5
    else:
        return 0
    
# ----------------------------------------------------------------------------------------------------------------------------------------
def basededatos_clientes(nombre,cedula, edad, carrera, entradas, codigos, acceso_restaurantes, asiento, gastos, asistencia):
    with open("Database_Clientes.txt","a+") as file:
            file.write(f"{nombre}@{cedula}@{edad}@{carrera}@{entradas}@{codigos}@{acceso_restaurantes}@{asiento}@{gastos}@{asistencia}\n")
    file.close()
    print("\nCliente registrado con éxito.")
    
#MODULO 3 ---------------------------------------------------------------------------------------------------------------------------------

def asistencia(clientes):
    if len(clientes) == 0:
        print('\n --- ANTES DE CONFIRMAR ASISTENCIA DEBEN HABER CLIENTES ---\n')
    else:
        cedula = input('\nIntroduce tu numero de cedula')
        asiento = input('Introduce tu numero de asiento')

        for i in clientes:
            c_ticket = getattr(i, 'cedula')
            if c_ticket == cedula:
                code_ticket = getattr(i, 'codigos')
                estado_ticket = getattr(i,'asistencia')
                if estado_ticket == True:
                    print(' \n--- Este boleto ya ha sido utilizado ---\n')
                elif code_ticket[0]== asiento[0] and code_ticket[1]== asiento[1]:
                    setattr(i, 'asistencia', True)
                    print ('\n --- Se ha confirmado tu asistencia con exito, recuerda que el boleto no puede ser utilizado de nuevo ---\n')
                elif code_ticket[0]!= asiento[0] or code_ticket[1]!= asiento[1]:
                    print ('\n--- Has ingresado la informacion incorrecta o es un boleto falso\n --> Volver a intentar ---\n')
                
            elif c_ticket != cedula:
                print ('Has ingresado la informacion incorrecta o es un boleto falso\n --> Volver a intentar')


#MODULO 4 ------------------------------------------------------------------------------------------------------------------------------------------

#Funcion para buscar los platos por nombre y tipo
def buscar_plato(lista_objeto, plato):
    for a in lista_objeto:
        plato_op = getattr(a,'nombre')
        if plato_op == plato:
            request = (a.show())
    return request

#Funcion para buscar todos los platos tipo
def buscar_tipo_producto(string, lista_objetos, ronda):
    print (string)
    for p in lista_objetos:
        producto = getattr(p,'ronda')
        if ronda == producto:
            print(p.show())
        else:
            pass

#Funcion para buscar productos por rango de precio
def buscar_por_precio(restaurantes,rapida, bebidas,b_alc, ronda,carrera):
    precio_min = input('\n-->Ingresa el precio minimo\n')
    while not (precio_min.isnumeric() and float(precio_min)) >= 0:
        precio_min = input('\n -- Ingreso invalido -- \n--> Ingresa el precio minimo\n')
    precio_min = float(precio_min)
    precio_max = input('\n-->Ingresa el precio maximo\n')
    while not (precio_max.isnumeric() and float(precio_max)) >= precio_min:
        precio_min = input('\n -- Ingreso invalido -- \n--> Ingresa el precio maximo\n')
    precio_max = float(precio_max)

    lista_productos = []
    listas_por_precio(restaurantes,carrera,precio_min , precio_max,lista_productos)
    listas_por_precio(rapida,carrera,precio_min , precio_max,lista_productos)
    listas_por_precio(bebidas,carrera,precio_min , precio_max,lista_productos)
    listas_por_precio(b_alc,carrera,precio_min , precio_max,lista_productos)

    return lista_productos

#Funcion para escoger los productos en el rango dado y en la carrera escogida
def listas_por_precio(lista, carrera,precio_min , precio_max,lista_productos):
    for i in lista:
        if i.ronda == carrera:
            pass
            if precio_min <= i.precio <= precio_max:
                lista_productos.append(i)
        else:
            pass


#Funcion que recibe las listas de los distintos objetos alimenticios para mostrarselos al cliente
def mostrar_productos(rest, rapida, bebida, b_alc, carreras):
    carrera = input('introduce el numero de la ronda de carrera a la que asistiras para ver el menu:')
    while True:
        opcion = input('Introduce tu metodo de busqueda\n 1 - Nombre de la bebida o plato \n 2 - Tipo de producto \n 3 - Rango de precios\n')
        
        #Busca por nombre del producto
        if opcion == '1':
            plato = input('Introduce el nombre del plato o bebida')
            tipo_plato = input('Introduce la clasificacion del producto\n 1- C. Restaurante \n 2 - C. Rapida \n 3 - Bebida \n 4 - Bebida Alcoholica')
            for i in carreras:
                ronda = getattr(i,'numero')
                if ronda == carrera:
                    continue
                if tipo_plato == '1':
                    request = buscar_plato(rest,plato)
                elif tipo_plato == '2':
                    request = buscar_plato(rapida,plato)
                elif tipo_plato == '3':
                    request = buscar_plato(bebida,plato)    
                elif tipo_plato == '4':
                    request = buscar_plato(b_alc,plato)
            print (request)
            break

        #Busca por tipo de producto
        elif opcion == '2':
            for i in carreras:
                ronda = getattr(i,'numero')
                if ronda == carrera:
                    tipo_prod = input('Introduce la clasificacion del producto\n 1- C. Restaurante \n 2 - C. Rapida \n 3 - Bebida \n 4 - Bebida Alcoholica\n')
                    if tipo_prod == '1':
                        buscar_tipo_producto('\n COMIDA RESTAURANTES \n', rest, ronda)
                    elif tipo_prod == '2':
                        buscar_tipo_producto('\n COMIDA RAPIDA \n', rapida, ronda)
                    elif tipo_prod == '3':
                        buscar_tipo_producto('\n BEBIDAS \n', bebida, ronda)
                    elif tipo_prod == '4':
                        buscar_tipo_producto('\n BEBIDAS ALCOHOLICAS\n', b_alc, ronda)
                    elif tipo_prod == '5':
                        break
            break

        #Busca por rango de precios
        elif opcion == '3':
            for i in carreras:
                ronda = getattr(i,'numero')
                if ronda == carrera:
                    continue

            lista = buscar_por_precio(rest,rapida,bebida,b_alc, ronda, carrera)
            for i in lista:
                print (i.show())
            break
        
        else:
            print ('\n\n INTRODUCE UNA OPCION VALIDA \n')

 #MODULO 5 ---------------------------------------------------------------------------------------------           


def comprar_rest(clientes, rest, rapida, bebida, b_alc):
    cedula = input('\nIntroduce tu numero de cedula')
    asiento = input('Introduce tu numero de asiento')
    productos = []
    gastos = 0

    
    for i in clientes:
        c_ticket = getattr(i, 'cedula')
        if c_ticket == cedula:
            code_ticket = getattr(i, 'codigos')
            if code_ticket[0]== asiento[0] and code_ticket[1]== asiento[1]:
                es_vip = i.entrada
                #Se comprueba la existencia del ticket y que el cliente sea VIP
                if es_vip == 'VIP':
                    while True:
                        #Se consulta el tipo de producto para adquirir
                        producto = input('Introduce el tipo de producto que deseas comprar \n 1 - Restaurante \n 2 - C. Rapida \n 3 - Bebidas\n 4 - Bebidas alcoholicas\n --> Presiona "S" para salir')
                        if producto == '1':
                            #Se comprueba que el producto exista
                            nombre_producto = input('Introduce el nombre del producto que deseas comprar \n')
                            for a in rest:
                                plato_op = getattr(a,'nombre')
                                if plato_op == nombre_producto:
                                    request = (a)
                                #Si no existe, continua
                                else:
                                    pass
                                    
                            productos.append(request)
                        elif producto == '2':
                            nombre_producto = input('Introduce el nombre del producto que deseas comprar \n')
                            for b in rapida:
                                plato_op = getattr(b,'nombre')
                                if plato_op == nombre_producto:
                                    request = (b)
                                else:
                                    pass
                                    
                            productos.append(request)
                        elif producto == '3':
                            nombre_producto = input('Introduce el nombre del producto que deseas comprar \n')
                            for c in bebida:
                                plato_op = getattr(c,'nombre')
                                if plato_op == nombre_producto:
                                    request = (c)
                                else:
                                    pass

                            productos.append(request)
                        elif producto == '4':
                            nombre_producto = input('Introduce el nombre del producto que deseas comprar \n')
                            for d in b_alc:
                                plato_op = getattr(d,'nombre')
                                if plato_op == nombre_producto:
                                    request = (d)
                                else:
                                    pass

                            productos.append(request)

                        #Culmina la compra de articulas
                        elif producto.upper() == 'S':
                            break 
                        else:
                            print ('\nIntroduce una opcion valida \n')

                    for i in productos:
                        gasto = getattr(i,'precio')
                        if gasto == None:
                            pass
                        else:
                            #Calcula los gastos del cliente agregando iva inmediato, descuento, etc
                            print (i.show())
                            gastos += gasto
                            descuento = (gastos*(es_perfecto(cedula)))
                            gasto_descuento = gastos - descuento

                        factura(gastos,gasto_descuento,descuento)

                        #Confirma con el usuario si este desea proceder con la compra, si no desea continua, regresa al menu 
                        opcion_compra = input('Desea proceder con la compra \n 1 - SI \n 2 - NO')
                        if opcion_compra == '1':
                            print (' \n***************   FACTURA   ***************\n\n')
                            print ('-'*50)
                            for i in productos:
                                print (i.show())
                            factura(gastos,gasto_descuento,descuento)
                        elif  opcion_compra == '2':
                            print ('Vuelva pronto')
                            
                #Si el cliente no es VIP no puede acceder a comprar articulos de los restaurantes
                elif es_vip == False:
                    print(' --- ACCESO VALIDO SOLO PARA CLIENTES VIP  ---')

def factura(gastos,gasto_descuento,descuento):
    print (f' TOTAL CON IVA        ------>  {gastos}\n')
    print (f' TOTAL CON DESCUENTO  ------>  {gasto_descuento}\n')
    print (f' DESCUENTO TOTAL      ------>  {descuento}\n')

def es_perfecto(cedula):
    suma_d = 0
    perfecto = 0
    cedula = int(cedula)
    for i in range(1, cedula):
        if cedula % i == 0:
            suma_d += 1
    if suma_d == cedula:
        perfecto = 0.15
    return perfecto

#MODULO 6 ---------------------------------------------------------------------------------------------     

def carrera_mayor_asistencia(ocupados, carreras):
    cont = 0
    mayor = 0
    
    for i in ocupados:
        for j in carreras:
            if j.ronda == i[0]:
                cont += 1
                if cont > mayor:
                    mayor = j
     
            print (f' El circuito con mayor asistencia fue{j.circuito}')

# MAIN ---------------------------------------------------------------------------------------------

def main():

    pilotos_objeto = []
    pilotos = []
    constructores_objetos = []
    constructores = []
    carreras_objeto = []
    circuitos_objeto = []
    clientes_objetos = []
    clientes = []
    comida_rest = []
    comida_rap = []
    bebidas = []
    bebidas_alc = []
    ocupados = []

    bienvenida()

    #Funciones que recuperan info del txt
    recuperar_clientes(clientes_objetos)
    recuperar_ocupados(clientes_objetos,ocupados)


    #Se recolecta la info de las API y se guarda en archivos json (Pilotos)
    request_pilotos = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json")
    contenido_pilotos = request_pilotos.content
    info_pilotos = open("pilotos.json","wb")
    info_pilotos.write(contenido_pilotos)
    info_pilotos.close()     

    #Se recolecta la info de las API y se guarda en archivos json (Constructores)
    request_constructores = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json')
    contenido_constructores = request_constructores.content
    info_constructores = open("constructores.json","wb")
    info_constructores.write(contenido_constructores)
    info_constructores.close()

    #Se recolecta la info de las API y se guarda en archivos json (Carreras y circuitos)
    request_carreras = requests.get('https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json')
    contenido_carreras = request_carreras.content
    info_carreras = open("carreras.json","wb")
    info_carreras.write(contenido_carreras)
    info_carreras.close()


    #Se recoge la informacion de los pilotos y se utiliza la funcion para convertir en objeto
    archivo_pilotos = open("pilotos.json")
    datos_pilotos = json.load(archivo_pilotos)

    for i in range(0, len(datos_pilotos)):
        p_nombre = datos_pilotos[i]['firstName']
        apellido = datos_pilotos[i]['lastName']
        fecha_nacimiento = datos_pilotos[i]['dateOfBirth']
        lugar_nacimiento = datos_pilotos[i]['nationality']
        numero = datos_pilotos[i]['permanentNumber']
        equipo = datos_pilotos[i]['team']
        crear_piloto(p_nombre, apellido, fecha_nacimiento, lugar_nacimiento, numero, equipo, pilotos_objeto, pilotos)

    info_pilotos.close() 

    #Se recoge la informacion de los constructores y se utiliza la funcion para convertir en objeto
    archivo_constructores = open("constructores.json")
    datos_constructores = json.load(archivo_constructores)
    
    
    for i in range(0, len(datos_constructores)):
        c_nombre = datos_constructores[i]['name']
        nacionalidad = datos_constructores[i]['nationality']
        id = datos_constructores[i]['id']
        
        crear_constructor(pilotos_objeto, c_nombre, nacionalidad, id, constructores_objetos, constructores)

    info_constructores.close() 


    #Se recoge la informacion de las carreras y se utiliza la funcion para convertir en objeto
    archivo_carreras = open("carreras.json")
    datos_carreras = json.load(archivo_carreras)

    for i in range(0, len(datos_carreras)):
        carrera_nombre = datos_carreras[i]['name']
        fecha = datos_carreras[i]['date']
        ronda = datos_carreras[i]['round']
        circuit = datos_carreras[i]['circuit']
        circuit_name = circuit.get('name')
        location = circuit.get('location')
        latitud = location.get('lat')
        longitud = location.get('long')
        localidad = location.get('locality')
        pais = location.get('country')
        mapa = datos_carreras[i]['map']
        general = mapa.get('general')
        vip = mapa.get('vip')
        restaurantes = datos_carreras[i]['restaurants']

        crear_carrera(carrera_nombre, ronda,fecha,circuit_name, pais, carreras_objeto, pilotos_objeto, general,vip)  
        crear_circuito(circuit_name,pais,localidad,latitud,longitud, circuitos_objeto)

#---------------------------------------------------------------------------------------------
#Se recoge la informacion de los restaurantes y se utiliza la funcion para convertir en objeto

        for p in restaurantes:
            for i,j in p.items():
                nombre_rest = p.get('name')
                items_rest = p.get('items')
                for q in items_rest:
                    nombre_c = q.get('name')
                    tipo = q.get('type')
                    precio = q.get('price')
                    precio = (float(precio) * 1.16)
                    if tipo == 'food:restaurant':
                        nuevo_alimento = Comida_rest(nombre_rest, carrera_nombre, ronda, nombre_c, precio)
                        comida_rest.append(nuevo_alimento)
                    elif tipo == "food:fast":
                        nuevo_alimento = Comida_rapida(nombre_rest, carrera_nombre, ronda, nombre_c, precio)
                        comida_rap.append(nuevo_alimento)
                    elif tipo == "drink:alcoholic":
                        nuevo_alimento = Bebida_alcoholica(nombre_rest, carrera_nombre, ronda, nombre_c, precio)
                        bebidas_alc.append(nuevo_alimento)
                    elif tipo == "drink:not-alcoholic":
                        nuevo_alimento = Bebida(nombre_rest, carrera_nombre, ronda, nombre_c, precio)
                        bebidas.append(nuevo_alimento)
     
    info_constructores.close()


#MENU PRINCIPAL ---------------------------------------------------------------------------------------------

    while True:
        print ("-"*80)
        option = input('\n INTRODUCE UNA OPCION\n\n---> 1 - Carreras y equipos \n---> 2 - Comprar entradas \n---> 3 - Confirmar asistencia \n---> 4 - VER MENU Restaurantes \n---> 5 - Comprar Restaurantes ( SOLO VIP )\n---> 6 - Estadisticas \n---> 7 - Terminar sesion\n')
        if option == '1':
            while True:
                print ("-"*80)
                option_1 = input(' INTRODUCE UNA OPCION \n --> 1 - Buscar constructores por pais \n --> 2 - Buscar pilotos por constructor \n --> 3 - Buscar a las carreras por país del circuito\n --> 4 - Buscar todas las carreras que ocurran en un mes \n --> 5 - Resultados \n --> 6 - REGRESAR AL MENU\n')
                if option_1 == '1':
                    buscar_constructores(constructores_objetos)
                elif option_1 == '2':
                    buscar_pilotos(pilotos_objeto)
                elif option_1 == '3':
                    buscar_carreras_circuito(carreras_objeto)
                elif option_1 == '4':
                    buscar_mes(carreras_objeto)
                elif option_1 == '5':
                    resultados(pilotos_objeto, constructores_objetos )
                elif option_1 == '6':
                    break
                else:      
                    print ('\n\n INTRODUCE UNA OPCION VALIDA \n',(10*'>'),('\n'))
        
        elif option == '2':
            get_info_cliente(carreras_objeto, clientes_objetos,clientes)
        elif option == '3':
            asistencia(clientes_objetos)
        elif option == '4':
            mostrar_productos(comida_rest,comida_rap,bebidas,bebidas_alc,carreras_objeto)
        elif option == '5':
            comprar_rest( clientes_objetos, comida_rest,comida_rap,bebidas,bebidas_alc)
        elif option == '6':
            pass
        elif option == '7':
            break
        else:
            print ('\n\n INTRODUCE UNA OPCION VALIDA \n',(10*'>'),('\n'))

main()