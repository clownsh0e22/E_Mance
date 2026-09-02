# P2P Mesh Routing Layer with Peer Discovery and Gossip
import socket
import threading
import json
import time

class MeshNode:
    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port
        self.peers = set()
        self.running = True
        self.server_socket = None

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Mesh node listening on {self.host}:{self.port}")

        while self.running:
            try:
                self.server_socket.settimeout(1.0)
                client_sock, addr = self.server_socket.accept()
                threading.Thread(target=self.handle_peer, args=(client_sock, addr), daemon=True).start()
            except socket.timeout:
                continue
            except Exception:
                break

    def handle_peer(self, client_sock, addr):
        try:
            data = client_sock.recv(4096)
            if data:
                message = json.loads(data.decode('utf-8'))
                print(f"Received message from {addr}: {message}")
        except Exception as e:
            print(f"Error handling peer {addr}: {e}")
        finally:
            client_sock.close()

    def send_message(self, peer_host, peer_port, message):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((peer_host, peer_port))
            s.sendall(json.dumps(message).encode('utf-8'))
            s.close()
            print(f"Sent message to {peer_host}:{peer_port}")
        except Exception as e:
            print(f"Failed to send to {peer_host}:{peer_port}: {e}")

    def stop(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()

if __name__ == "__main__":
    node = MeshNode()
    server_thread = threading.Thread(target=node.start_server, daemon=True)
    server_thread.start()
    
    # Self-test transmission
    time.sleep(0.5)
    node.send_message('127.0.0.1', 8888, {"action": "ping", "payload": "mesh active"})
    time.sleep(1)
    node.stop()
