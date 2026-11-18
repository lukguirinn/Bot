

# Configuración de Meta y WhatsApp

## Proyecto: Calendi

## 1. Objetivo

Documentar la configuración realizada en Meta para conectar Calendi con WhatsApp Cloud API.

## 2. Plataforma utilizada

Se utilizó Meta for Developers para crear y configurar la aplicación de Calendi.

Plataforma:
https://developers.facebook.com/

Tecnología seleccionada:
- WhatsApp Business Platform.
- WhatsApp Cloud API.
- Webhooks de Meta.

## 3. Recursos configurados

Durante la configuración se realizaron las siguientes tareas:

- Creación de la aplicación en Meta.
- Incorporación del producto WhatsApp.
- Configuración del número de prueba.
- Obtención del token de acceso.
- Identificación del Phone Number ID.
- Configuración de las credenciales locales.
- Configuración del webhook.
- Verificación de la conexión con Meta.

## 4. Variables de entorno

El proyecto utiliza las siguientes variables:

```env
WHATSAPP_TOKEN=
WHATSAPP_PHONE_NUMBER_ID=
WEBHOOK_VERIFY_TOKEN=
```

Los valores reales se almacenan exclusivamente en el archivo `.env`.

El archivo `.env`:
- Se mantiene fuera del repositorio.
- Está incluido en `.gitignore`.
- No debe compartirse ni publicarse.

## 5. Configuración del webhook

Se implementó un servidor Flask con los siguientes endpoints:

### GET /webhook

Permite verificar la conexión del webhook con Meta.

### POST /webhook

Permite recibir notificaciones y eventos enviados por WhatsApp.

La configuración se realizó utilizando una URL pública de desarrollo mediante Ngrok.

## 6. Seguridad

Se adoptaron las siguientes medidas:

- No incluir tokens en el código fuente.
- Guardar credenciales mediante variables de entorno.
- Excluir `.env` del repositorio.
- No compartir credenciales en capturas o documentación.
- Mantener las credenciales fuera de GitHub.

## 7. Registro de configuración

| Elemento | Estado |
|---|---|
| Aplicación de Meta creada | Completado |
| WhatsApp agregado | Completado |
| Número de prueba configurado | Completado |
| Token obtenido | Completado |
| Phone Number ID identificado | Completado |
| Credenciales locales configuradas | Completado |
| Archivo `.env` excluido de GitHub | Completado |
| Webhook configurado | Completado |
| Verificación del webhook | Completado |

## 8. Pruebas pendientes

Aunque la configuración inicial está realizada, quedan pendientes:

- Validar la recepción de mensajes reales.
- Comprobar el procesamiento de mensajes reales.
- Validar la respuesta automática mediante plantillas oficiales.
- Probar el flujo completo de comunicación.

Estas pruebas se registran en `04-pruebas.md`.

## 9. Resultado

La configuración inicial de Meta y WhatsApp Cloud API se encuentra realizada.

Calendi dispone de una aplicación configurada, credenciales locales y un webhook verificado.

La validación completa de la comunicación con mensajes reales continúa pendiente.

## 10. Estado

Configuración inicial completada.

Pruebas de comunicación real pendientes de validación.
