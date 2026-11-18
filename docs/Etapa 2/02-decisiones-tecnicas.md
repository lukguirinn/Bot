
# Decisiones técnicas

## Proyecto: Calendi

## 1. Objetivo

Documentar las decisiones tecnológicas adoptadas para desarrollar Calendi y mantener una arquitectura organizada y consistente.

## 2. Tecnologías seleccionadas

| Componente | Tecnología | Estado |
|---|---|---|
| Plataforma de mensajería | WhatsApp Business Platform | Seleccionada |
| API | WhatsApp Cloud API | Seleccionada |
| Lenguaje | Python | Seleccionado |
| Framework web | Flask | Seleccionado |
| Base de datos | SQLite | Prevista |
| Hosting | Render | Previsto |
| Túnel de desarrollo | Ngrok | Utilizado |
| Control de versiones | Git y GitHub | Utilizados |
| Integración de calendario | Google Calendar API | Próxima etapa |

## 3. WhatsApp Cloud API

Se utilizará la API oficial de Meta para conectar Calendi con WhatsApp.

Motivos:
- Es una integración oficial.
- Permite enviar y recibir mensajes.
- Permite desarrollar una solución propia.
- Evita depender de bibliotecas no oficiales.

El envío de respuestas se realizará mediante plantillas oficiales de WhatsApp cuando corresponda.

## 4. Python

Se utilizará Python como lenguaje principal del proyecto.

Motivos:
- Es el lenguaje utilizado para desarrollar la lógica del bot.
- Permite integrar APIs externas.
- Cuenta con herramientas para automatización y procesamiento de mensajes.

## 5. Flask

Se utilizará Flask para desarrollar el servidor web de Calendi.

Responsabilidades:
- Crear endpoints HTTP.
- Recibir solicitudes de Meta.
- Implementar la verificación del webhook.
- Recibir notificaciones de WhatsApp.
- Conectar el webhook con la lógica del bot.

Motivos:
- Es un framework ligero.
- Permite implementar un servidor web sencillo.
- Es adecuado para el desarrollo inicial del proyecto.

## 6. Organización del código

Se utilizará una estructura modular para separar las responsabilidades.

```text
src/
├── __init__.py
├── main.py
├── webhook.py
├── whatsapp.py
└── bot.py
```

### Responsabilidades

**main.py**
- Punto de entrada de la aplicación.
- Inicia el servidor Flask.

**webhook.py**
- Gestiona la verificación del webhook.
- Recibe los eventos de WhatsApp.
- Deriva los mensajes a la lógica del bot.

**whatsapp.py**
- Contiene las funciones de comunicación con WhatsApp Cloud API.
- Permite enviar plantillas oficiales.

**bot.py**
- Procesa los mensajes recibidos.
- Contiene la lógica inicial de interpretación.

**__init__.py**
- Identifica el directorio src como paquete de Python.

## 7. Configuración y credenciales

Las credenciales se administrarán mediante variables de entorno.

Se utilizará un archivo `.env` ubicado en la raíz del proyecto.

Variables utilizadas:

```env
WHATSAPP_TOKEN=
WHATSAPP_PHONE_NUMBER_ID=
WEBHOOK_VERIFY_TOKEN=
```

Reglas de seguridad:
- No guardar credenciales directamente en el código.
- No publicar `.env` en GitHub.
- Mantener `.env` incluido en `.gitignore`.
- No compartir tokens públicamente.

El archivo `.env.example` podrá utilizarse como plantilla sin credenciales reales.

## 8. Entorno de desarrollo

Se utilizará un entorno virtual de Python para administrar las dependencias.

Estructura local:

```text
Bot/
├── .venv/
├── .env
├── .gitignore
├── requirements.txt
├── verificar.py
├── src/
└── docs/
```

- `.venv/`: entorno virtual local.
- `.env`: configuración privada.
- `requirements.txt`: dependencias del proyecto.
- `verificar.py`: herramienta de diagnóstico.

Los directorios y archivos privados no deben publicarse en GitHub.

## 9. Ngrok

Se utilizará Ngrok durante el desarrollo local para exponer temporalmente el servidor Flask a Internet.

Esto permitirá que Meta pueda comunicarse con el webhook durante las pruebas.

En producción se utilizará un servicio de hosting con HTTPS.

## 10. Base de datos

Se considera SQLite como alternativa inicial para almacenar información del proyecto.

Su implementación queda pendiente para una etapa posterior, cuando se definan las necesidades de almacenamiento de usuarios, eventos y recordatorios.

## 11. Hosting

Se considera Render como alternativa para desplegar Calendi.

Antes de realizar el despliegue se deberán evaluar:
- Configuración del servidor.
- Variables de entorno.
- Disponibilidad de HTTPS.
- Persistencia de datos.
- Costos del servicio.

## 12. Decisiones futuras

Quedan pendientes de definición:
- Implementación de SQLite.
- Integración con Google Calendar API.
- Diseño del sistema de usuarios.
- Administración de eventos y recordatorios.
- Despliegue definitivo.

## 13. Estado

Las decisiones principales de desarrollo están documentadas.

La arquitectura inicial utiliza Python, Flask y WhatsApp Cloud API.

Las tecnologías previstas para etapas posteriores todavía no se consideran implementadas.
