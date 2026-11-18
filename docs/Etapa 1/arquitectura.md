

# Arquitectura del sistema

## 1. Descripción general

Calendi utilizará una arquitectura modular que permita separar la recepción de mensajes, el procesamiento de solicitudes, la gestión de eventos y las integraciones externas.

La arquitectura se desarrollará progresivamente durante las distintas etapas del proyecto.

## 2. Tecnologías

| Tecnología | Función | Estado |
|---|---|---|
| Python | Lenguaje principal | En uso |
| Flask | Framework web | Implementado |
| WhatsApp Cloud API | Comunicación con WhatsApp | Integración inicial |
| Google Calendar API | Gestión de calendarios | Pendiente |
| SQLite | Base de datos | Prevista |
| GitHub | Control de versiones | En uso |
| Ngrok | Exposición del servidor local | Utilizado en pruebas |
| Render | Despliegue | Previsto |

## 3. Arquitectura general

```text
Usuario
   |
 WhatsApp
   |
WhatsApp Cloud API
   |
 Webhook Flask
   |
 Procesamiento del mensaje
   |
 Lógica de Calendi
   |
 Servicios de calendario
   |
 Google Calendar API
   |
 Respuesta de Calendi
   |
 WhatsApp
   |
 Usuario
```

## 4. Componentes

### 4.1 WhatsApp Cloud API

Permite la comunicación entre Calendi y WhatsApp.

### 4.2 Webhook

Es el punto de entrada de las notificaciones enviadas por Meta.

Se implementa mediante Flask y permite verificar la conexión y recibir eventos.

### 4.3 Procesamiento de mensajes

Analiza los mensajes recibidos y determina qué acción debe realizarse.

Actualmente existe una lógica inicial de identificación de mensajes.

### 4.4 Servicios de calendario

Se desarrollarán para administrar eventos, consultas y recordatorios.

### 4.5 Google Calendar API

Permitirá crear, consultar, modificar y eliminar eventos en el calendario del usuario.

Su integración queda pendiente.

### 4.6 Base de datos

Se evaluará SQLite para almacenar información de usuarios, configuraciones y referencias a eventos.

Su implementación queda pendiente.

## 5. Estructura modular actual

```text
src/
├── __init__.py
├── main.py
├── webhook.py
├── whatsapp.py
└── bot.py
```

Responsabilidades:

- `main.py`: inicia el servidor Flask.
- `webhook.py`: recibe y gestiona eventos de WhatsApp.
- `whatsapp.py`: contiene las funciones de comunicación con la API.
- `bot.py`: procesa los mensajes recibidos.
- `__init__.py`: identifica el paquete de Python.

## 6. Seguridad

- Utilizar variables de entorno.
- Mantener las credenciales fuera de GitHub.
- Validar las solicitudes recibidas.
- Proteger los datos de los usuarios.
- Utilizar HTTPS en producción.
- Utilizar OAuth 2.0 para Google Calendar.

## 7. Evolución

La arquitectura inicial corresponde al MVP.

Se ampliará cuando se incorporen la integración con Google Calendar, el almacenamiento de datos, la gestión de usuarios y el sistema de recordatorios.

