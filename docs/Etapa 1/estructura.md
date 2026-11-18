
# Estructura del proyecto

## 1. Objetivo

Documentar la organización actual de archivos y carpetas de Calendi.

## 2. Estructura del proyecto

```text
Bot/
│
├── .venv/                  # Entorno virtual local
├── .env                    # Variables privadas locales
├── .gitignore
├── README.md
├── requirements.txt
├── verificar.py
│
├── main.py                 # Archivo histórico
├── webhook.py              # Archivo histórico
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── webhook.py
│   ├── whatsapp.py
│   └── bot.py
│
└── docs/
    ├── Etapa 1/
    │   ├── alcance.md
    │   ├── arquitectura.md
    │   ├── entorno.md
    │   └── estructura.md
    │
    └── Etapa 2/
        ├── README.md
        ├── 01-investigacion-Wpp.md
        ├── 02-decisiones-tecnicas.md
        ├── 03-configuracion-meta.md
        └── 04-pruebas.md
```

La carpeta `.venv/` y el archivo `.env` son locales y no deben subirse al repositorio.

## 3. Descripción de carpetas

### src/

Contiene el código principal de Calendi.

### src/main.py

Punto de entrada del servidor Flask.

### src/webhook.py

Gestiona la verificación y recepción de eventos de WhatsApp.

### src/whatsapp.py

Contiene las funciones de comunicación con WhatsApp Cloud API.

### src/bot.py

Contiene la lógica inicial de procesamiento de mensajes.

### docs/

Contiene la documentación técnica y funcional del proyecto.

### .venv/

Contiene el entorno virtual de Python.

### .env

Contiene las credenciales y variables privadas.

### verificar.py

Permite ejecutar comprobaciones técnicas de las credenciales de WhatsApp.

## 4. Archivos históricos

Se mantienen temporalmente en la raíz:

- `main.py`
- `webhook.py`

Estos archivos corresponden a pruebas y versiones anteriores.

No deben utilizarse como punto de entrada del sistema modular.

Se conservarán hasta validar completamente la estructura de `src/`.

## 5. Archivos de configuración

### requirements.txt

Contiene las dependencias necesarias para ejecutar el proyecto.

### .gitignore

Evita publicar archivos privados y temporales.

### README.md

Presenta el proyecto y enlaza la documentación.

## 6. Evolución de la estructura

La estructura podrá ampliarse cuando se incorporen:

- Servicios de calendario.
- Integración con Google Calendar.
- Base de datos.
- Sistema de usuarios.
- Pruebas automatizadas.
