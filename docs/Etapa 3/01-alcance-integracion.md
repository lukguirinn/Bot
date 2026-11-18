# Etapa 3 — Alcance de la integración con Google Calendar

## 1. Objetivo

Integrar Calendi con Google Calendar para permitir que cada usuario conecte su propia cuenta de Google y autorice el acceso a su calendario.

La integración debe ser segura, independiente para cada usuario y preparada para incorporar las funciones de administración de eventos en la siguiente etapa.

## 2. Modelo de integración

Se utilizará un modelo de conexión individual mediante OAuth 2.0.

Cada usuario deberá:

1. Iniciar el proceso de vinculación con Google.
2. Iniciar sesión en su cuenta.
3. Autorizar los permisos solicitados por Calendi.
4. Completar la vinculación.
5. Poder desconectar su cuenta cuando lo desee.

Cada conexión deberá quedar asociada al usuario correspondiente de WhatsApp.

## 3. Funcionalidades incluidas en esta etapa

- Configurar Google Cloud.
- Habilitar Google Calendar API.
- Configurar la pantalla de consentimiento OAuth.
- Crear las credenciales necesarias.
- Implementar el proceso de autorización.
- Recibir y validar la respuesta de Google.
- Obtener y renovar tokens de acceso cuando corresponda.
- Asociar cada conexión con su usuario.
- Validar el acceso al calendario principal.
- Contemplar errores de autorización y desconexión.
- Documentar la configuración y las pruebas.

## 4. Funcionalidades fuera del alcance

Las siguientes funciones corresponden a la Etapa 4:

- Crear eventos.
- Consultar eventos.
- Modificar eventos.
- Eliminar eventos.
- Administrar turnos.
- Configurar recordatorios.
- Gestionar disponibilidad horaria.

## 5. Seguridad

- No almacenar credenciales dentro del código.
- No subir archivos `.env` a GitHub.
- Proteger los tokens de acceso y actualización.
- Solicitar únicamente los permisos necesarios.
- Validar el proceso OAuth y su parámetro `state`.
- Evitar que un usuario pueda acceder al calendario de otro.
- Permitir la revocación de la autorización.

## 6. Resultado esperado

Al finalizar la etapa, cada usuario deberá poder vincular su cuenta de Google Calendar con Calendi.

El sistema deberá identificar correctamente cada conexión y validar que puede acceder al calendario autorizado, sin permitir el acceso a información de otros usuarios.

La gestión de eventos quedará preparada para desarrollarse en la Etapa 4.

## 7. Estado

- [x] Modelo de conexión individual definido.
- [ ] Configuración de Google Cloud.
- [ ] Implementación de OAuth 2.0.
- [ ] Asociación de usuarios y conexiones.
- [ ] Validación de acceso al calendario.
- [ ] Pruebas de seguridad y desconexión.