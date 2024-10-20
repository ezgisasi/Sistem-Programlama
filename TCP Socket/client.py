from socket import *
import random
import time

def client():
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(('localhost', 12000)) 

    try:
        while True:
            randomNumber = random.random()  
            clientSocket.send(str(randomNumber).encode())  
            print(f'Gönderilen sayi: {randomNumber}')
            time.sleep(1)  
    except Exception as e:
        print(f'Hata: {e}')
    finally:
        clientSocket.close()  

if __name__ == '__main__':
    client()
