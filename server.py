import socket


class Server:
    def __init__(self, host, port):
        self.server_host = "localhost"
        self.server_port = 5050
        self.server_addr = (self.server_host, self.server_port)
        self.format = "utf-8"
        self.header_size = 20
        self.Run()

    def TakeOffHeader(self, conn):
        header = conn.recv(self.header_size).decode(self.format)
        msg_size = int(header.strip())
        return msg_size

    def Recv(self, conn, addr):
        print(f"{addr} connect!")
        while conn:
            msg_size = self.TakeOffHeader(conn)
            msg = conn.recv(msg_size)
            if msg:
                msg = msg.decode(self.format)
                print(f"{addr} {msg}")
    
    def Run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(self.server_addr)
            s.listen()
            print("Server listening...")
    
            while True:
                conn, client_addr = s.accept()
                self.Recv(conn, client_addr)


server = Server("localhost", 5050)