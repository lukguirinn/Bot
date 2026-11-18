
# Entorno de desarrollo

## 1. Objetivo

Documentar las herramientas y configuraciones necesarias para desarrollar, ejecutar y probar Calendi.

## 2. Herramientas

- Python 3.
- Visual Studio Code.
- Git.
- GitHub.
- Flask.
- Ngrok.
- Cuenta de Meta Developers.

## 3. Instalación

### Python

https://www.python.org/downloads/

Verificar:

```powershell
python --version
```

### Git

https://git-scm.com/downloads

Verificar:

```powershell
git --version
```

### Visual Studio Code

https://code.visualstudio.com/

## 4. Repositorio

Clonar el repositorio:

```powershell
git clone https://github.com/lukguirinn/Bot.git
```

Ingresar:

```powershell
cd Bot
```

## 5. Entorno virtual

Crear el entorno virtual:

```powershell
python -m venv .venv
```

Activarlo:

```powershell
.venv\Scripts\Activate.ps1
```

## 6. Dependencias

Instalar las dependencias registradas:

```powershell
pip install -r requirements.txt
```

## 7. Variables de entorno

El proyecto utiliza un archivo `.env` en la raíz.

Variables necesarias:

```env
WHATSAPP_TOKEN=
WHATSAPP_PHONE_NUMBER_ID=
WEBHOOK_VERIFY_TOKEN=
```

Los valores reales deben permanecer privados.

El archivo `.env` no debe publicarse en GitHub.

## 8. Ejecución

El servidor Flask se inicia desde la raíz del proyecto mediante:

```powershell
python -m src.main
```

El servidor utiliza el puerto 5000.

## 9. Diagnóstico

Para verificar las credenciales de WhatsApp se utiliza:

```powershell
python verificar.py
```

Esta herramienta es independiente del inicio normal del servidor.

## 10. Ngrok

Durante las pruebas locales se utilizará Ngrok para exponer el servidor Flask a Meta.

La dirección pública deberá configurarse en el webhook de Meta.

## 11. Verificación del entorno

El entorno se considera preparado cuando:

- Python está instalado.
- Git está configurado.
- El repositorio está disponible.
- El entorno virtual funciona.
- Las dependencias están instaladas.
- Las variables de entorno están configuradas.
- El servidor Flask inicia correctamente.
