# Programa de Operaciones con Conjuntos y Relaciones

Un programa interactivo en Python para realizar operaciones matemáticas con conjuntos y relaciones, desarrollado como proyecto de clase sobre relaciones matemáticas.

## 📋 Características

- **Operaciones de conjuntos**: Unión, intersección, diferencia, complemento, producto cartesiano
- **Propiedades de relaciones**: Verificación de reflexividad, simetría y transitividad
- **Operaciones avanzadas**: Potencia de relaciones, composición de relaciones
- **Interfaz interactiva**: Menús amigables con validación de entrada
- **Gestión dinámica**: Crear, guardar y reutilizar conjuntos y relaciones
- **Ejemplos predefinidos**: Casos específicos del enunciado de la tarea

## 🚀 Instalación y Uso

### Prerrequisitos
- Python 3.7 o superior

### Instalación
```bash
# Clonar el repositorio
git clone [URL_DEL_REPOSITORIO]
cd relaciones-conjuntos

# Ejecutar el programa
python main.py
```

### Uso Básico
1. Ejecuta `python main.py`
2. Selecciona una opción del menú principal
3. Sigue las instrucciones interactivas
4. Los resultados pueden guardarse como nuevos conjuntos/relaciones

## 📁 Estructura del Proyecto

```
relaciones-conjuntos/
│
├── src/                      # Código fuente principal
│   ├── conjuntos.py         # Lógica de operaciones matemáticas
│   ├── interfaz.py          # Interfaz de usuario y menús
│   ├── utilidades.py        # Funciones auxiliares
│   └── validadores.py       # Validación de entrada
│
├── ejemplos/                 # Casos de prueba y ejemplos
│   └── casos_prueba.py      # Ejemplos predefinidos del enunciado
│
├── docs/                     # Documentación
│   ├── especificacion.tex   # Documento LaTeX
│   └── capturas/            # Screenshots de ejecuciones
│
├── main.py                  # Punto de entrada
└── README.md               # Este archivo
```

## 🔧 Ejemplos de Uso

### Operaciones Básicas
```python
# Ejemplo de conjuntos
A = {1, 'a', 'b'}
B = {'a', 'b', 'c'}

# Unión: A ∪ B = {1, 'a', 'b', 'c'}
# Intersección: A ∩ B = {'a', 'b'}
# Diferencia: A - B = {1}
```

### Relaciones
```python
# Ejemplo de relación
R = {(1,1), ('a','a'), ('b','b'), (1,'a'), ('a',1), ('a','b'), ('b','a'), (1,'b'), ('b',1)}

# Verificar propiedades:
# - ¿Es reflexiva en A? True
# - ¿Es simétrica? True  
# - ¿Es transitiva? True
```

## 📊 Ejemplos Predefinidos

El programa incluye los siguientes ejemplos del enunciado:

**Conjuntos:**
- U = {a,b,c,d,e,f,g,h,i,j,k,1,2,3,4,5}
- A = {1,a,b}
- B = {a,b,c}
- C = {1,2,3}

**Relaciones:**
- E = {(1,a),(2,b),(3,c)}
- R = {(1,1),(a,a),(b,b),(1,a),(a,1),(a,b),(b,a),(1,b),(b,1)}

**Operaciones de ejemplo:**
- bin(E,C,B)
- ref(R,A), sim(R,A), tra(R,A)
- R^3
- R∘E

## 🎯 Funcionalidades Principales

### 1. Gestión de Conjuntos
- Crear conjuntos desde entrada de usuario
- Operaciones: ∪, ∩, -, ^c, ×
- Guardar resultados para uso posterior

### 2. Gestión de Relaciones  
- Crear relaciones como conjuntos de pares ordenados
- Verificar propiedades matemáticas
- Operaciones: composición, potencia

### 3. Interfaz Interactiva
- Menús numerados claros
- Validación robusta de entrada
- Confirmación de sobrescritura
- Visualización formateada de resultados


## 🤝 Contribución

Este es un proyecto académico. Las mejoras son bienvenidas siguiendo las buenas prácticas de código limpio.

## 📄 Licencia

Proyecto académico - Ver archivo de licencia para detalles.

---
*Desarrollado como proyecto de clase sobre relaciones matemáticas*
