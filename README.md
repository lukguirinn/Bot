
# Calendi

Asistente de calendario mediante WhatsApp.

Calendi es un proyecto de software que busca facilitar la gestión de eventos, agendas y recordatorios utilizando WhatsApp como interfaz principal.

## Objetivo

Permitir que los usuarios administren sus actividades mediante mensajes, sin necesidad de utilizar una aplicación de calendario adicional.

## Funcionalidades previstas

- Crear eventos.
- Consultar eventos.
- Modificar eventos.
- Eliminar eventos.
- Configurar recordatorios.
- Integrar Google Calendar.
- Interpretar solicitudes escritas en lenguaje natural.

## Tecnologías

| Tecnología | Función |
|---|---|
| Python | Lenguaje principal |
| Flask | Servidor web |
| WhatsApp Cloud API | Comunicación con WhatsApp |
| Google Calendar API | Integración de calendarios |
| SQLite | Base de datos prevista |
| Ngrok | Túnel para pruebas locales |
| Git y GitHub | Control de versiones |
| Render | Hosting previsto |

## Estructura del proyecto

```text
Bot/
├── .env                 # Configuración privada local
├── .venv/               # Entorno virtual local
├── .gitignore
├── README.md
├── requirements.txt
├── verificar.py
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── webhook.py
│   ├── whatsapp.py
│   └── bot.py
└── docs/
    ├── Etapa 1/
    └── Etapa 2/
```

Los archivos `.env` y `.venv/` son locales y no deben publicarse en GitHub.

## Documentación

### Etapa 1 — Planificación y configuración

- [Alcance del proyecto](docs/Etapa%201/alcance.md)
- [Arquitectura](docs/Etapa%201/arquitectura.md)
- [Entorno de desarrollo](docs/Etapa%201/entorno.md)
- [Estructura del proyecto](docs/Etapa%201/estructura.md)

### Etapa 2 — Desarrollo del bot de WhatsApp

- [Documentación general](docs/Etapa%202/README.md)
- [Investigación de WhatsApp](docs/Etapa%202/01-investigacion-Wpp.md)
- [Decisiones técnicas](docs/Etapa%202/02-decisiones-tecnicas.md)
- [Configuración de Meta](docs/Etapa%202/03-configuracion-meta.md)
- [Pruebas](docs/Etapa%202/04-pruebas.md)

## Roadmap

1. Planificación y configuración.
2. Desarrollo del bot de WhatsApp.
3. Integración con Google Calendar.
4. Desarrollo de funciones del calendario.
5. Interpretación de mensajes.
6. Pruebas y puesta en marcha.

## Estado actual

Calendi cuenta con una estructura modular en Python, un servidor Flask, una integración inicial con WhatsApp Cloud API y pruebas parciales de comunicación.

La recepción de mensajes reales y la automatización completa de respuestas continúan pendientes de validación.

## Seguridad

- Las credenciales se guardan en `.env`.
- El archivo `.env` no debe subirse a GitHub.
- No se deben publicar tokens ni identificadores privados.
- Las dependencias se administran mediante `requirements.txt`.
