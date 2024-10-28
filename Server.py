import socket
import threading
from datetime import datetime

clients = [] # List to keep track of connected clients

def handle_clients(client_socket, address):
    # Announce new connection message to all clients
    welcome_message = f"{address} connected."
    print(welcome_message)
    broadcast(welcome_message.encode())
    
    while True:
        try:
            message = client_socket.recv(1024)
            if message: # If there's a message, broadcast it to all other clients
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                formatted_message = f"{timestamp}: {message.decode()}" # Format the message with timestamp
                print(formatted_message)
                broadcast(formatted_message.encode())
        except:
            disconnect_message = f"{address} has disconnected."
            print(disconnect_message)
            broadcast(disconnect_message.encode())
            clients.remove(client_socket) # Remove the client from the list and close the connection
            client_socket.close()  # Close the connection
            break
def broadcast(message):
    for client in clients: # Send the message to all other clients except the sender
        try:
            client.send(message) # Send the message to the client
        except:
            # If the client has disconnected, remove it from the list and close the connection
            client.close()
            clients.remove(client)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5) 
    print("Server is running...")

    while True:
        client_socket, address = server_socket.accept() # Accept a new client
        clients.append(client_socket) # Add new client to the list
        print(f"New Connection from {address}")
        threading.Thread(target=handle_clients, args=(client_socket, address)).start() # Create a new thread for each client

start_server()