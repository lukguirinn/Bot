
# Etapa 2 — Desarrollo del bot de WhatsApp

## Proyecto: Calendi

## 1. Objetivo

Desarrollar la conexión entre Calendi y WhatsApp mediante la plataforma oficial WhatsApp Cloud API de Meta.

El objetivo es que el bot pueda recibir mensajes, procesarlos y responder mediante plantillas oficiales de WhatsApp.

## 2. Resultado esperado

Al finalizar esta etapa, Calendi deberá poder:

- Recibir mensajes de WhatsApp.
- Identificar al usuario que envía el mensaje.
- Obtener el contenido del mensaje.
- Procesar los mensajes mediante la lógica del bot.
- Generar respuestas.
- Enviar respuestas mediante WhatsApp Cloud API.
- Mantener una conexión funcional con la API oficial de Meta.

## 3. Decisiones técnicas

| Componente | Tecnología |
|---|---|
| Plataforma de mensajería | WhatsApp Business Platform |
| API | WhatsApp Cloud API |
| Proveedor | Meta |
| Lenguaje | Python |
| Framework | Flask |
| Base de datos inicial | SQLite (prevista) |
| Hosting | Render (previsto) |
| Entorno de desarrollo | Local |
| Túnel de desarrollo | Ngrok |
| Control de versiones | Git y GitHub |

## 4. Arquitectura

El funcionamiento general será:

Usuario
  ↓
WhatsApp
  ↓
WhatsApp Cloud API
  ↓
Webhook de Calendi
  ↓
Servidor Flask
  ↓
Lógica del bot
  ↓
WhatsApp Cloud API
  ↓
Usuario

## 5. Tareas de la etapa

### Tarea #15 — Investigación de WhatsApp Business Platform

Objetivo: investigar las alternativas disponibles y seleccionar la tecnología de integración.

Actividades:
- Investigar WhatsApp Cloud API.
- Comprender el funcionamiento de los webhooks.
- Revisar los requisitos de autenticación.
- Analizar las alternativas disponibles.
- Documentar las decisiones técnicas.

Estado: Completada.

### Tarea #16 — Configuración de Meta

Objetivo: configurar los recursos necesarios para conectar Calendi con WhatsApp.

Actividades:
- Configurar Meta for Developers.
- Crear la aplicación.
- Agregar WhatsApp como producto.
- Configurar el número de prueba.
- Obtener las credenciales.
- Guardar las credenciales de manera segura.

Estado: Configuración inicial realizada.

### Tarea #17 — Implementación del webhook

Objetivo: desarrollar el servidor que recibirá las notificaciones de WhatsApp.

Actividades:
- Implementar el servidor Flask.
- Crear el endpoint GET de verificación.
- Crear el endpoint POST de recepción.
- Configurar el webhook en Meta.
- Verificar la conexión.

Estado: Implementado y verificado.

### Tarea #18 — Recepción y procesamiento de mensajes

Objetivo: permitir que Calendi interprete los eventos recibidos.

Actividades:
- Recibir eventos mediante el webhook.
- Identificar al remitente.
- Obtener el contenido del mensaje.
- Ejecutar la lógica inicial del bot.
- Controlar eventos sin mensajes procesables.

Estado: Procesamiento de eventos de prueba realizado. Recepción de mensajes reales pendiente de validación.

### Tarea #19 — Envío de respuestas de prueba

Objetivo: implementar el envío de respuestas desde Calendi hacia WhatsApp.

Actividades:
- Implementar la comunicación con WhatsApp Cloud API.
- Enviar plantillas oficiales.
- Validar las respuestas de la API.
- Comprobar la entrega del mensaje.
- Documentar los resultados.

Estado: Envío manual de plantilla de prueba realizado. Automatización del flujo completo pendiente.

## 6. Estructura actual del código

```text
Bot/
├── .env
├── .venv/
├── verificar.py
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── webhook.py
│   ├── whatsapp.py
│   └── bot.py
├── docs/
│   ├── Etapa 1/
│   └── Etapa 2/
├── requirements.txt
├── .gitignore
└── README.md
```

Los archivos `.env` y `.venv/` son locales y no deben subirse a GitHub.

## 7. Responsabilidades de los archivos

### src/main.py
Punto de entrada de la aplicación. Inicia el servidor Flask.

### src/webhook.py
Gestiona la verificación del webhook y la recepción de eventos de WhatsApp.

### src/whatsapp.py
Contiene las funciones para comunicarse con WhatsApp Cloud API y enviar plantillas oficiales.

### src/bot.py
Contiene la lógica inicial para procesar los mensajes recibidos.

### verificar.py
Permite realizar comprobaciones técnicas del token, los permisos y el número de WhatsApp.

## 8. Seguridad

- No publicar tokens en GitHub.
- Guardar las credenciales en variables de entorno.
- Mantener `.env` fuera del repositorio.
- Utilizar `.gitignore`.
- No incluir credenciales en el código fuente.
- Utilizar HTTPS en el entorno público.
- Evitar almacenar información personal innecesaria.

## 9. Pruebas realizadas

- Verificación del webhook con Meta.
- Recepción de eventos de prueba.
- Respuesta HTTP 200 del servidor Flask.
- Procesamiento de mensajes de prueba.
- Envío manual de la plantilla oficial hello_world.
- Confirmación de entrega de la plantilla de prueba.

## 10. Pruebas pendientes

- Recepción de mensajes reales desde WhatsApp.
- Procesamiento de mensajes reales.
- Automatización de respuestas desde el webhook.
- Validación del flujo completo.
- Manejo de errores y eventos duplicados.

## 11. Criterios de finalización

La Etapa 2 se considerará completada cuando:

- El webhook funcione correctamente.
- Calendi reciba mensajes reales.
- Identifique y procese los mensajes.
- Genere respuestas adecuadas.
- Envíe respuestas mediante plantillas oficiales cuando corresponda.
- El flujo completo esté probado y documentado.

## 12. Próxima etapa

Una vez validada la conexión básica con WhatsApp, avanzaremos hacia la integración con Google Calendar.

El objetivo será permitir que Calendi pueda gestionar eventos, consultar agendas y administrar recordatorios.
