
# Estructura del proyecto

## 1. Objetivo

Definir la organización inicial de archivos y carpetas de Calendi.

## 2. Estructura propuesta

```text
calendi/
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── models/
│   └── utils/
│
├── docs/
│   ├── alcance.md
│   ├── arquitectura.md
│   ├── entorno.md
│   └── estructura.md
│
├── tests/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── main.py
└── README.md
```

## 3. Descripción de carpetas

### app/

Contendrá el código principal del sistema.

### app/routes/

Contendrá las rutas y endpoints del sistema, incluyendo el webhook.

### app/services/

Contendrá la lógica de negocio y los servicios de integración.

### app/models/

Contendrá los modelos de datos.

### app/utils/

Contendrá funciones auxiliares.

### docs/

Contendrá la documentación del proyecto.

### tests/

Contendrá las pruebas del sistema.

## 4. Archivos principales

### main.py

Será el punto de entrada de la aplicación.

### requirements.txt

Contendrá las dependencias necesarias.

### .env.example

Contendrá una plantilla de las variables de entorno requeridas, sin credenciales reales.

### .gitignore

Evitará que archivos innecesarios o sensibles se publiquen en GitHub.

### README.md

Contendrá la descripción general y las instrucciones iniciales del proyecto.

## 5. Organización del código

Se utilizará una arquitectura modular.

Cada componente tendrá una responsabilidad específica para facilitar:

- El mantenimiento.
- Las pruebas.
- La incorporación de funcionalidades.
- La reutilización de código.
- La escalabilidad.

## 6. Evolución

La estructura podrá ampliarse cuando se incorporen nuevas funcionalidades.
