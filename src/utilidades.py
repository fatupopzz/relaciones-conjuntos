"""
Utilidades para el manejo de entrada y salida de datos.
Contiene funciones para parsing de conjuntos y relaciones.
"""

import re


def convertir_elemento(elemento_str):
    """
    Convierte un string a su tipo apropiado (int, float, o string).
    
    Args:
        elemento_str (str): String a convertir
        
    Returns:
        Elemento convertido al tipo apropiado
    """
    elemento_str = elemento_str.strip()
    
    try:
        # Intentar convertir a entero
        if '.' not in elemento_str:
            return int(elemento_str)
        else:
            # Intentar convertir a float
            return float(elemento_str)
    except ValueError:
        # Si no es número, mantener como string
        return elemento_str


def crear_conjunto_desde_entrada(entrada):
    """
    Convierte una entrada de string a conjunto.
    
    Args:
        entrada (str): String con elementos separados por comas (ej: "a,b,c,1,2")
        
    Returns:
        set: Conjunto con los elementos parseados
    """
    # Limpiar la entrada
    entrada = entrada.strip().replace('{', '').replace('}', '')
    elementos = []
    
    if entrada:
        # Dividir por comas y procesar cada elemento
        partes = entrada.split(',')
        for parte in partes:
            elemento = convertir_elemento(parte)
            elementos.append(elemento)
    
    return set(elementos)


def crear_relacion_desde_entrada(entrada):
    """
    Convierte una entrada de string a relación (conjunto de pares ordenados).
    
    Args:
        entrada (str): String con pares ordenados (ej: "(1,a),(2,b),(3,c)")
        
    Returns:
        set: Conjunto de tuplas representando la relación
    """
    entrada = entrada.strip().replace('{', '').replace('}', '')
    pares = set()
    
    if entrada:
        # Buscar patrones como (a,b) usando expresiones regulares
        patron_pares = r'\(([^,]+),([^)]+)\)'
        coincidencias = re.findall(patron_pares, entrada)
        
        for par in coincidencias:
            elemento1 = convertir_elemento(par[0])
            elemento2 = convertir_elemento(par[1])
            pares.add((elemento1, elemento2))
    
    return pares


def mostrar_conjunto_formateado(conjunto, nombre=""):
    """
    Muestra un conjunto de forma ordenada y legible.
    
    Args:
        conjunto (set): Conjunto a mostrar
        nombre (str): Nombre del conjunto (opcional)
    """
    if nombre:
        print(f"{nombre}: ", end="")
    
    # Separar números y strings para mejor presentación
    numeros = sorted([x for x in conjunto if isinstance(x, (int, float))])
    strings = sorted([x for x in conjunto if isinstance(x, str)])
    
    elementos_ordenados = numeros + strings
    print("{" + ", ".join(map(str, elementos_ordenados)) + "}")


def mostrar_relacion_formateada(relacion, nombre=""):
    """
    Muestra una relación de forma ordenada y legible.
    
    Args:
        relacion (set): Relación a mostrar
        nombre (str): Nombre de la relación (opcional)
    """
    if nombre:
        print(f"{nombre}: ", end="")
    
    # Convertir a lista y ordenar para presentación consistente
    pares_lista = list(relacion)
    pares_lista.sort(key=lambda x: (str(x[0]), str(x[1])))
    
    pares_str = [f"({par[0]},{par[1]})" for par in pares_lista]
    print("{" + ", ".join(pares_str) + "}")


def solicitar_entrada_usuario(mensaje, validador=None):
    """
    Solicita entrada del usuario con validación opcional.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        validador (function): Función de validación opcional
        
    Returns:
        str: Entrada validada del usuario
    """
    while True:
        entrada = input(mensaje).strip()
        
        if validador is None:
            return entrada
        
        es_valida, mensaje_error = validador(entrada)
        if es_valida:
            return entrada
        else:
            print(f"Error: {mensaje_error}")


def confirmar_accion(mensaje):
    """
    Solicita confirmación del usuario para una acción.
    
    Args:
        mensaje (str): Mensaje de confirmación
        
    Returns:
        bool: True si el usuario confirma, False en caso contrario
    """
    respuesta = input(f"{mensaje} (s/n): ").strip().lower()
    return respuesta in ['s', 'si', 'sí', 'y', 'yes']


def mostrar_separador(caracter="-", longitud=50):
    """Muestra una línea separadora"""
    print(caracter * longitud)
