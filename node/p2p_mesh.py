# P2P Mesh Routing Layer
import socket
import threading

def start_mesh_node(port=8888):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"Mesh node active on port {port}")

if __name__ == "__main__":
    start_mesh_node()
