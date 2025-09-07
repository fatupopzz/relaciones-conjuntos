"""
Casos de prueba y ejemplos predefinidos del enunciado.
Ejecuta los ejemplos específicos mencionados en la tarea.
"""

from src.utilidades import mostrar_conjunto_formateado, mostrar_relacion_formateada, mostrar_separador


def ejecutar_ejemplos_predefinidos(operador):
    """Ejecuta todos los ejemplos predefinidos del enunciado original"""
    print("\n" + "=" * 60)
    print("              EJECUTANDO EJEMPLOS PREDEFINIDOS")
    print("=" * 60)
    print("Estos son los ejemplos específicos mencionados en el enunciado:")
    print("- bin(E,C,B)")
    print("- ref(R,A), sim(R,A), tra(R,A)")
    print("- R^3")
    print("- R∘E")
    mostrar_separador()
    
    # Mostrar conjuntos y relaciones iniciales
    mostrar_datos_iniciales(operador)
    
    # Ejecutar cada ejemplo
    ejemplo_bin(operador)
    ejemplo_propiedades_relacion(operador)
    ejemplo_potencia_relacion(operador)
    ejemplo_composicion_relacion(operador)
    
    print("\n" + "=" * 60)
    print("              EJEMPLOS COMPLETADOS")
    print("=" * 60)


def mostrar_datos_iniciales(operador):
    """Muestra los conjuntos y relaciones iniciales del enunciado"""
    print("\n1. CONJUNTOS Y RELACIONES INICIALES (del enunciado):")
    print("-" * 50)
    
    # Mostrar universo
    print("Universo:")
    mostrar_conjunto_formateado(operador.conjuntos['U'], "U")
    
    print("\nConjuntos:")
    mostrar_conjunto_formateado(operador.conjuntos['A'], "A")
    mostrar_conjunto_formateado(operador.conjuntos['B'], "B")
    mostrar_conjunto_formateado(operador.conjuntos['C'], "C")
    
    print("\nRelaciones:")
    mostrar_relacion_formateada(operador.relaciones['E'], "E")
    mostrar_relacion_formateada(operador.relaciones['R'], "R")


def ejemplo_bin(operador):
    """Ejecuta el ejemplo bin(E,C,B)"""
    print("\n\n2. OPERACIÓN bin(E,C,B):")
    print("-" * 50)
    
    # Explicar la operación
    print("La operación bin(E,C,B) calcula: (C × B) ∩ E")
    print("Es decir, el producto cartesiano de C×B intersectado con E")
    
    # Calcular paso a paso
    conjunto_C = operador.conjuntos['C']
    conjunto_B = operador.conjuntos['B']
    relacion_E = operador.relaciones['E']
    
    # Paso 1: Producto cartesiano C × B
    producto_CB = operador.producto_cartesiano(conjunto_C, conjunto_B)
    print(f"\nPaso 1 - Producto cartesiano C × B:")
    mostrar_relacion_formateada(producto_CB)
    
    # Paso 2: Intersección con E
    resultado_bin = operador.operacion_bin(relacion_E, conjunto_C, conjunto_B)
    print(f"\nPaso 2 - (C × B) ∩ E:")
    mostrar_relacion_formateada(resultado_bin)
    
    print(f"\n✓ Resultado final bin(E,C,B) = {resultado_bin}")


def ejemplo_propiedades_relacion(operador):
    """Ejecuta los ejemplos ref(R,A), sim(R,A), tra(R,A)"""
    print("\n\n3. PROPIEDADES DE LA RELACIÓN R EN EL CONJUNTO A:")
    print("-" * 50)
    
    relacion_R = operador.relaciones['R']
    conjunto_A = operador.conjuntos['A']
    
    print("Verificando las propiedades de la relación R:")
    mostrar_relacion_formateada(relacion_R, "R")
    print("En el conjunto:")
    mostrar_conjunto_formateado(conjunto_A, "A")
    
    # Reflexividad
    es_reflexiva = operador.es_reflexiva(relacion_R, conjunto_A)
    print(f"\nref(R,A): ¿Es R reflexiva en A?")
    print(f"Para ser reflexiva, debe contener (a,a) para todo a ∈ A")
    print(f"Verificando: (1,1), (a,a), (b,b) en R...")
    print(f"Resultado: {es_reflexiva}")
    
    # Simetría
    es_simetrica = operador.es_simetrica(relacion_R)
    print(f"\nsim(R,A): ¿Es R simétrica?")
    print(f"Para ser simétrica, si (a,b) ∈ R entonces (b,a) ∈ R")
    print(f"Resultado: {es_simetrica}")
    
    # Transitividad
    es_transitiva = operador.es_transitiva(relacion_R)
    print(f"\ntra(R,A): ¿Es R transitiva?")
    print(f"Para ser transitiva, si (a,b) ∈ R y (b,c) ∈ R entonces (a,c) ∈ R")
    print(f"Resultado: {es_transitiva}")
    
    # Resumen
    print(f"\n✓ Resumen de propiedades de R:")
    print(f"  - Reflexiva en A: {es_reflexiva}")
    print(f"  - Simétrica: {es_simetrica}")
    print(f"  - Transitiva: {es_transitiva}")


