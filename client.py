import socket, time
from caesarcipher import CaesarCipher


class Client:
    def __init__(self, host, port):
        self.server_host = host
        self.server_port = port
        self.server_addr = (self.server_host, self.server_port)
        self.format = "utf-8"
        self.header_size = 20
        self.Run()

    def WearHeader(self, msg):
        header = f"{len(msg):<{self.header_size}}"
        return header + msg

    def Send(self, conn):
        while True:
            msg = input("Enter message: ")
            msg = self.WearHeader(msg)
            msg = msg.encode(self.format)
            conn.send(msg)

    def Run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(self.server_addr)
            print(f"You connect {self.server_addr}")
            while True:
                self.Send(s)


client = Client("localhost", 5050)