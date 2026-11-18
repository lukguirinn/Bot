# 3.02 — Diseño de autenticación OAuth

## Objetivo
Definir cómo cada usuario autoriza a Calendi a acceder a su calendario.

## Funcionamiento
1. El usuario solicita conectar Google Calendar desde WhatsApp.
2. Calendi genera un enlace de autorización.
3. El usuario abre el enlace.
4. Google solicita iniciar sesión y autorizar permisos.
5. Google devuelve una respuesta al sistema.
6. Calendi valida la respuesta.
7. Se obtienen los tokens de acceso.
8. La conexión queda asociada al usuario de WhatsApp.

## Seguridad
- Utilizar OAuth 2.0.
- Validar el parámetro state.
- Proteger los tokens.
- No compartir conexiones entre usuarios.
- Permitir desconectar la cuenta.

## Resultado esperado
Cada usuario tendrá una conexión independiente con su cuenta de Google.

## Estado
- [x] Modelo OAuth individual definido
- [ ] Implementación pendiente