require_relative 'Person_pb'
require 'socket'

serverPort = 12001
serverSocket = TCPServer.open(serverPort)
puts "Sunucu dinliyor..."

while true
  connectionSocket = serverSocket.accept
  serialized_person = connectionSocket.recv(1024)

  person = Person.decode(serialized_person)

  puts "Kişi Bilgileri: "
  puts "Adı: #{person.first_name}"
  puts "Soyadı: #{person.last_name}"
  puts "Numarası: #{person.number}"


  response_message = "Adı: #{person.first_name}, Soyadı: #{person.last_name}, Numarası: #{person.number}"
  connectionSocket.send(response_message, 0)

  connectionSocket.close
end
