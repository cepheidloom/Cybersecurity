import socket
tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp.bind(('10.0.2.69',9090))
tcp.listen()
conn,addr=tcp.accept()
with conn:
	print("connected",addr)
