import socket
tcp = socket.socket(socket.AF_INET,socket.sock_STREAM)
tcp.connect(('10.0.2.6.9',9090))
tcp.sendall(b"www.google.com")
tcp.close()
