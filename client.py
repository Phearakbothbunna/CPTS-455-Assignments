# Name: Phearak Both Bunna
# CPTS455 HW3

# Rosources used for this Assignment:
    # https://www.geeksforgeeks.org/socket-programming-python/
    # https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
    # https://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php 


import socket
import os

# This if for client side
def client_side():
    
    # We can ge the hostname and specify the port number
    host = socket.gethostname()
    port = 12345 

    # Create socket object
    client_socket = socket.socket()
    # Then we connect the client socket to the server
    client_socket.connect((host, port))

    while True:
        # Get input from users
        user_input = input("Enter 'text' to send text messages OR 'file' to share file: ")
        # If users want to quit, they can type in "quit"
        if user_input.lower() == 'quit':
            break
        # Handle text message sending (we encode before send over through network socket)
        elif user_input.lower() == 'text':
            while True:
                # If user type in "quit", we will take them back to the beginning
                messages = input("Enter your text message (Type 'exit' to go back to beginning): ")
                if messages.lower() == 'exit':
                    break
                # Send over the message in a string format that server can recognize
                client_socket.send(f"text:{messages}".encode())

                # When we receive the message, we decode it
                message = client_socket.recv(1024).decode()
                # Display the messages in the terminal
                print("Message received from SERVER: " + message)
            
        # Handle file sending 
        elif user_input.lower() == 'file':
            file_path = input("Enter the path for the file you wish to send: ")
            # This will check whether the file path given exists in the system
            if os.path.exists(file_path):
                # This will open the file at the given path in a binary read mode
                with open(file_path, 'rb') as file:
                    # This will read the content of the file as binary data
                    file_open = file.read()
                    # Send over the file in a format where the server can recognize
                    client_socket.send(f"file:{os.path.basename(file_path)}".encode())
                    client_socket.send(file_open)
            else:
                print("File not found...")
        else:
            print("INVALID. Please choose between text or file...")

    # We close the connection
    client_socket.close()
    print("Connection closed!")


if __name__ == '__main__':
    client_side()