def ejemplo_potencia_relacion(operador):
    """Ejecuta el ejemplo R^3"""
    print("\n\n4. POTENCIA DE RELACIÓN R^3:")
    print("-" * 50)
    
    relacion_R = operador.relaciones['R']
    
    print("Calculando la potencia R^3 = R ∘ R ∘ R")
    print("Relación original:")
    mostrar_relacion_formateada(relacion_R, "R")
    
    # Calcular paso a paso
    print(f"\nCalculando paso a paso:")
    
    # R^2 = R ∘ R
    r_cuadrada = operador.potencia_relacion(relacion_R, 2)
    print(f"\nR^2 = R ∘ R:")
    mostrar_relacion_formateada(r_cuadrada)
    
    # R^3 = R^2 ∘ R
    r_cubo = operador.potencia_relacion(relacion_R, 3)
    print(f"\nR^3 = R^2 ∘ R:")
    mostrar_relacion_formateada(r_cubo)
    
    print(f"\n✓ Resultado final R^3 = {r_cubo}")


def ejemplo_composicion_relacion(operador):
    """Ejecuta el ejemplo R∘E"""
    print("\n\n5. COMPOSICIÓN DE RELACIONES R∘E:")
    print("-" * 50)
    
    relacion_R = operador.relaciones['R']
    relacion_E = operador.relaciones['E']
    
    print("Calculando la composición R ∘ E")
    print("Donde (a,c) ∈ R∘E si existe b tal que (a,b) ∈ R y (b,c) ∈ E")
    
    print("\nRelación R:")
    mostrar_relacion_formateada(relacion_R, "R")
    
    print("\nRelación E:")
    mostrar_relacion_formateada(relacion_E, "E")
    
    # Calcular composición
    composicion_RE = operador.composicion_relaciones(relacion_R, relacion_E)
    
    print(f"\nR ∘ E:")
    mostrar_relacion_formateada(composicion_RE)
    
    # Explicar algunos casos específicos
    print(f"\n🔍 Análisis de la composición:")
    print(f"Buscamos pares (a,c) donde existe b tal que (a,b) ∈ R y (b,c) ∈ E")
    
    # Mostrar algunos ejemplos específicos si existen
    if composicion_RE:
        print(f"Por ejemplo:")
        for par in list(composicion_RE)[:3]:  # Mostrar máximo 3 ejemplos
            a, c = par
            # Buscar el elemento intermedio
            for par_r in relacion_R:
                for par_e in relacion_E:
                    if len(par_r) == 2 and len(par_e) == 2:
                        if par_r[0] == a and par_r[1] == par_e[0] and par_e[1] == c:
                            print(f"  - ({a},{c}) está porque ({a},{par_r[1]}) ∈ R y ({par_e[0]},{c}) ∈ E")
                            break
    
    print(f"\n✓ Resultado final R∘E = {composicion_RE}")


def ejecutar_casos_adicionales(operador):
    """Ejecuta algunos casos adicionales para demostrar funcionalidad"""
    print("\n\n6. CASOS ADICIONALES DE DEMOSTRACIÓN:")
    print("-" * 50)
    
    # Ejemplo de operaciones básicas
    conjunto_A = operador.conjuntos['A']
    conjunto_B = operador.conjuntos['B']
    conjunto_C = operador.conjuntos['C']
    
    print("Operaciones básicas de conjuntos:")
    
    # A ∪ B
    union_AB = operador.union_conjuntos(conjunto_A, conjunto_B)
    print(f"A ∪ B = {union_AB}")
    
    # A ∩ C
    interseccion_AC = operador.interseccion_conjuntos(conjunto_A, conjunto_C)
    print(f"A ∩ C = {interseccion_AC}")
    
    # A - B
    diferencia_AB = operador.diferencia_conjuntos(conjunto_A, conjunto_B)
    print(f"A - B = {diferencia_AB}")
    
    # A^c
    complemento_A = operador.complemento_conjunto(conjunto_A)
    print(f"A^c = {complemento_A}")
