# Configuración de Meta y WhatsApp

## Proyecto: Calendi

## 1. Objetivo

Configurar los recursos necesarios en Meta para conectar Calendi con WhatsApp Cloud API.

## 2. Requisitos

Antes de comenzar:
- Tener acceso a una cuenta de Meta.
- Tener acceso a Meta for Developers.
- Crear una aplicación.
- Agregar WhatsApp como producto.
- Disponer de un número de prueba o un número habilitado para la plataforma.
- Configurar las credenciales.

## 3. Crear la aplicación

Ingresar a:

https://developers.facebook.com/

Pasos:
1. Iniciar sesión.
2. Ingresar a la sección de aplicaciones.
3. Crear una nueva aplicación.
4. Seleccionar el tipo de aplicación disponible para la integración.
5. Agregar el producto WhatsApp.
6. Ingresar al panel de configuración de WhatsApp.

## 4. Configurar WhatsApp

Dentro del panel de WhatsApp se deberán identificar los recursos disponibles:

- WhatsApp Business Account ID.
- Phone Number ID.
- Número de teléfono.
- Token de acceso.

Estos datos se utilizarán para conectar el programa con la API.

## 5. Número de prueba

Para el desarrollo inicial se recomienda utilizar el número de prueba proporcionado por Meta.

El número de prueba permitirá validar la integración sin comenzar directamente con el número definitivo de Calendi.

Se deberán seguir las instrucciones del panel para agregar el destinatario de prueba autorizado.

## 6. Credenciales

Las credenciales necesarias se almacenarán mediante variables de entorno.

Ejemplo de nombres:

```env
WHATSAPP_TOKEN=
WHATSAPP_PHONE_NUMBER_ID=
WHATSAPP_BUSINESS_ACCOUNT_ID=
WHATSAPP_VERIFY_TOKEN=
```

Los valores reales no deben incluirse en este documento.

## 7. Configuración del webhook

Cuando el servidor esté disponible, se configurará el webhook.

Se deberá definir:
- URL pública del servidor.
- Token de verificación.
- Eventos o campos de WhatsApp que se recibirán.

Meta realizará una solicitud de verificación para confirmar que el servidor controla la URL configurada.

## 8. Seguridad

- No compartir tokens.
- No publicar credenciales.
- No incluir secretos en capturas de pantalla.
- No subir el archivo `.env`.
- Revocar o renovar credenciales si quedan expuestas.

## 9. Registro de configuración

Completar durante la tarea #16:

| Elemento | Estado |
|---|---|
| Aplicación de Meta creada | Pendiente |
| WhatsApp agregado | Pendiente |
| Número de prueba configurado | Pendiente |
| Token obtenido | Pendiente |
| Phone Number ID identificado | Pendiente |
| Credenciales almacenadas de forma segura | Pendiente |

## 10. Resultado esperado

Al finalizar:
- La aplicación de Meta estará configurada.
- WhatsApp estará habilitado.
- Se dispondrá de los recursos necesarios para conectar el servidor.
- Las credenciales estarán guardadas de forma segura.

## 11. Estado

Documento preparado.

La configuración real se completará durante la tarea #16.
