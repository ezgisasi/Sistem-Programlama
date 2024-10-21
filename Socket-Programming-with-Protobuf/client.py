from socket import *
import Person_pb2  

person = Person_pb2.Person()
person.first_name = "Ezgi"
person.last_name = "Şaşı"
person.number = 22060346

serialized_person = person.SerializeToString()

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('localhost',12001))

clientSocket.send(serialized_person)

response = clientSocket.recv(1024)  
print('Sunucudan gelen yanıt: ', response.decode())

clientSocket.close()
