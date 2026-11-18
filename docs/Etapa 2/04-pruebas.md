# Pruebas de integración con WhatsApp

## Proyecto: Calendi

## 1. Objetivo

Registrar las pruebas realizadas durante la Etapa 2 para verificar que Calendi pueda comunicarse correctamente con WhatsApp.

## 2. Alcance

Se probarán:
- Configuración de Meta.
- Verificación del webhook.
- Recepción de mensajes.
- Procesamiento de mensajes.
- Envío de respuestas.
- Manejo de errores.

## 3. Pruebas planificadas

### Prueba 1 — Verificación del webhook

Objetivo: comprobar que Meta puede verificar el webhook de Calendi.

Resultado esperado:
- El servidor responde correctamente a la solicitud de verificación.
- Meta acepta la URL configurada.

Estado: Pendiente.

### Prueba 2 — Recepción de mensaje

Objetivo: comprobar que Calendi recibe un mensaje enviado por WhatsApp.

Resultado esperado:
- El webhook recibe el evento.
- Se identifica el remitente.
- Se obtiene el contenido del mensaje.

Estado: Pendiente.

### Prueba 3 — Procesamiento del mensaje

Objetivo: comprobar que el servidor procesa el mensaje recibido.

Resultado esperado:
- El mensaje se interpreta correctamente.
- Se ejecuta la lógica correspondiente.
- Se genera una respuesta.

Estado: Pendiente.

### Prueba 4 — Envío de respuesta

Objetivo: comprobar que Calendi puede enviar una respuesta a WhatsApp.

Resultado esperado:
- La API acepta la solicitud.
- El mensaje se entrega al destinatario de prueba.

Estado: Pendiente.

### Prueba 5 — Flujo completo

Objetivo: verificar la comunicación completa entre el usuario y Calendi.

Procedimiento:
1. Enviar un mensaje desde WhatsApp.
2. Verificar que Calendi lo recibe.
3. Verificar que Calendi lo procesa.
4. Verificar que Calendi envía una respuesta.
5. Confirmar que la respuesta llega a WhatsApp.

Resultado esperado:
- El flujo completo funciona correctamente.

Estado: Pendiente.

## 4. Registro de resultados

| Prueba | Resultado | Observaciones |
|---|---|---|
| Verificación webhook | Pendiente | |
| Recepción de mensaje | Pendiente | |
| Procesamiento | Pendiente | |
| Envío de respuesta | Pendiente | |
| Flujo completo | Pendiente | |

## 5. Registro de errores

Durante las pruebas se documentarán:
- Fecha.
- Función probada.
- Error detectado.
- Causa identificada.
- Solución aplicada.
- Resultado de la nueva prueba.

## 6. Criterio de aprobación

Una prueba se considera aprobada cuando cumple el resultado esperado y no presenta errores que impidan continuar con la integración.

## 7. Criterio de finalización de la etapa

La Etapa 2 se considera finalizada cuando:
- El webhook está verificado.
- Calendi recibe mensajes.
- Calendi procesa mensajes.
- Calendi envía respuestas.
- El flujo completo funciona.
- Los resultados están documentados.

## 8. Estado

Pruebas realizadas parcialmente.

- Verificación del webhook con Meta: completada.
- Recepción de evento de prueba enviado desde el panel de Meta: completada.
- Respuesta HTTP 200 del servidor Flask: comprobada.
- Recepción de mensajes reales desde WhatsApp: pendiente de validación.
- Procesamiento de mensajes: pendiente.
- Envío automático de respuestas desde el webhook: pendiente.
- Flujo completo: pendiente.

Las pruebas de recepción de mensajes reales y el flujo completo quedan pendientes de continuar durante el desarrollo de Calendi.