import socket
import threading
username = input("Enter your username: ")
def receive_messages(client_socket):
    while True:
        try:
            full_message = client_socket.recv(1024) # Receive message from the client
            print( full_message.decode())
        except:
            print("Connection closed.")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    threading.Thread(target=receive_messages, args=(client_socket,)).start() # Start a new thread to receive messages
    while True:
        message = input()
        full_massage = f"{username}: {message}"
        client_socket.send(full_massage.encode())

start_client()