# Name: Phearak Both Bunna
# CPTS455 HW3

# Rosources used for this Assignment:
    # https://www.geeksforgeeks.org/socket-programming-python/
    # https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
    # https://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php 

import socket

# This is for the server side
def server_side():
    
    # We can get the hostname and specify the port number (above 1024)
    host = socket.gethostname()
    port = 12345
    
    # Create the socket object
    server_socket = socket.socket()
    # Then we bind the socket to the address we specify above
    server_socket.bind((host, port))
    # We listen for incoming connections
    server_socket.listen()
    # Accept the new connection 
    # Store the new socket object & address of the client initiated the connection (tuple)
    obj, addr = server_socket.accept()

    # Show which address we are connected to
    print("Connected to: " + str(addr))

    # Keep the loop running
    while True:
        # To receive the messages (1024 is the size in bytes it can accpet)
        messages = obj.recv(1024).decode()
        if not messages:
            # We break the loop is no data is received
            break
        
        # Check to see if the data being sent is a text message
        if messages.startswith("text:"):
            # This will only extract the actual message content (not the front part)
            # Ex: "text: Hello there!", only "Hello there!" will be extracted
            message = messages[len("text:"):]
            print("Message received from USER: " + message)
            # Send back a response to the client side
            response = input("Enter a response: ")
            obj.send(response.encode())
        # Check to see if the data being sent is a file
        elif messages.startswith("file:"):
            # We extract only the file name
            file_name = messages[len("file:"):]
            file_open = obj.recv(1024)
            # We open the file being sent, takes the binary data that is stored & write it to the file name specified
            with open(file_name, 'wb') as file:
                file.write(file_open)
            # Let the user know that the file has been received
            print(f"File received: {file_name}")
        

    # We close the connection
    obj.close()


if __name__ == '__main__':
    server_side()
