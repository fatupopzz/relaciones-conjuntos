"""
Interfaz de usuario para el programa de conjuntos y relaciones.
Maneja la interacción con el usuario y los menús.
"""

from src.utilidades import (
    crear_conjunto_desde_entrada, crear_relacion_desde_entrada,
    mostrar_conjunto_formateado, mostrar_relacion_formateada,
    solicitar_entrada_usuario, confirmar_accion, mostrar_separador
)
from src.validadores import (
    validar_nombre_conjunto, validar_entrada_conjunto, validar_entrada_relacion,
    validar_numero_entero_positivo, validar_opcion_menu, validar_sobrescritura
)

def mostrar_menu_principal():
    """Muestra el menú principal de opciones"""
    print("\n" + "=" * 50)
    print("           MENÚ DE OPERACIONES")
    print("=" * 50)
    print("1.  Crear nuevo conjunto")
    print("2.  Crear nueva relación")
    print("3.  Ver conjuntos y relaciones actuales")
    print("4.  Unión de conjuntos (A ∪ B)")
    print("5.  Intersección de conjuntos (A ∩ B)")
    print("6.  Diferencia de conjuntos (A - B)")
    print("7.  Complemento de conjunto (A^c)")
    print("8.  Producto cartesiano (A × B)")
    print("9.  Verificar si relación es reflexiva")
    print("10. Verificar si relación es simétrica")
    print("11. Verificar si relación es transitiva")
    print("12. Potencia de relación (R^n)")
    print("13. Composición de relaciones (R₁ ∘ R₂)")
    print("14. Operación bin(E,C,B)")
    print("15. Ejecutar ejemplos predefinidos")
    print("0.  Salir")
    mostrar_separador()


def mostrar_conjuntos_y_relaciones(operador):
    """Muestra todos los conjuntos y relaciones actuales"""
    print("\n" + "=" * 50)
    print("         CONJUNTOS Y RELACIONES ACTUALES")
    print("=" * 50)
    
    print("\nCONJUNTOS:")
    if operador.conjuntos:
        for nombre in sorted(operador.conjuntos.keys()):
            mostrar_conjunto_formateado(operador.conjuntos[nombre], nombre)
    else:
        print("  (No hay conjuntos definidos)")
    
    print("\nRELACIONES:")
    if operador.relaciones:
        for nombre in sorted(operador.relaciones.keys()):
            mostrar_relacion_formateada(operador.relaciones[nombre], nombre)
    else:
        print("  (No hay relaciones definidas)")
    
    mostrar_separador()


def obtener_conjunto_usuario(operador, mensaje):
    """
    Obtiene un conjunto del usuario por nombre o permite crearlo.
    
    Returns:
        tuple: (conjunto, nombre) o (None, None) si se cancela
    """
    print(f"\n{mensaje}")
    if operador.conjuntos:
        print("Conjuntos disponibles:", ", ".join(sorted(operador.conjuntos.keys())))
    
    nombre = input("Nombre del conjunto: ").strip().upper()
    
    if nombre in operador.conjuntos:
        return operador.conjuntos[nombre], nombre
    
    print(f"El conjunto '{nombre}' no existe.")
    if confirmar_accion("¿Deseas crearlo ahora?"):
        conjunto = crear_conjunto_interactivo(operador, nombre)
        if conjunto is not None:
            return conjunto, nombre
    
    return None, None


def obtener_relacion_usuario(operador, mensaje):
    """
    Obtiene una relación del usuario por nombre o permite crearla.
    
    Returns:
        tuple: (relacion, nombre) o (None, None) si se cancela
    """
    print(f"\n{mensaje}")
    if operador.relaciones:
        print("Relaciones disponibles:", ", ".join(sorted(operador.relaciones.keys())))
    
    nombre = input("Nombre de la relación: ").strip().upper()
    
    if nombre in operador.relaciones:
        return operador.relaciones[nombre], nombre
    
    print(f"La relación '{nombre}' no existe.")
    if confirmar_accion("¿Deseas crearla ahora?"):
        relacion = crear_relacion_interactiva(operador, nombre)
        if relacion is not None:
            return relacion, nombre
    
    return None, None


def crear_conjunto_interactivo(operador, nombre=None):
    """Crea un conjunto de forma interactiva"""
    if nombre is None:
        nombre = solicitar_entrada_usuario(
            "Nombre: ",
            validar_nombre_conjunto
        ).upper()
    
    # Verificar sobrescritura
    puede_sobrescribir, requiere_confirmacion, mensaje = validar_sobrescritura(
        nombre, operador, 'conjunto'
    )
    
    if not puede_sobrescribir:
        print(f"Error: {mensaje}")
        return None
    
    if requiere_confirmacion:
        if not confirmar_accion(f"{mensaje}. ¿Sobrescribir?"):
            return None
    
    print("Elementos (ej: a,b,c,1,2):")
    
    entrada = solicitar_entrada_usuario(
        "> ",
        validar_entrada_conjunto
    )
    
    conjunto = crear_conjunto_desde_entrada(entrada)
    operador.agregar_conjunto(nombre, conjunto)
    
    print(f"✓ {nombre} creado:")
    mostrar_conjunto_formateado(conjunto, nombre)
    
    return conjunto


