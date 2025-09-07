"""
Módulo principal para operaciones con conjuntos y relaciones.
Contiene la clase OperadorConjuntos con todas las operaciones matemáticas.
"""


class OperadorConjuntos:
    """Clase para manejar operaciones con conjuntos y relaciones"""
    
    def __init__(self):
        """Inicializa el operador con conjuntos y relaciones vacíos"""
        self.conjuntos = {}
        self.relaciones = {}
        self.cargar_ejemplos_iniciales()
    
    def cargar_ejemplos_iniciales(self):
        """Carga los conjuntos y relaciones de ejemplo del enunciado"""
        self.conjuntos['U'] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 1, 2, 3, 4, 5}
        self.conjuntos['A'] = {1, 'a', 'b'}
        self.conjuntos['C'] = {1, 2, 3}
        self.conjuntos['B'] = {'a', 'b', 'c'}
        
        self.relaciones['E'] = {(1, 'a'), (2, 'b'), (3, 'c')}
        self.relaciones['R'] = {(1, 1), ('a', 'a'), ('b', 'b'), (1, 'a'), ('a', 1), 
                               ('a', 'b'), ('b', 'a'), (1, 'b'), ('b', 1)}
    
    def agregar_conjunto(self, nombre, conjunto):
        """Agrega un nuevo conjunto al diccionario"""
        self.conjuntos[nombre] = conjunto
    
    def agregar_relacion(self, nombre, relacion):
        """Agrega una nueva relación al diccionario"""
        self.relaciones[nombre] = relacion
    
    def obtener_conjunto(self, nombre):
        """Obtiene un conjunto por nombre"""
        return self.conjuntos.get(nombre)
    
    def obtener_relacion(self, nombre):
        """Obtiene una relación por nombre"""
        return self.relaciones.get(nombre)
    
    def listar_conjuntos(self):
        """Retorna una lista de nombres de conjuntos disponibles"""
        return list(self.conjuntos.keys())
    
    def listar_relaciones(self):
        """Retorna una lista de nombres de relaciones disponibles"""
        return list(self.relaciones.keys())
    
    # === OPERACIONES BÁSICAS DE CONJUNTOS ===
    
    def union_conjuntos(self, conjunto1, conjunto2):
        """Calcula la unión de dos conjuntos (A ∪ B)"""
        return conjunto1.union(conjunto2)
    
    def interseccion_conjuntos(self, conjunto1, conjunto2):
        """Calcula la intersección de dos conjuntos (A ∩ B)"""
        return conjunto1.intersection(conjunto2)
    
    def diferencia_conjuntos(self, conjunto1, conjunto2):
        """Calcula la diferencia entre dos conjuntos (A - B)"""
        return conjunto1.difference(conjunto2)
    
    def complemento_conjunto(self, conjunto, universo=None):
        """Calcula el complemento de un conjunto respecto al universo (A^c)"""
        if universo is None:
            universo = self.conjuntos.get('U', set())
        return universo.difference(conjunto)
    
    def producto_cartesiano(self, conjunto1, conjunto2):
        """Calcula el producto cartesiano de dos conjuntos (A × B)"""
        producto = set()
        for elemento1 in conjunto1:
            for elemento2 in conjunto2:
                producto.add((elemento1, elemento2))
        return producto
    
    # === PROPIEDADES DE RELACIONES ===
    
    def es_reflexiva(self, relacion, conjunto):
        """
        Verifica si una relación es reflexiva en un conjunto dado.
        Una relación R es reflexiva si para todo a ∈ A, (a,a) ∈ R
        """
        for elemento in conjunto:
            if (elemento, elemento) not in relacion:
                return False
        return True
    
    def es_simetrica(self, relacion):
        """
        Verifica si una relación es simétrica.
        Una relación R es simétrica si para todo (a,b) ∈ R, entonces (b,a) ∈ R
        """
        for par in relacion:
            if len(par) == 2:  # Verificar que sea un par ordenado
                elemento1, elemento2 = par
                if (elemento2, elemento1) not in relacion:
                    return False
        return True
    
    def es_transitiva(self, relacion):
        """
        Verifica si una relación es transitiva.
        Una relación R es transitiva si para todo (a,b) ∈ R y (b,c) ∈ R, entonces (a,c) ∈ R
        """
        for par1 in relacion:
            for par2 in relacion:
                if len(par1) == 2 and len(par2) == 2:
                    # Si el segundo elemento de par1 es igual al primer elemento de par2
                    if par1[1] == par2[0]:
                        # Entonces debe existir el par (par1[0], par2[1])
                        if (par1[0], par2[1]) not in relacion:
                            return False
        return True
    
    # === OPERACIONES AVANZADAS DE RELACIONES ===
    
    def potencia_relacion(self, relacion, n):
        """
        Calcula la potencia n de una relación (R^n).
        R^n = R ∘ R ∘ ... ∘ R (n veces)
        """
        if n == 1:
            return relacion.copy()
        
        resultado = relacion.copy()
        for _ in range(n - 1):
            resultado = self.composicion_relaciones(resultado, relacion)
        return resultado
    
    def composicion_relaciones(self, relacion1, relacion2):
        """
        Calcula la composición de dos relaciones (R₁ ∘ R₂).
        (a,c) ∈ R₁ ∘ R₂ si existe b tal que (a,b) ∈ R₁ y (b,c) ∈ R₂
        """
        composicion = set()
        for par1 in relacion1:
            for par2 in relacion2:
                if len(par1) == 2 and len(par2) == 2:
                    # Si el segundo elemento de par1 es igual al primer elemento de par2
                    if par1[1] == par2[0]:
                        composicion.add((par1[0], par2[1]))
        return composicion
    
    # === OPERACIONES ESPECIALES ===
    
    def operacion_bin(self, relacion_E, conjunto_C, conjunto_B):
        """
        Operación bin(E,C,B): calcula (C × B) ∩ E
        Producto cartesiano de C×B intersectado con la relación E
        """
        producto_CB = self.producto_cartesiano(conjunto_C, conjunto_B)
        return producto_CB.intersection(relacion_E)
