# Tarea 3: Normalización

## Integrantes

- Elías Kably  
- Elie Fayad  
- Lucas García  
- Alonso Zamanillo  
- Tomás Boom  

## Descripción

Esta tarea consiste en la implementación de una **relvar** (relación variable) que permite verificar y analizar formas normales en una base de datos relacional, específicamente **Forma Normal de Boyce-Codd (FNBC)** y **Cuarta Forma Normal (4FN)**.

El objetivo principal es construir una herramienta que, dado un esquema de relación, pueda evaluar sus dependencias funcionales y multivaluadas, y determinar si cumple con las formas normales mencionadas.

## Funcionalidades implementadas

Se desarrollaron los siguientes métodos en Python como parte de la clase `Relvar`:

- `is_trivial` (para **dependencias funcionales**): Verifica si una dependencia funcional es trivial.
- `is_trivial` (para **dependencias multivaluadas**): Verifica si una dependencia multivaluada es trivial.
- `closure`: Calcula el **cierre** de un conjunto de atributos con base en las dependencias funcionales.
- `is_superkey`: Verifica si un conjunto de atributos es una **superclave**.
- `is_key`: Verifica si un conjunto de atributos es una **clave candidata**.
- `is_relvar_in_bcnf`: Determina si la relvar está en **Forma Normal de Boyce-Codd (FNBC)**.
- `is_relvar_in_4nf`: Determina si la relvar está en **Cuarta Forma Normal (4FN)**.

## Requisitos

- Python 3.x
- Librerías estándar (no se requieren paquetes externos)

## Cómo usar

1. Clona este repositorio:
   ```bash
   git clone https://github.com/usuario/repositorio.git](https://github.com/AZama23/BD_Eq2_Tarea3
   cd repositorio


  

