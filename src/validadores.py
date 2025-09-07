"""
Validadores para entrada de datos del usuario.
Contiene funciones de validación para diferentes tipos de entrada.
"""

import re


def validar_nombre_conjunto(nombre):
    """
    Valida que el nombre de un conjunto sea válido.
    
    Args:
        nombre (str): Nombre del conjunto
        
    Returns:
        tuple: (es_valido, mensaje_error)
    """
    if not nombre:
        return False, "El nombre no puede estar vacío"
    
    if not nombre.replace('_', '').isalnum():
        return False, "El nombre solo puede contener letras, números y guiones bajos"
    
    if len(nombre) > 20:
        return False, "El nombre no puede tener más de 20 caracteres"
    
    return True, ""


def validar_entrada_conjunto(entrada):
    """
    Valida que la entrada para un conjunto tenga formato correcto.
    
    Args:
        entrada (str): Entrada del usuario para conjunto
        
    Returns:
        tuple: (es_valido, mensaje_error)
    """
    if not entrada.strip():
        return True, ""  # Conjunto vacío es válido
    
    # Remover llaves si las hay
    entrada_limpia = entrada.strip().replace('{', '').replace('}', '')
    
    # Verificar que tenga formato básico de elementos separados por comas
    if entrada_limpia:
        elementos = entrada_limpia.split(',')
        for elemento in elementos:
            if not elemento.strip():
                return False, "Los elementos no pueden estar vacíos"
    
    return True, ""


def validar_entrada_relacion(entrada):
    """
    Valida que la entrada para una relación tenga formato correcto.
    
    Args:
        entrada (str): Entrada del usuario para relación
        
    Returns:
        tuple: (es_valido, mensaje_error)
    """
    if not entrada.strip():
        return True, ""  # Relación vacía es válida
    
    # Verificar que tenga el formato de pares ordenados
    patron_pares = r'\([^,]+,[^)]+\)'
    pares_encontrados = re.findall(patron_pares, entrada)
    
    if not pares_encontrados:
        return False, "Debe contener pares ordenados en formato (a,b)"
    
    # Verificar que no haya caracteres extraños fuera de los pares
    entrada_sin_pares = re.sub(patron_pares, '', entrada)
    entrada_sin_pares = entrada_sin_pares.replace('{', '').replace('}', '').replace(',', '').replace(' ', '')
    
    if entrada_sin_pares:
        return False, "Formato incorrecto. Use: (a,b),(c,d),..."
    
    return True, ""


def validar_numero_entero_positivo(entrada):
    """
    Valida que la entrada sea un número entero positivo.
    
    Args:
        entrada (str): Entrada del usuario
        
    Returns:
        tuple: (es_valido, mensaje_error)
    """
    try:
        numero = int(entrada)
        if numero <= 0:
            return False, "Debe ser un número entero positivo"
        return True, ""
    except ValueError:
        return False, "Debe ser un número entero válido"


def validar_opcion_menu(entrada, opciones_validas):
    """
    Valida que la opción del menú sea válida.
    
    Args:
        entrada (str): Opción seleccionada
        opciones_validas (list): Lista de opciones válidas
        
    Returns:
        tuple: (es_valido, mensaje_error)
    """
    if entrada not in opciones_validas:
        return False, f"Opción no válida. Opciones disponibles: {', '.join(opciones_validas)}"
    
    return True, ""


def es_nombre_protegido(nombre, tipo='conjunto'):
    """
    Verifica si un nombre está protegido contra sobrescritura.
    
    Args:
        nombre (str): Nombre a verificar
        tipo (str): 'conjunto' o 'relacion'
        
    Returns:
        bool: True si el nombre está protegido
    """
    if tipo == 'conjunto':
        nombres_protegidos = ['U', 'A', 'B', 'C']
    else:  # relacion
        nombres_protegidos = ['E', 'R']
    
    return nombre.upper() in nombres_protegidos


def validar_sobrescritura(nombre, operador, tipo='conjunto'):
    """
    Valida si se puede sobrescribir un conjunto o relación.
    
    Args:
        nombre (str): Nombre del conjunto/relación
        operador: Instancia de OperadorConjuntos
        tipo (str): 'conjunto' o 'relacion'
        
    Returns:
        tuple: (puede_sobrescribir, requiere_confirmacion, mensaje)
    """
    nombre = nombre.upper()
    
    # Verificar si es un nombre protegido
    if es_nombre_protegido(nombre, tipo):
        return False, False, f"No se puede sobrescribir {nombre} (es un {tipo} importante del ejemplo)"
    
    # Verificar si ya existe
    if tipo == 'conjunto':
        existe = nombre in operador.conjuntos
    else:
        existe = nombre in operador.relaciones
    
    if existe:
        return True, True, f"El {tipo} '{nombre}' ya existe"
    
    return True, False, ""
