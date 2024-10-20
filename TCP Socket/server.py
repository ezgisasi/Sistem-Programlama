from socket import *

def server():
    serverSocket = socket(AF_INET, SOCK_STREAM)  
    serverSocket.bind(('localhost', 12000))     
    serverSocket.listen(1)              

    print('Sunucu dinliyor...')

    connectionSocket, addr = serverSocket.accept() 
    print(f'Bağlantı kuruldu: {addr}')

    try:
        while True:
            message = connectionSocket.recv(1024).decode()  
            print(f'Gelen sayi: {message}')
    except Exception as e:
        print(f'Hata: {e}')
    finally:
        connectionSocket.close()  

if __name__ == '__main__':
    server()