def crear_relacion_interactiva(operador, nombre=None):
    """Crea una relación de forma interactiva"""
    if nombre is None:
        nombre = solicitar_entrada_usuario(
            "Nombre: ",
            validar_nombre_conjunto
        ).upper()
    
    # Verificar sobrescritura
    puede_sobrescribir, requiere_confirmacion, mensaje = validar_sobrescritura(
        nombre, operador, 'relacion'
    )
    
    if not puede_sobrescribir:
        print(f"Error: {mensaje}")
        return None
    
    if requiere_confirmacion:
        if not confirmar_accion(f"{mensaje}. ¿Sobrescribir?"):
            return None
    
    print("Pares (ej: (1,a),(2,b)):")
    
    entrada = solicitar_entrada_usuario(
        "> ",
        validar_entrada_relacion
    )
    
    relacion = crear_relacion_desde_entrada(entrada)
    operador.agregar_relacion(nombre, relacion)
    
    print(f"✓ {nombre} creada:")
    mostrar_relacion_formateada(relacion, nombre)
    
    return relacion


def guardar_resultado_conjunto(operador, resultado, tipo_operacion):
    """Pregunta al usuario si quiere guardar el resultado como un nuevo conjunto"""
    if len(resultado) == 0:
        print("El resultado es un conjunto vacío, no se guardará automáticamente.")
        return
    
    if confirmar_accion(f"¿Deseas guardar este resultado de {tipo_operacion} como un nuevo conjunto?"):
        nombre = solicitar_entrada_usuario(
            "Nombre para el nuevo conjunto: ",
            validar_nombre_conjunto
        ).upper()
        
        puede_sobrescribir, requiere_confirmacion, mensaje = validar_sobrescritura(
            nombre, operador, 'conjunto'
        )
        
        if not puede_sobrescribir:
            print(f"Error: {mensaje}")
            return
        
        if requiere_confirmacion:
            if not confirmar_accion(f"{mensaje}. ¿Sobrescribir?"):
                return
        
        operador.agregar_conjunto(nombre, resultado)
        print(f"✓ Conjunto '{nombre}' guardado exitosamente")


def guardar_resultado_relacion(operador, resultado, tipo_operacion):
    """Pregunta al usuario si quiere guardar el resultado como una nueva relación"""
    if len(resultado) == 0:
        print("El resultado es una relación vacía, no se guardará automáticamente.")
        return
    
    if confirmar_accion(f"¿Deseas guardar este resultado de {tipo_operacion} como una nueva relación?"):
        nombre = solicitar_entrada_usuario(
            "Nombre para la nueva relación: ",
            validar_nombre_conjunto
        ).upper()
        
        puede_sobrescribir, requiere_confirmacion, mensaje = validar_sobrescritura(
            nombre, operador, 'relacion'
        )
        
        if not puede_sobrescribir:
            print(f"Error: {mensaje}")
            return
        
        if requiere_confirmacion:
            if not confirmar_accion(f"{mensaje}. ¿Sobrescribir?"):
                return
        
        operador.agregar_relacion(nombre, resultado)
        print(f"✓ Relación '{nombre}' guardada exitosamente")


def ejecutar_operacion_conjuntos(operador, tipo_operacion):
    """Ejecuta operaciones que requieren dos conjuntos"""
    conjunto1, nombre1 = obtener_conjunto_usuario(operador, "Selecciona el primer conjunto:")
    if conjunto1 is None:
        return
    
    conjunto2, nombre2 = obtener_conjunto_usuario(operador, "Selecciona el segundo conjunto:")
    if conjunto2 is None:
        return
    
    if tipo_operacion == "union":
        resultado = operador.union_conjuntos(conjunto1, conjunto2)
        simbolo = "∪"
    elif tipo_operacion == "interseccion":
        resultado = operador.interseccion_conjuntos(conjunto1, conjunto2)
        simbolo = "∩"
    elif tipo_operacion == "diferencia":
        resultado = operador.diferencia_conjuntos(conjunto1, conjunto2)
        simbolo = "-"
    elif tipo_operacion == "producto":
        resultado = operador.producto_cartesiano(conjunto1, conjunto2)
        simbolo = "×"
    
    print(f"\nResultado: {nombre1} {simbolo} {nombre2} =")
    if tipo_operacion == "producto":
        mostrar_relacion_formateada(resultado)
        guardar_resultado_relacion(operador, resultado, f"{tipo_operacion} cartesiano")
    else:
        mostrar_conjunto_formateado(resultado)
        guardar_resultado_conjunto(operador, resultado, tipo_operacion)


