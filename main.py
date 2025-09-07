
"""
Programa de Operaciones con Conjuntos y Relaciones
Autor: [Tu Nombre]
Fecha: Septiembre 2025

Punto de entrada principal del programa.
"""

from src.conjuntos import OperadorConjuntos
from src.interfaz import ejecutar_menu_principal


def main():
    """Función principal del programa"""
    print("=" * 60)
    print("    PROGRAMA DE OPERACIONES CON CONJUNTOS Y RELACIONES")
    print("=" * 60)
    print("Desarrollado como proyecto de clase sobre relaciones matemáticas")
    print("Permite crear conjuntos, relaciones y realizar operaciones entre ellos")
    print()
    
    # Crear instancia del operador
    operador = OperadorConjuntos()
    
    # Ejecutar menú principal
    ejecutar_menu_principal(operador)


if __name__ == "__main__":
    main()
