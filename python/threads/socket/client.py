import socket
import sys
import time

def connect_to_server(host='localhost', port=8888, client_name="cliente 1"):
    """Conecta ao servidor socket e envia mensagens"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((host, port))
        print(f"Conectado ao servidor {host}:{port}")
        
        count = 1
        while True:
            # Envia mensagem para o servidor
            message = f"Mensagem {count} do {client_name}"
            client.send(message.encode('utf-8'))
            print(f"Enviado: {message}")
            
            # Recebe resposta do servidor
            response = client.recv(1024).decode('utf-8')
            print(f"Recebido: {response}")
            
            count += 1
            time.sleep(2)  # Espera 2 segundos antes de enviar a próxima mensagem
            
            # Opção para encerrar o cliente após 5 mensagens
            if count > 10:
                choice = input("Enviar mais mensagens? (s/n): ")
                if choice.lower() != 's':
                    count = 0
                    break
                
                    
    except KeyboardInterrupt:
        print("Cliente encerrado pelo usuário")
    except Exception as e:
        print(f"Erro no cliente: {e}")
    finally:
        client.close()
        print("Conexão encerrada")

if __name__ == "__main__":
    # Verifica se o host foi fornecido como argumento de linha de comando
    host = 'localhost'
    if len(sys.argv) > 1:
        client_name = sys.argv[1] if sys.argv[1] else "client 1"
    else:
        client_name = "client 1"
    connect_to_server(host=host, client_name=client_name)