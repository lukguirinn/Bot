
# Pruebas de integración con WhatsApp

## Proyecto: Calendi

## 1. Objetivo

Registrar las pruebas realizadas durante el desarrollo de la integración entre Calendi y WhatsApp Cloud API.

## 2. Alcance

Se evaluarán:

- Verificación del webhook.
- Recepción de eventos.
- Identificación del remitente.
- Procesamiento de mensajes.
- Envío de plantillas.
- Respuestas automáticas.
- Flujo completo de comunicación.

## 3. Registro de pruebas

### Prueba 1 — Verificación del webhook

Objetivo: comprobar que Meta puede verificar el webhook de Calendi.

Resultado:
- Se implementó el endpoint GET.
- Se realizó la verificación con Meta.
- El webhook fue aceptado.

Estado: Completada.

### Prueba 2 — Recepción de eventos de prueba

Objetivo: comprobar que Flask recibe notificaciones.

Resultado:
- Se envió un evento de prueba desde el panel de Meta.
- Flask recibió la solicitud.
- El servidor respondió HTTP 200.

Estado: Completada.

Observación:

Esta prueba confirma la recepción de un evento de prueba, pero no demuestra todavía que lleguen mensajes reales de WhatsApp.

### Prueba 3 — Procesamiento de mensajes simulados

Objetivo: comprobar la lógica inicial del bot.

Resultado:
- Se probó el reconocimiento de "hola".
- El bot devolvió el resultado "saludo".
- Se probó un mensaje no reconocido.
- El bot devolvió el resultado "desconocido".

Estado: Completada para los casos simulados.

### Prueba 4 — Envío manual de plantilla

Objetivo: comprobar la comunicación saliente con WhatsApp Cloud API.

Resultado:
- Se utilizó la plantilla oficial `hello_world`.
- La API aceptó la solicitud.
- Se recibió una respuesta HTTP 200.
- Se confirmó la entrega del mensaje de prueba.

Estado: Completada.

### Prueba 5 — Recepción de mensajes reales

Objetivo: comprobar que los mensajes enviados desde WhatsApp llegan al webhook.

Resultado:

La recepción de mensajes reales todavía no se encuentra validada.

Estado: Pendiente.

### Prueba 6 — Respuesta automática

Objetivo: comprobar que Calendi responde automáticamente al recibir un mensaje real.

Resultado:

El código inicial contempla una respuesta mediante plantilla para el resultado "saludo".

Sin embargo, el flujo completo todavía no fue validado con un mensaje real recibido desde WhatsApp.

Estado: Pendiente.

### Prueba 7 — Flujo completo

Objetivo: validar toda la comunicación entre el usuario y Calendi.

Procedimiento:

1. El usuario envía un mensaje.
2. Meta notifica al webhook.
3. Flask recibe el evento.
4. Calendi procesa el mensaje.
5. Se genera la respuesta.
6. WhatsApp Cloud API envía la plantilla.
7. El usuario recibe la respuesta.

Estado: Pendiente.

## 4. Resumen de pruebas

| Prueba | Estado |
|---|---|
| Verificación del webhook | Completada |
| Recepción de evento simulado | Completada |
| Procesamiento de mensajes simulados | Completada |
| Envío manual de plantilla | Completada |
| Recepción de mensajes reales | Pendiente |
| Respuesta automática real | Pendiente |
| Flujo completo | Pendiente |

## 5. Registro de errores

Durante las pruebas se deberán documentar:

- Fecha.
- Funcionalidad probada.
- Error detectado.
- Causa identificada.
- Solución aplicada.
- Resultado de la nueva prueba.

## 6. Criterios de aprobación

Una prueba se considera aprobada cuando cumple el resultado esperado y no presenta errores que impidan continuar.

## 7. Criterios de finalización de la Etapa 2

La etapa se considerará completada cuando:

- El webhook esté verificado.
- Calendi reciba mensajes reales.
- Identifique al remitente.
- Procese los mensajes.
- Envíe respuestas mediante plantillas oficiales cuando corresponda.
- El flujo completo esté probado.
- Los resultados estén documentados.

## 8. Estado general

La integración inicial con WhatsApp Cloud API está implementada parcialmente.

Se completaron las pruebas de verificación, recepción de eventos simulados, procesamiento inicial y envío manual de plantillas.

Continúan pendientes las pruebas con mensajes reales y la validación del flujo automático completo.
