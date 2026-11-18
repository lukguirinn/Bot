
# Investigación de WhatsApp Business Platform

## Proyecto: Calendi

## 1. Objetivo

Investigar las alternativas disponibles para conectar Calendi con WhatsApp y determinar la tecnología que se utilizará para recibir y enviar mensajes.

## 2. WhatsApp Business Platform

Es la plataforma oficial de Meta que permite integrar WhatsApp con sistemas externos mediante APIs.

Permite desarrollar aplicaciones que gestionan interacciones con usuarios mediante WhatsApp.

## 3. WhatsApp Cloud API

WhatsApp Cloud API es la API alojada por Meta.

Permite:

- Enviar mensajes.
- Recibir mensajes mediante webhooks.
- Consultar estados de entrega.
- Enviar plantillas oficiales.
- Integrar WhatsApp con aplicaciones propias.

Documentación oficial:

https://developers.facebook.com/docs/whatsapp/cloud-api/

## 4. Funcionamiento general

El flujo de comunicación de Calendi será:

1. El usuario envía un mensaje.
2. WhatsApp Cloud API recibe el mensaje.
3. Meta envía una notificación al webhook.
4. Flask recibe el evento.
5. Calendi procesa el mensaje.
6. Se determina la respuesta.
7. El programa envía la respuesta mediante WhatsApp Cloud API.
8. WhatsApp entrega la respuesta al usuario.

## 5. Webhooks

Un webhook permite que una plataforma envíe información automáticamente a otra aplicación cuando sucede un evento.

En Calendi se utilizará para recibir notificaciones de WhatsApp.

El servidor implementa:

- Endpoint GET para verificar el webhook.
- Endpoint POST para recibir notificaciones.

En producción se necesitará una URL pública HTTPS.

## 6. Autenticación

Para comunicarse con WhatsApp Cloud API se necesita un token de acceso.

También se utiliza el identificador del número de teléfono para realizar solicitudes de envío.

Las credenciales deben:

- Guardarse en variables de entorno.
- Mantenerse fuera del repositorio.
- No compartirse públicamente.
- Renovarse cuando corresponda.

## 7. Alternativas evaluadas

### WhatsApp Cloud API

Ventajas:

- Integración oficial.
- Comunicación directa con Meta.
- Control sobre el desarrollo.
- Adecuada para construir un producto propio.

Desventajas:

- Requiere configuración de Meta.
- Requiere desarrollar el servidor.
- Se deben administrar credenciales y lógica.

### Twilio

Ventajas:

- Proporciona herramientas de integración.
- Puede simplificar ciertos procesos.

Desventajas:

- Incorpora un proveedor intermediario.
- Tiene condiciones y costos propios.
- Genera dependencia adicional.

### Bibliotecas no oficiales

Pueden servir para experimentación, pero no serán la base de Calendi debido a sus limitaciones de estabilidad y soporte.

## 8. Tecnología seleccionada

Se seleccionó WhatsApp Cloud API directamente con Meta.

Para el servidor se seleccionó Python con Flask.

Motivos:

- Flask permite desarrollar endpoints HTTP.
- Es liviano.
- Se integra con las herramientas de Python.
- Es adecuado para el desarrollo inicial.

## 9. Costos

Los costos dependerán de las tarifas y condiciones vigentes de Meta, el tipo de mensaje y el país.

También deberán considerarse:

- Hosting.
- Base de datos.
- Servicios adicionales.

Documentación oficial:

https://developers.facebook.com/docs/whatsapp/pricing/

## 10. Reglas de mensajería

Se deberán respetar las políticas de WhatsApp Business Platform.

Entre ellas:

- Obtener los permisos y consentimientos correspondientes.
- Respetar las reglas de mensajería.
- Utilizar plantillas aprobadas cuando corresponda.
- Respetar las condiciones de la ventana de atención.

Documentación:

https://developers.facebook.com/docs/whatsapp/

## 11. Conclusión

Se seleccionó WhatsApp Cloud API como plataforma oficial de comunicación.

La integración se desarrolla mediante Python y Flask.

El envío de respuestas se realizará utilizando plantillas oficiales de WhatsApp cuando corresponda.

## 12. Estado

Investigación y selección tecnológica documentadas.

La integración inicial con Meta se encuentra en desarrollo y validación.

Quedan pendientes las pruebas completas de recepción de mensajes reales y automatización de respuestas.
