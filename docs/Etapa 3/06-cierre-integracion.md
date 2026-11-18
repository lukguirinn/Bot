# Etapa 3 — Integración con Google Calendar

## 1. Objetivo

Integrar Google Calendar con Calendi mediante OAuth 2.0, permitiendo que cada usuario conecte su propia cuenta y que sus credenciales sean administradas de forma independiente.

## 2. Implementaciones realizadas

- Creación del proyecto Calendi en Google Cloud.
- Activación de Google Calendar API.
- Configuración de consentimiento OAuth.
- Creación de credenciales OAuth.
- Configuración de permisos de calendario.
- Implementación del flujo de autorización individual.
- Implementación del callback OAuth.
- Almacenamiento de credenciales cifradas mediante Fernet.
- Persistencia de conexiones mediante SQLite.
- Asociación de conexiones al número de WhatsApp.
- Recuperación y renovación automática de credenciales.
- Implementación de consulta de validación del calendario.
- Implementación de desconexión individual.
- Integración de la desconexión con el webhook de WhatsApp.

## 3. Arquitectura implementada

### Módulos principales

- `src/google_auth.py`: autenticación, autorización y desconexión.
- `src/google_calendar.py`: recuperación de credenciales y acceso a Google Calendar.
- `src/database.py`: persistencia de conexiones.
- `src/webhook.py`: recepción y procesamiento de mensajes de WhatsApp.

### Base de datos

Tabla: `conexiones_google`

Campos:
- `id`
- `telefono`
- `credenciales_cifradas`
- `fecha_actualizacion`

Cada conexión se identifica mediante el número de WhatsApp del usuario.

## 4. Seguridad

- Credenciales OAuth almacenadas cifradas.
- Claves de seguridad almacenadas en `.env`.
- Separación de credenciales por usuario.
- Validación de enlaces OAuth firmados.
- Tiempo de expiración para enlaces de autorización.
- Manejo de errores durante la autorización y revocación.

Las credenciales y archivos `.env` no deben subirse al repositorio.

## 5. Pruebas realizadas

### Conexión individual
Se conectaron dos cuentas diferentes de Google Calendar.

### Aislamiento
Se verificó que cada número de WhatsApp recupera su propio calendario.

### Credenciales
Se comprobó que ambas cuentas disponen de credenciales válidas y refresh token.

### Desconexión
Se realizaron cuatro pruebas automatizadas:
- Desconexión exitosa.
- Error de revocación.
- Usuario sin conexión.
- Número inválido.

Resultado: 4/4 aprobadas.

### Integración con WhatsApp
Se verificó la identificación del mensaje de desconexión desde el webhook.

Resultado: 1/1 aprobada.

Total de pruebas automatizadas informadas: 5/5 aprobadas.

## 6. Pendientes antes de producción

- Ejecutar una prueba real de revocación con una cuenta descartable de prueba.
- Configurar OAuth mediante HTTPS.
- Retirar la excepción de transporte inseguro para producción.
- Revisar PKCE y endurecer el flujo OAuth.
- Completar pruebas de errores de red y recuperación de credenciales.
- Configurar las plantillas oficiales de WhatsApp para confirmar la conexión y desconexión.

## 7. Resultado

La integración individual con Google Calendar está implementada y cuenta con pruebas automatizadas satisfactorias.

La etapa queda preparada para continuar con el desarrollo de las funcionalidades de calendario.

**Estado:** Implementación de desarrollo completada. Validaciones de producción pendientes.