def ejecutar_verificacion_propiedades(operador, tipo_propiedad):
    """Ejecuta verificaciones de propiedades de relaciones"""
    relacion, nombre_rel = obtener_relacion_usuario(operador, "Selecciona la relación:")
    if relacion is None:
        return
    
    if tipo_propiedad == "reflexiva":
        conjunto, nombre_conj = obtener_conjunto_usuario(operador, "Selecciona el conjunto para verificar reflexividad:")
        if conjunto is None:
            return
        resultado = operador.es_reflexiva(relacion, conjunto)
        print(f"\n¿Es la relación {nombre_rel} reflexiva en el conjunto {nombre_conj}? {resultado}")
    
    elif tipo_propiedad == "simetrica":
        resultado = operador.es_simetrica(relacion)
        print(f"\n¿Es la relación {nombre_rel} simétrica? {resultado}")
    
    elif tipo_propiedad == "transitiva":
        resultado = operador.es_transitiva(relacion)
        print(f"\n¿Es la relación {nombre_rel} transitiva? {resultado}")


def ejecutar_menu_principal(operador):
    """Ejecuta el bucle principal del menú"""
    opciones_validas = [str(i) for i in range(16)]
    
    while True:
        mostrar_menu_principal()
        
        opcion = solicitar_entrada_usuario(
            "Selecciona una opción: ",
            lambda x: validar_opcion_menu(x, opciones_validas)
        )
        
        if opcion == '0':
            print("\n¡Gracias por usar el programa!")
            print("¡Hasta luego! 👋")
            break
        
        elif opcion == '1':
            crear_conjunto_interactivo(operador)
        
        elif opcion == '2':
            crear_relacion_interactiva(operador)
        
        elif opcion == '3':
            mostrar_conjuntos_y_relaciones(operador)
        
        elif opcion == '4':
            ejecutar_operacion_conjuntos(operador, "union")
        
        elif opcion == '5':
            ejecutar_operacion_conjuntos(operador, "interseccion")
        
        elif opcion == '6':
            ejecutar_operacion_conjuntos(operador, "diferencia")
        
        elif opcion == '7':
            conjunto, nombre = obtener_conjunto_usuario(operador, "Selecciona el conjunto para calcular su complemento:")
            if conjunto is not None:
                resultado = operador.complemento_conjunto(conjunto)
                print(f"\nComplemento de {nombre}:")
                mostrar_conjunto_formateado(resultado)
                guardar_resultado_conjunto(operador, resultado, "complemento")
        
        elif opcion == '8':
            ejecutar_operacion_conjuntos(operador, "producto")
        
        elif opcion == '9':
            ejecutar_verificacion_propiedades(operador, "reflexiva")
        
        elif opcion == '10':
            ejecutar_verificacion_propiedades(operador, "simetrica")
        
        elif opcion == '11':
            ejecutar_verificacion_propiedades(operador, "transitiva")
        
        elif opcion == '12':
            relacion, nombre = obtener_relacion_usuario(operador, "Selecciona la relación:")
            if relacion is not None:
                n_str = solicitar_entrada_usuario(
                    "Ingresa la potencia (número entero positivo): ",
                    validar_numero_entero_positivo
                )
                n = int(n_str)
                resultado = operador.potencia_relacion(relacion, n)
                print(f"\n{nombre}^{n} =")
                mostrar_relacion_formateada(resultado)
                guardar_resultado_relacion(operador, resultado, f"potencia {n}")
        
        elif opcion == '13':
            relacion1, nombre1 = obtener_relacion_usuario(operador, "Selecciona la primera relación:")
            if relacion1 is None:
                continue
            
            relacion2, nombre2 = obtener_relacion_usuario(operador, "Selecciona la segunda relación:")
            if relacion2 is None:
                continue
            
            resultado = operador.composicion_relaciones(relacion1, relacion2)
            print(f"\nComposición {nombre1} ∘ {nombre2} =")
            mostrar_relacion_formateada(resultado)
            guardar_resultado_relacion(operador, resultado, "composición")
        
        elif opcion == '14':
            relacion_E, nombre_E = obtener_relacion_usuario(operador, "Selecciona la relación E:")
            if relacion_E is None:
                continue
            
            conjunto_C, nombre_C = obtener_conjunto_usuario(operador, "Selecciona el conjunto C:")
            if conjunto_C is None:
                continue
            
            conjunto_B, nombre_B = obtener_conjunto_usuario(operador, "Selecciona el conjunto B:")
            if conjunto_B is None:
                continue
            
            resultado = operador.operacion_bin(relacion_E, conjunto_C, conjunto_B)
            print(f"\nbin({nombre_E},{nombre_C},{nombre_B}) = ({nombre_C} × {nombre_B}) ∩ {nombre_E} =")
            mostrar_relacion_formateada(resultado)
            guardar_resultado_relacion(operador, resultado, "operación bin")
        
        elif opcion == '15':
            ejecutar_ejemplos_predefinidos(operador)
        
        # Pausa para que el usuario pueda leer el resultado
        if opcion != '0':
            input("\nPresiona Enter para continuar...")
