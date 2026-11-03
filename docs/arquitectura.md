
# Arquitectura del sistema

## 1. Descripción general

Calendi utilizará una arquitectura modular que permita separar la recepción de mensajes, el procesamiento de solicitudes, la gestión de eventos y las integraciones externas.

## 2. Tecnologías propuestas

| Tecnología | Función |
|---|---|
| Python | Lenguaje principal |
| Flask | Framework web |
| WhatsApp Cloud API | Comunicación con WhatsApp |
| Google Calendar API | Integración con calendarios |
| SQLite | Base de datos inicial |
| GitHub | Control de versiones |
| Render | Despliegue del servicio |

Las tecnologías se consideran propuestas iniciales y podrán modificarse durante el desarrollo.

## 3. Arquitectura general

```text
Usuario
  |
  v
WhatsApp
  |
  v
WhatsApp Cloud API
  |
  v
Webhook de Flask
  |
  v
Procesamiento del mensaje
  |
  v
Servicios de Calendi
  |
  +----> Google Calendar API
  |
  +----> Base de datos
  |
  v
Respuesta del bot
  |
  v
WhatsApp
  |
  v
Usuario
```

## 4. Componentes

### 4.1 WhatsApp Cloud API

Se utilizará para recibir mensajes y enviar respuestas a los usuarios.

### 4.2 Webhook

Será el punto de entrada de los mensajes recibidos.

Se encargará de recibir las solicitudes y derivarlas al sistema de procesamiento.

### 4.3 Procesamiento de mensajes

Interpretará el contenido del mensaje y determinará qué acción debe realizarse.

Ejemplos:

- Crear un evento.
- Consultar la agenda.
- Modificar un evento.
- Eliminar un evento.

### 4.4 Servicios

Contendrán la lógica necesaria para ejecutar las acciones solicitadas.

### 4.5 Google Calendar API

Permitirá administrar eventos en el calendario del usuario.

### 4.6 Base de datos

Almacenará información necesaria para el funcionamiento del sistema, como usuarios, configuraciones y referencias a eventos.

## 5. Flujo de procesamiento

1. El usuario envía un mensaje por WhatsApp.
2. WhatsApp Cloud API entrega el mensaje al webhook.
3. El sistema identifica al usuario.
4. Se procesa la solicitud.
5. Se ejecuta la acción correspondiente.
6. Se obtiene el resultado.
7. Calendi envía una respuesta al usuario.

## 6. Seguridad

- Las credenciales se almacenarán mediante variables de entorno.
- No se publicarán tokens ni contraseñas en GitHub.
- Se validarán las solicitudes recibidas.
- Se protegerá el acceso a los datos de cada usuario.
- Se utilizará OAuth 2.0 para la integración con Google Calendar.

## 7. Consideraciones

La arquitectura inicial se diseñará para un MVP.

A medida que el proyecto crezca, podrán incorporarse nuevas tecnologías y servicios.
