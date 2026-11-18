# Investigación de WhatsApp Business Platform

## Proyecto: Calendi

## 1. Objetivo

Investigar las alternativas disponibles para conectar Calendi con WhatsApp y determinar qué tecnología utilizaremos para recibir y enviar mensajes.

## 2. WhatsApp Business Platform

WhatsApp Business Platform es la plataforma de Meta que permite integrar WhatsApp con sistemas externos mediante APIs.

Se diferencia de WhatsApp Messenger y WhatsApp Business App porque permite que un programa propio gestione las interacciones con los usuarios.

## 3. WhatsApp Cloud API

WhatsApp Cloud API es la API alojada por Meta.

Permite:
- Enviar mensajes.
- Recibir mensajes mediante webhooks.
- Consultar estados de entrega.
- Enviar mensajes de texto y otros tipos de contenido admitidos.
- Integrar WhatsApp con aplicaciones propias.

Documentación oficial:

https://developers.facebook.com/docs/whatsapp/cloud-api/

## 4. Funcionamiento general

El flujo de comunicación será:

1. El usuario envía un mensaje a Calendi.
2. WhatsApp Cloud API recibe el mensaje.
3. Meta envía un evento a nuestro webhook.
4. FastAPI recibe el evento.
5. Calendi procesa el mensaje.
6. Calendi genera una respuesta.
7. Nuestro programa envía la respuesta a través de la API.
8. WhatsApp entrega la respuesta al usuario.

## 5. Webhooks

Un webhook permite que una plataforma envíe información automáticamente a otra aplicación cuando sucede un evento.

En Calendi utilizaremos webhooks para recibir:
- Mensajes entrantes.
- Estados de mensajes.
- Notificaciones de eventos admitidos.

El webhook deberá contar con una URL pública HTTPS en el entorno de producción.

## 6. Autenticación

Para comunicarse con WhatsApp Cloud API se requiere un token de acceso.

El token permite autenticar las solicitudes que nuestro programa realiza a Meta.

Las credenciales deben:
- Guardarse en variables de entorno.
- Mantenerse fuera del repositorio.
- No compartirse públicamente.
- Rotarse o renovarse cuando corresponda.

## 7. Alternativas evaluadas

### WhatsApp Cloud API

Ventajas:
- Plataforma oficial.
- Integración directa.
- Control sobre el desarrollo.
- Adecuada para construir un producto propio.

Desventajas:
- Requiere configuración de Meta.
- Requiere implementar el servidor.
- Debemos administrar credenciales y lógica.

### Twilio

Ventajas:
- Proveedor con herramientas propias.
- Puede simplificar algunos aspectos de integración.

Desventajas:
- Intermediario adicional.
- Costos propios del proveedor.
- Dependencia de sus servicios.

### Bibliotecas no oficiales

Ventajas:
- Pueden ser útiles para experimentar.

Desventajas:
- Menor estabilidad.
- Riesgo de desconexión o bloqueo.
- No son adecuadas como base recomendada para un producto comercial.

## 8. Costos

El costo de utilizar WhatsApp puede depender de las tarifas vigentes de Meta, el país, el tipo de mensaje y las condiciones aplicables.

También deben considerarse:
- Hosting.
- Base de datos.
- Servicios externos adicionales.

Antes del lanzamiento se deben consultar las tarifas oficiales:

https://developers.facebook.com/docs/whatsapp/pricing/

No se establece un costo definitivo en esta etapa.

## 9. Reglas de mensajería

WhatsApp establece condiciones para el envío de mensajes.

Entre ellas:
- El usuario debe haber otorgado el consentimiento correspondiente para recibir comunicaciones.
- Existen reglas para mensajes iniciados por la empresa.
- Los mensajes enviados fuera de la ventana de atención al usuario pueden requerir plantillas aprobadas.
- Deben respetarse las políticas de WhatsApp Business.

Documentación:

https://developers.facebook.com/docs/whatsapp/

## 10. Conclusión

Se recomienda utilizar WhatsApp Cloud API directamente con Meta.

Esta alternativa permite construir Calendi sobre una integración oficial, con control sobre el código y la arquitectura.

La integración se realizará utilizando Python y Flask.

## 11. Estado

Investigación documentada.

Pendiente:
- Configuración de cuenta.
- Configuración del número.
- Obtención de credenciales.
- Implementación del webhook.
- Pruebas de comunicación.
