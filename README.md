# Propuesta Formativa Obligatoria (PFO)

**TP: Implementación de un Chat Básico Cliente-Servidor con Sockets y Base de Datos**

## Descripción

Este trabajo práctico consiste en desarrollar un chat básico Cliente-Servidor utilizando sockets en Python y una base de datos SQLite.
El servidor recibe mensajes de los clientes, los almacena en la base de datos y envía una confirmación con timestamp.
El cliente se conecta al servidor, envía mensajes y muestra la respuesta del servidor.

## Objetivo

- Configurar un servidor de sockets en Python que reciba mensajes de clientes.
- Guardar los mensajes en una base de datos SQLite.
- Aplicar buenas prácticas de modularización, comentarios claros y manejo de errores.

## Requisitos

- Python 3.x
- Módulo `sqlite3` (incluido en la instalación estándar de Python)

## Instalación

1. Clonar o descargar este repositorio.
2. Ubicar los archivos `servidor.py` y `cliente.py` en la misma carpeta.
3. (Opcional) Crear un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Linux / Mac
   venv\Scripts\activate         # Windows
   ```

## Uso

1. Abrir una terminal y navegar a la carpeta del proyecto.
2. **Ejecutar el servidor:**
   ```bash
   python3 servidor.py
   ```
   El servidor quedará escuchando en `localhost:8080`.

3. **En otra terminal, ejecutar el cliente:**
   ```bash
   python3 cliente.py
   ```

4. Escribir mensajes en la terminal.
5. Ver las respuestas del servidor con timestamp.
6. Para salir, escribir `salir` en el cliente.

## Archivos

- `servidor.py`: Servidor que escucha en localhost:8080
- `cliente.py`: Cliente que se conecta al servidor
- `chat.db`: Base de datos SQLite (se crea automáticamente)

## Características

- Servidor multicliente usando threads
- Almacenamiento de mensajes en SQLite con timestamp e IP
- Manejo de errores de conexión y base de datos
- Confirmación de recepción con timestamp