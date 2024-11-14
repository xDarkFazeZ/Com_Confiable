import socket
import time

def start_client():
    host = '127.0.0.1'
    port = 8000
    message = "Hola servidor confiable!"
    retries = 5  # Número de intentos para reenviar el mensaje
    client_socket = None

    for attempt in range(retries):
        try:
            if client_socket is None:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((host, port))
                print(f"Conectado al servidor en {host}:{port}")

            # Enviar mensaje al servidor
            client_socket.send(message.encode())
            print(f"Enviado: {message}")

            # Esperar por el ACK
            response = client_socket.recv(1024).decode()

            if response == "ACK":
                print(f"Recibido ACK: {response}")
                break  # Salir si el ACK es recibido correctamente
            else:
                print(f"No se recibió ACK, reintentando... (Intento {attempt + 1})")
                time.sleep(2)  # Retraso antes de reintentar

        except socket.error as e:
            print(f"Error de conexión: {e}")
            print("Intentando reconectar...")
            time.sleep(2)
            client_socket = None  # Reinicia la conexión
        except Exception as e:
            print(f"Error desconocido: {e}")
            break

    else:
        print("No se recibió ACK después de varios intentos. Abortando.")
        if client_socket:
            client_socket.close()

if __name__ == "__main__":
    start_client()
