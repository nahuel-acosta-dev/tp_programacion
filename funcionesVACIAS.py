from principal import *
from configuracion import *
import random
import math
from extras import *


################################################################
#-------------------FUNCIONES TERMINADAS-----------------------------------#
#### FUNCION LECTURA() ###
### FUNCION BUSCAR_PRODUCTO() ###
### FUNCION PROCESAR() ###
### FUNCION DAME_PRODUCTO() ###
#-------------------------------------------------------------------------#
################################################################

################################################################
#RECORDAR HACER git pull ANTES DE EMPEZAR A PROGRAMAR PARA ACTUALIZAR SU PROYECTO LOCAL
###############################################################

# lee el archivo y carga en la lista lista_producto todas las palabras

# comentario de prueba

def lectura():
    with open('productos.txt', 'r') as file:
        lines = file.readlines()

    array = []

    for line in lines:
        """usamos strip para eliminar espacion al principio y al final de la cadenas. 
            con split dividimos por (,), es decir cada elemento del subarray  se obtiene a partir de dividir en el momento
            que encontremos la (,) en el txt"""
        subarray = line.strip().split(',')

        subarray[1] = int(subarray[1])
        subarray[2] = int(subarray[2])

        array.append(subarray)

    return array


# De la lista de productos elige uno al azar y devuelve una lista de 3 elementos, el primero el nombre del producto , el segundo si es economico
# o premium y el tercero el precio.
def buscar_producto(lista_productos, excluidos):
    
    nombres_excluidos = [excluido[0] for excluido in excluidos]
    productos_disponibles = [producto for producto in lista_productos if producto[0] not in nombres_excluidos]

    # se le da el array que devuelve la funcion lectura() y te da un array al azar economico o premium
    
    if not productos_disponibles:
        return None  # Si no hay productos disponibles, devolvemos None

    producto_aleatorio = random.choice(productos_disponibles)
    producto_aleatorio = producto_aleatorio.copy()

    numero_aleatorio = random.randint(1, 2)

    if numero_aleatorio == 1:
        valor = producto_aleatorio[1]
        producto_aleatorio[1] = " (Eco)"
        producto_aleatorio[2] = valor
    else:
        producto_aleatorio[1] = " (Pre)"
    return producto_aleatorio

###############################################################################
# Elige el producto. Debe tener al menos dos productos con un valor similar
# def dameProducto(lista_productos, margen):
#     producto = buscarProductosSimilares(lista_productos, margen)
#     return producto

def dameProducto(lista_productos, margen):
    max_intentos = len(lista_productos)
    intentos = 0
    producto_probados = []
    
    while intentos < max_intentos:
        producto_aleatorio = buscar_producto(lista_productos, producto_probados)
        contadorProductosSimilares = 0
        
        
        for producto in lista_productos:
            
            if producto[0] != producto_aleatorio[0]:
                if producto_aleatorio[2] >= producto[1]:
                    diferencia_1 = producto_aleatorio[2] - producto[1]
                else:
                    diferencia_1 = producto[1] - producto_aleatorio[2]
                    
                if producto_aleatorio[2] >= producto[1]:
                    diferencia_2 = producto_aleatorio[2] - producto[2]
                else:
                    diferencia_2 = producto[2] - producto_aleatorio[2] 
    
                if diferencia_1 <= margen and diferencia_2 <= margen:
                    contadorProductosSimilares +=1
                    
                if contadorProductosSimilares >= 2:
                    return producto_aleatorio
        producto_probados.append(producto_aleatorio)    
        intentos += 1  # Incrementamos el contador de intentos para evitar un bucle infinito en caso de que el txt este mal
        
        
    return None
    
################################################################################


# Devuelve True si existe el precio recibido como parametro aparece al menos 3 veces. Debe considerar el Margen.
def esUnPrecioValido(precio, lista_productos, margen):
    return True

# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro
# del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente
# el producto


def procesar(producto_principal, producto_candidato, margen):
    if producto_principal[2] - producto_candidato[2]< margen and producto_principal[2] - producto_candidato[2] >- margen:
        sonido_correcto()
        return producto_candidato[2]
    sonido_incorrecto()
    return 0

# Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
# De manera aleatoria se debera tomar el valor economico o el valor premium. Agregar al nombre '(economico)' o '(premium)'
# para que sea mostrado en pantalla.


def dameProductosAleatorios(producto, lista_productos, margen):
    productos_seleccionados = [["Monitor de computadora", "(premium)", 2870],
                               ["Silla de oficina", "(economico)", 3174],
                               ["Lavadora", "(premium)", 4197],
                               ["Refrigerador", "(premium)", 4533],
                               ["Laptop", "(economico)", 4650],
                               ["Cafetera", "(economico)", 2358]]
    return productos_seleccionados
