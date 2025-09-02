import socket
import sqlite3
import threading
from datetime import datetime

def inicializar_db():
    """Inicializa la base de datos SQLite"""
    conn = sqlite3.connect('chat.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contenido TEXT NOT NULL,
            fecha_envio TEXT NOT NULL,
            ip_cliente TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn

def guardar_mensaje(conn, contenido, ip_cliente):
    """Guarda mensaje en la base de datos"""
    try:
        cursor = conn.cursor()
        fecha_envio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(
            'INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) VALUES (?, ?, ?)',
            (contenido, fecha_envio, ip_cliente)
        )
        conn.commit()
        return fecha_envio
    except sqlite3.Error as e:
        print(f"Error en DB: {e}")
        return None

def manejar_cliente(client_socket, addr, conn):
    """Maneja la conexión de un cliente"""
    try:
        while True:
            mensaje = client_socket.recv(1024).decode('utf-8')
            if not mensaje:
                break
            
            # Guardar mensaje en DB
            timestamp = guardar_mensaje(conn, mensaje, addr[0])
            
            if timestamp:
                respuesta = f"Mensaje recibido: {timestamp}"
            else:
                respuesta = "Error al guardar mensaje"
            
            client_socket.send(respuesta.encode('utf-8'))
    
    except Exception as e:
        print(f"Error con cliente {addr}: {e}")
    finally:
        client_socket.close()

def inicializar_socket():
    """Inicializa y configura el socket del servidor"""
    try:
        # Configuración del socket TCP/IP
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('localhost', 9999))
        server_socket.listen(5)
        return server_socket
    except OSError as e:
        print(f"Error al inicializar socket: {e}")
        return None

def main():
    """Función principal del servidor"""
    # Inicializar base de datos
    try:
        conn = inicializar_db()
        print("Base de datos inicializada")
    except sqlite3.Error as e:
        print(f"Error DB no accesible: {e}")
        return
    
    # Inicializar socket
    server_socket = inicializar_socket()
    if not server_socket:
        return
    
    print("Servidor escuchando en localhost:9999")
    
    try:
        while True:
            # Aceptar conexiones
            client_socket, addr = server_socket.accept()
            print(f"Cliente conectado desde {addr}")
            
            # Crear hilo para manejar cliente
            client_thread = threading.Thread(
                target=manejar_cliente, 
                args=(client_socket, addr, conn)
            )
            client_thread.daemon = True
            client_thread.start()
    
    except KeyboardInterrupt:
        print("\nCerrando servidor...")
    finally:
        server_socket.close()
        conn.close()

if __name__ == "__main__":
    main()