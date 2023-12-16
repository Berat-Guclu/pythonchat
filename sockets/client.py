import socket
import threading

HEADER = 64
PORT = 1235
SERVER = "localhost"
FORMAT = "utf-8"
EXIT_COMMAND = "exit!"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)

    client.send(message)

def receive():
    while True:
        try:
         msg = client.recv(1024).decode(FORMAT)

         print(msg)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()
uname=input("Your username")
send(f"Hello, I'm a new client! {uname}")

while True:
    msg = input()
    message = uname+": "+msg
    if msg == EXIT_COMMAND:
        send(message)
        client.close()
        break
    else:
        send(message)

client.close()
