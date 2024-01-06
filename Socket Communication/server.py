# Required imports
import socket
import threading

# Constants
HEADER = 60
FORMAT = "utf-8"

# Port for the socket to listen on
PORT = 5050

DISCONNECT_MESSAGE = "Disconnected !!!"

# Get the local machine's IP address as the server address
SERVER = socket.gethostbyname(socket.gethostname())
Address = (SERVER, PORT)

# Create a socket instance
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified address and port
server.bind(Address)


def handle_client(conn, addr):
    """
    Handles a client connection.

    Parameters:
    - conn (socket): The client connection socket.
    - addr (tuple): The address of the client (IP, port).

    Returns:
    None
    """
    print(f"[NEW CONNECTION] {addr} is connected.")
    connected = True

    while connected:
        # Receive the message length
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            # Receive the actual message
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")

            # Send a received message acknowledgment to the client
            conn.send("[MESSAGE] is received".encode(FORMAT))

    conn.close()  # Close the connection with the client


def start():
    """
    Starts the server and handles incoming connections.

    Parameters:
    None

    Returns:
    None
    """
    server.listen()
    print(f"[SERVER] Server is listening on {SERVER}")

    # A forever loop until interrupted or an error occurs
    while True:
        try:
            (conn, addr) = server.accept()

            # Start a new thread for each client
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

            # Print the number of active connections
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

        except KeyboardInterrupt:
            print("\n[SERVER] Server shutting down...")
            break

        except Exception as e:
            print(f"[ERROR] An error occurred: {e}")

    server.close()  # Close the server socket


if __name__ == "__main__":
    print("[SERVER] Server is starting !!!")
    start()
