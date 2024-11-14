import socket
import random
import time

def handle_client(client_socket, addr):
    try:
        message = client_socket.recv(1024).decode()
        print(f"Recibido de {addr}: {message}")

        # Simulación de pérdida de ACK
        if random.random() < 0.2:  # 20% de probabilidades de perder el paquete
            print(f"Simulación: pérdida de ACK para {addr}")
        else:
            # Enviar un ACK (confirmación)
            client_socket.send("ACK".encode())
            print(f"Enviado ACK a {addr}")

    except Exception as e:
        print(f"Error con el cliente {addr}: {e}")
    finally:
        client_socket.close()

def start_server():
    host = '192.168.0.211'
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Servidor confiable escuchando en {host}:{port}")

    while True:
        try:
            print("Esperando conexiones de clientes...")
            client_socket, addr = server_socket.accept()
            print(f"Conexión establecida con {addr}")
            handle_client(client_socket, addr)
        except KeyboardInterrupt:
            print("Servidor detenido manualmente.")
            break
    server_socket.close()

if __name__ == "__main__":
    start_server()
