import socket

# ip_addr = "0.0.0.0"
# ip_addr = "localhost"
ip_addr = "127.0.0.1"
port = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip_addr, port))
sock.listen(1)
conn, addr = sock.accept()
print(addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()
