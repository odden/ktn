# -*- coding: utf-8 -*-
import socket
import threading
import json

class Client:
    """
    This is the chat client class
    """

    def __init__(self):
        """
        This method is run when creating a new Client object
        """

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.run()

        # TODO: Finish init process with necessary code


    def run(self, host, server_port):
        # Initiate the connection to the server
        self.__init__()
        print "Welcome to AwzmChat<3 write something awezome"
        self.connection.connect((self.host, self.server_port))

        self.login = False

        while not login:
            self.username = raw_input('Username: ')
            self.login()

        self.threading = threading.Thread(target = self.receive_message)
        self.threading.setDeamon(True)
        self.threading.start()

        while login:
            


    def login(self):
        self.send(self.parse({'request':'login', 'username':self.username}))
        login = True

    def disconnect(self):
        # TODO: Handle disconnection
        self.send(self.parse({'request':'logout'}))

    def receive_message(self, message):
        # TODO: Handle incoming message
        while(login):
            data = raw_input()

            received = connection.recv(1024)
            self.send(self.parse({'request':'msg', 'content' }))
        pass

    def send_payload(self, data):
        # TODO: Handle sending of a payload
        self.connection.sendall(data)
        pass


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations is necessary
    """
    client = Client('localhost', 9998)
