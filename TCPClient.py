import socket
import threading
# Opret en socket til klienten
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Forbinder til serveren
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    while True:
        # Læs kommando fra terminalen
        command = input("Indtast kommando Random;, Add; or Subtract;")

        if command == "exit":
            break

        # Send kommandoen til serveren
        client_socket.send(command.encode())

        # Modtag og udskriv svaret fra serveren
        response = client_socket.recv(1024)
        print("Modtaget fra serveren:", response.decode('utf-8'))

except KeyboardInterrupt:
    pass
finally:
    # Luk forbindelsen til serveren
    client_socket.close()
