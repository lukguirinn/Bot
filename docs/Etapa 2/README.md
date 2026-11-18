# Etapa 2 — Bot de WhatsApp

## Proyecto: Calendi

## 1. Objetivo

Desarrollar la conexión entre Calendi y WhatsApp para que el bot pueda recibir mensajes, procesarlos y responder automáticamente.

En esta etapa se implementará la comunicación básica entre WhatsApp y nuestro programa en Python.

## 2. Resultado esperado

Al finalizar la etapa, Calendi deberá poder:

- Recibir mensajes de WhatsApp.
- Procesar mensajes entrantes.
- Identificar al usuario que envió el mensaje.
- Generar una respuesta.
- Enviar la respuesta por WhatsApp.
- Mantener una conexión funcional con la API oficial de Meta.

## 3. Decisiones técnicas

| Componente | Tecnología elegida |
|---|---|
| Plataforma de mensajería | WhatsApp Cloud API |
| Proveedor | Meta |
| Lenguaje | Python |
| Framework | FastAPI |
| Base de datos inicial | SQLite |
| Hosting previsto | Render |
| Entorno de desarrollo | Local |
| Control de versiones | Git y GitHub |

## 4. Arquitectura

El funcionamiento será el siguiente:

Usuario
  ↓
WhatsApp
  ↓
WhatsApp Cloud API
  ↓
Webhook de Calendi
  ↓
Servidor FastAPI
  ↓
Lógica del bot
  ↓
Generación de respuesta
  ↓
WhatsApp Cloud API
  ↓
Usuario

## 5. Tareas de la etapa

### Tarea #15 — Investigar WhatsApp Business Platform

Objetivo: investigar la plataforma oficial de Meta y definir cómo conectaremos Calendi.

Actividades:
- Investigar WhatsApp Cloud API.
- Identificar los recursos necesarios.
- Comprender los webhooks.
- Revisar los requisitos de autenticación.
- Investigar los costos y limitaciones.

Resultado: investigación y decisiones técnicas documentadas.

### Tarea #16 — Configurar cuenta y número

Objetivo: crear y configurar los recursos de Meta necesarios para Calendi.

Actividades:
- Crear o configurar la cuenta de Meta Developers.
- Crear la aplicación de Meta.
- Agregar WhatsApp como producto.
- Configurar el número de prueba.
- Obtener las credenciales necesarias.
- Guardar las credenciales de manera segura.

Resultado: cuenta y número preparados para las pruebas.

### Tarea #17 — Configurar webhook

Objetivo: crear el endpoint que recibirá las notificaciones de WhatsApp.

Actividades:
- Crear el proyecto de FastAPI.
- Implementar el endpoint de verificación.
- Implementar el endpoint de recepción.
- Configurar la URL del webhook en Meta.
- Validar la conexión.

Resultado: webhook configurado y verificado.

### Tarea #18 — Recibir mensajes entrantes

Objetivo: permitir que Calendi reciba mensajes enviados por los usuarios.

Actividades:
- Interpretar los eventos recibidos.
- Identificar el remitente.
- Obtener el contenido del mensaje.
- Procesar el mensaje recibido.
- Controlar errores y eventos duplicados.

Resultado: Calendi recibe y procesa mensajes correctamente.

### Tarea #19 — Enviar respuestas de prueba

Objetivo: implementar el envío de mensajes desde Calendi hacia WhatsApp.

Actividades:
- Implementar la comunicación con la API.
- Enviar una respuesta de prueba.
- Validar la respuesta de la API.
- Probar el flujo completo.
- Documentar los resultados.

Resultado: Calendi recibe un mensaje y responde correctamente.

## 6. Estructura inicial del código

```text
src/
├── main.py
├── config.py
├── webhook.py
├── whatsapp.py
└── bot.py
```

### Responsabilidades

- main.py: iniciar el servidor FastAPI.
- config.py: administrar la configuración.
- webhook.py: recibir los eventos de WhatsApp.
- whatsapp.py: comunicarse con WhatsApp Cloud API.
- bot.py: procesar mensajes y generar respuestas.

## 7. Seguridad

- No publicar tokens en GitHub.
- Utilizar variables de entorno.
- No incluir credenciales en el código fuente.
- Validar las solicitudes recibidas.
- Utilizar HTTPS en el entorno público.
- No guardar información personal innecesaria.

## 8. Pruebas

Se realizarán las siguientes pruebas:

1. Verificar el webhook.
2. Recibir un mensaje.
3. Identificar el remitente.
4. Procesar el contenido.
5. Enviar una respuesta.
6. Verificar que la respuesta llegue correctamente.
7. Comprobar el manejo de errores.

## 9. Criterios de finalización

La etapa se considera completada cuando:

- La cuenta de Meta está configurada.
- El webhook está verificado.
- Calendi recibe mensajes.
- Calendi procesa los mensajes.
- Calendi envía respuestas.
- Las pruebas están documentadas.

## 10. Próxima etapa

Una vez completada la conexión básica, se podrá avanzar hacia la integración de las funciones de calendario, creación de eventos, consulta de agenda y recordatorios.
