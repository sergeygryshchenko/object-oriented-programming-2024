from socket import *

class TCommunicator:
    def __init__(self, r_host, r_port, s_host, s_port):
        self.r_host = r_host
        self.r_port = r_port
        self.s_host = s_host
        self.s_port = s_port
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.bind((self.r_host, self.r_port))
        self.ready = True
        

    def send(self, msg):
        try:
            if self.ready:
                self.sock.sendto(msg.encode('utf-8'), (self.s_host, self.s_port))
                print("Message sent successfully")
        except OSError as e:
            print("Error sending message:", e)

    def receive(self):
        try:
            data, addr = self.sock.recvfrom(1024)
            print("Received message:", data.decode('utf-8'))
            return data.decode('utf-8')
        except OSError as e:
            print("Error receiving message:", e)
            return None
