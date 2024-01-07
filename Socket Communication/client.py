# Required imports
import socket
import time

# Constants
PORT = 5050
HEADER = 60
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "Disconnected !!!"

# Get the local machine's IP address as the server address
SERVER = socket.gethostbyname(socket.gethostname())
Address = (SERVER, PORT)

# Creating a socket instance
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(Address)


# Function to send messages
def send(msg):
    """
    Sends a message to the server.

    Parameters:
    - msg (str): The message to be sent.

    Returns:
    None
    """
    # Encoding the message
    message = msg.encode(FORMAT)
    msg_length = len(message)

    # Ensure the header is always HEADER bytes by padding with spaces if needed
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))

    # Sending the message
    client.send(send_length)
    client.send(message)

    # Receive and print acknowledgment from the server
    print(client.recv(2048).decode(FORMAT))


# Sending messages
send("Hello server socket. Client socket here.")
time.sleep(1)  # Introducing a delay using time.sleep() instead of input()

send("Let's make a connection by applying the fundamentals of networking and socket.")
time.sleep(1)

send("Bye!!!")
time.sleep(1)

# Disconnecting from the server
send(DISCONNECT_MESSAGE)

# Close the socket connection
client.close()
