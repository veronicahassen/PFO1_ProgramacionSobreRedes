import socket

def conectar_servidor():
    """Conecta al servidor en localhost:5000"""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 9999))
        return client_socket
    except ConnectionRefusedError:
        print("Error: No se pudo conectar al servidor")
        return None
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

def main():
    """Función principal del cliente"""
    # Conectar al servidor
    client_socket = conectar_servidor()
    if not client_socket:
        return
    
    print("Conectado al servidor. Escribe 'salir' para terminar.")
    
    try:
        while True:
            # Solicitar mensaje al usuario
            mensaje = input("Mensaje: ")
            
            # Verificar condición de salida
            if mensaje.lower() == 'salir':
                break
            
            # Enviar mensaje al servidor
            client_socket.send(mensaje.encode('utf-8'))
            
            # Recibir respuesta del servidor
            respuesta = client_socket.recv(1024).decode('utf-8')
            print(f"Servidor: {respuesta}")
    
    except KeyboardInterrupt:
        print("\nDesconectando...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()