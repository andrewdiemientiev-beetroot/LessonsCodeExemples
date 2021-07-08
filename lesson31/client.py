import socket

ip_addr = "127.0.0.1"
port = 8000
bite_chunk = 1024

# for server
file = open('', 'rb')
file.read(bite_chunk)

# for client
file = open('', 'wb')


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip_addr, port))
sock.send(b"hello world")
data = sock.recv(1024)
sock.close()
print(data.decode('utf-8'))
