import socket
import threading
import time

def handle_client(client_socket, client_address):
    """Função para lidar com as conexões dos clientes"""
    print(f"Conexão estabelecida com {client_address}")
    
    try:
        while True:
            # Recebe dados do cliente
            data = client_socket.recv(1024)
            if not data:
                break
                
            message = data.decode('utf-8')
            print(f"Recebido de {client_address}: {message}")
            
            # Envia resposta ao cliente
            response = f"Eco: {message}"
            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Erro ao comunicar com {client_address}: {e}")
    finally:
        client_socket.close()
        print(f"Conexão com {client_address} encerrada")

def start_server(host='0.0.0.0', port=8888):
    """Inicia o servidor socket"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((host, port))
        server.listen(5)
        print(f"Servidor iniciado em {host}:{port}")
        
        while True:
            client_socket, client_address = server.accept()
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.daemon = True
            client_thread.start()
            
    except KeyboardInterrupt:
        print("Servidor encerrado pelo usuário")
    except Exception as e:
        print(f"Erro no servidor: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    print("Iniciando servidor de socket...")
    start_server('127.0.0.1')