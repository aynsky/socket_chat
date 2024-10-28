# Python Chat Program

This is a simple chat program built in Python that allows multiple clients to connect to a server and exchange messages in real-time. The project consists of two main components: the server and the client.

## Features

- Real-time chat between multiple clients
- Timestamps for each message
- Notifications when clients connect or disconnect

## Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Files

- `server.py`: The server code that handles client connections and message broadcasting
- `client.py`: The client code that connects to the server, sends messages, and receives broadcasts

### Running the Program

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   
2. **Run the Server**

    Open a terminal and start the server:

    ```bash
    python3 server.py

  The server will start listening for incoming connections on 127.0.0.1:12345


3. **Run the Client**
   
   Open another terminal for each client instance and run:

   ```bash
   python3 client.py

  Each client will be prompted to enter a username.
  Once connected, clients can start sending messages to each other.

**Usage**

Sending Messages: Type a message in the client terminal and press Enter to send it.
Receiving Messages: Each message includes a timestamp and shows the username of the sender.

**Example Output** - server
    
    New connection from ('127.0.0.1', 12345)
    [2024-10-28 12:34:56] Alice: Hello, everyone!
    [2024-10-28 12:35:01] Bob: Hi, Alice!
    Alice has disconnected.
    
**client**

    Enter your username: Alice
    [2024-10-28 12:34:56] Bob: Hi, Alice!

Notes
Ports: The default port is 12345. You can modify this in server.py and client.py if needed.
Concurrency: Each client runs in its own thread, allowing simultaneous messaging.


**License**
This project is licensed under the MIT License. See the LICENSE file for details.

Be sure to replace `https://github.com/your-username/your-repo-name.git` with the actual URL of your repository before uploading. Let me know if there’s anything else you’d like to add!





   
