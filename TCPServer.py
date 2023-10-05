import socket
import threading

def handleClient(connectionSocket, addr):
    print(str(addr) + " successful connection")
    sentence = connectionSocket.recv(1024).decode()

    sentenceSplit = sentence.split(";", 2)

    if "Random" == sentenceSplit[0]:
        try:
            min_val = int(sentenceSplit[1])
            max_val = int(sentenceSplit[2])
            import random
            random_num = random.randint(min_val, max_val)
            response = str(random_num)
            print(response)
            connectionSocket.send(response.encode())
        except ValueError:
            response = "Invalid input. Brug format 'Random;<tal1>;<tal2>'"
            print(response)
            connectionSocket.send(response.encode())
    elif "Add" == sentenceSplit[0]:
        try:
            num1 = int(sentenceSplit[1])
            num2 = int(sentenceSplit[2])
            result = num1 + num2
            response = str(result)
            print(response)
            connectionSocket.send(response.encode())
        except ValueError:
            response = "Invalid input. Brug format 'Add;<tal1>;<tal2>'"
            print(response)
            connectionSocket.send(response.encode())
    elif "Subtract" == sentenceSplit[0]:
        try:
            num1 = int(sentenceSplit[1])
            num2 = int(sentenceSplit[2])
            result = num1 - num2
            response = str(result)
            print(response)
            connectionSocket.send(response.encode())
        except ValueError:
            response = "Invalid input. Brug format 'Subtract;<tal1>;<tal2>'"
            print(response)
            connectionSocket.send(response.encode())
    else:
        response = "Error"
        print(response)
        connectionSocket.send(response.encode())

    connectionSocket.close()

# Opret en socket til serveren
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socketen til en specifik adresse og port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Lyt efter indkommende forbindelser
server_socket.listen(5)
print("Serveren lytter på {}:{}".format(*server_address))

while True:
    # Accepter en indkommende forbindelse
    client_socket, client_address = server_socket.accept()
    print("Forbindelse fra:", client_address)

    # Opret en tråd til at håndtere klienten
    handle_thread = threading.Thread(target=handleClient, args=(client_socket, client_address))
    handle_thread.start()
