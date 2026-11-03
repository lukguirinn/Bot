
# Entorno de desarrollo

## 1. Objetivo

Preparar el entorno local necesario para desarrollar, ejecutar y probar Calendi.

## 2. Herramientas necesarias

- Python 3.
- Visual Studio Code.
- Git.
- Cuenta de GitHub.
- Navegador web.

## 3. Instalación

### Python

Instalar Python desde:

https://www.python.org/downloads/

Verificar la instalación:

```bash
python --version
```

### Git

Instalar Git desde:

https://git-scm.com/downloads

Verificar la instalación:

```bash
git --version
```

### Visual Studio Code

Instalar desde:

https://code.visualstudio.com/

## 4. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta:

```bash
cd calendi
```

## 5. Crear entorno virtual

```bash
python -m venv venv
```

Activar el entorno virtual en Windows:

```bash
venv\Scripts\activate
```

## 6. Instalar dependencias

```bash
pip install flask
```

Las dependencias adicionales se incorporarán a medida que avance el desarrollo.

## 7. Ejecutar el proyecto

```bash
python main.py
```

## 8. Variables de entorno

Las credenciales y configuraciones privadas se almacenarán mediante variables de entorno.

Se utilizará un archivo `.env` local que no deberá publicarse en GitHub.

El archivo `.env.example` servirá como referencia para las variables necesarias.

## 9. Herramientas externas

Durante el desarrollo será necesario configurar:

- Meta Developers.
- WhatsApp Cloud API.
- Google Cloud.
- Google Calendar API.

Estas configuraciones se realizarán en las etapas correspondientes.

## 10. Verificación

El entorno se considerará preparado cuando:

- Python esté instalado.
- Git esté configurado.
- El repositorio esté clonado.
- El entorno virtual funcione.
- Flask esté instalado.
- El proyecto pueda ejecutarse localmente.
