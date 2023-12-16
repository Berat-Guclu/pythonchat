import socket
import threading

HEADER = 64
PORT = 13277
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
EXIT_COMMAND = "exit!"
KILL = "kill//"

RUNNING = True

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []


def handle_client(conn, addr):
 print(f"New Connection {addr}")
 clients.append(conn)


 while True:
        try:

            msg = conn.recv(HEADER).decode(FORMAT)

            print(f"{msg}")
            broadcast(msg, conn)
            if msg == EXIT_COMMAND:
                clientterminator(conn, clients)

                connected = False
                break
        except Exception as e:
            print(f"Error handling message from {addr}: {e}")

            break

 return 0
def clientterminator(conn, clients):
    conn.close()
    if conn in clients:
        clients.remove(conn)
    print(f"Number of active connections: {len(clients)}")


def broadcast(msg, sender_conn):
    for client in clients:
        try:
            if client != sender_conn and client.fileno() != -1:
                client.send(msg.encode(FORMAT))
            else:
              pass
        except socket.error as e:
            print(f"Error broadcasting to a client: {e}")
            clients.remove(client)


def adminp():
 while True:
    msg = input()
    if msg == "kill//":
        broadcast(msg,server)
    else:
        broadcast(msg,server)

def start():
    server.listen(15)
    print(f"Server listening on: {ADDR}")
    thread2 = threading.Thread(target=adminp, args=())
    thread2.start()

    while RUNNING:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"ACTIVE CONNECTIONS {threading.activeCount() - 1}")

print("Server Starting...")
start()
