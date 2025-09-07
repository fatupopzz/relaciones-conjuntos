#!/usr/bin/env python3
"""
Programa de Operaciones con Conjuntos y Relaciones
Proyecto de clase sobre relaciones matemáticas
"""

from src.conjuntos import OperadorConjuntos
from src.interfaz import ejecutar_menu_principal


def main():
    """Función principal del programa"""
    print("=" * 50)
    print("  OPERACIONES CON CONJUNTOS Y RELACIONES")
    print("=" * 50)
    
    operador = OperadorConjuntos()
    ejecutar_menu_principal(operador)


if __name__ == "__main__":
    main()
