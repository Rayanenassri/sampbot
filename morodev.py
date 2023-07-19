import socket
import time

SERVER_IP = '192.53.174.102'  # Replace with your SA-MP server's IP address
SERVER_PORT = 28715  # Replace with your SA-MP server's port
PLAYER_NAME = 'Moro_Dev'
PASSWORD = 'mamababa15'

def send_packet(sock, packet):
    sock.send(packet.encode())

def receive_packet(sock):
    return sock.recv(4096).decode()

def login_fake_player():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_IP, SERVER_PORT))

    # Send the login request packet
    login_packet = f'{PLAYER_NAME}\n{PASSWORD}\n'.encode()
    send_packet(sock, login_packet)

    # Receive the response packet
    response_packet = receive_packet(sock)

    if 'Login successful' in response_packet:
        print(f'Player {PLAYER_NAME} logged in successfully.')
    else:
        print(f'Failed to log in player {PLAYER_NAME}. Error: {response_packet}')

    # Close the socket connection
    sock.close()

# Log in the fake player
login_fake_player()

# Simulate the fake player's actions
while True:
    # Perform various actions here (e.g., sending commands to the server)
    # ...

    # Pause for a certain duration before performing the next action
    time.sleep(5)  # Adjust the duration as needed
