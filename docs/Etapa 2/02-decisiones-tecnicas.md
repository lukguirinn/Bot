# Decisiones técnicas

## Proyecto: Calendi

## 1. Objetivo

Registrar las decisiones tecnológicas que se utilizarán durante la Etapa 2 para evitar cambios innecesarios y mantener una arquitectura consistente.

## 2. Decisiones

| Componente | Decisión |
|---|---|
| Plataforma | WhatsApp Business Platform |
| API | WhatsApp Cloud API |
| Lenguaje | Python |
| Framework | FastAPI |
| Base de datos inicial | SQLite |
| Hosting previsto | Render |
| Entorno de desarrollo | Local |
| Control de versiones | Git y GitHub |

## 3. WhatsApp Cloud API

Se utilizará la API oficial de Meta para conectar Calendi con WhatsApp.

Motivo:
- Es una integración oficial.
- Permite enviar y recibir mensajes.
- Permite desarrollar una solución propia.
- Evita depender de bibliotecas no oficiales.

## 4. Python

Se utilizará Python como lenguaje principal.

Motivo:
- Es el lenguaje que el desarrollador está estudiando.
- Permite implementar la lógica del bot.
- Cuenta con herramientas para desarrollar APIs y automatizaciones.

## 5. FastAPI

Se utilizará FastAPI para crear el servidor.

Responsabilidades:
- Crear endpoints.
- Recibir solicitudes HTTP.
- Implementar el webhook.
- Validar las solicitudes.
- Conectar el webhook con la lógica del bot.

## 6. SQLite

Se utilizará SQLite como base de datos inicial.

Motivo:
- Es sencilla de configurar.
- No requiere un servidor independiente.
- Es adecuada para el prototipo inicial.

La elección deberá revisarse cuando Calendi necesite una base de datos compartida para múltiples instancias o una mayor capacidad de operación.

## 7. Render

Se considera Render como hosting previsto para desplegar el servidor.

Durante el desarrollo se utilizará el entorno local.

Antes de desplegar se verificarán:
- Compatibilidad con FastAPI.
- Disponibilidad de HTTPS.
- Configuración de variables de entorno.
- Persistencia de datos.
- Plan y costos vigentes.

## 8. Estructura inicial del proyecto

```text
Programacion-1/
│
├── docs/
│   └── etapa-2/
│
├── src/
│   ├── main.py
│   ├── config.py
│   ├── webhook.py
│   ├── whatsapp.py
│   └── bot.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 9. Responsabilidades de los archivos

### main.py

Iniciar la aplicación FastAPI.

### config.py

Leer y administrar la configuración del proyecto.

### webhook.py

Gestionar la verificación del webhook y la recepción de eventos.

### whatsapp.py

Contener las funciones para comunicarse con WhatsApp Cloud API.

### bot.py

Procesar los mensajes y generar las respuestas.

## 10. Seguridad

Las credenciales no deben almacenarse directamente en el código.

Se utilizarán variables de entorno.

El archivo `.env` deberá estar incluido en `.gitignore`.

Se podrá mantener un `.env.example` con los nombres de las variables, sin credenciales reales.

## 11. Decisiones pendientes de revisión

- Confirmar el hosting elegido.
- Confirmar la persistencia de SQLite en el hosting.
- Evaluar PostgreSQL cuando sea necesario.
- Evaluar costos antes del lanzamiento.
- Definir políticas de conservación de datos.

## 12. Estado

Decisiones iniciales documentadas.

Las decisiones podrán revisarse si las necesidades del proyecto cambian.
