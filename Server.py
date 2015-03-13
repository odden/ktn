# -*- coding: utf-8 -*-
import SocketServer
from datetime import datetime
import threading
import json
import re


class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    active_users = []

    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request

        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096).strip()
            if received_string:
                print(received_string)
                self.handle_data(received_string)
            else:
                print('The client is disconnected.')
                break            
            # TODO: Add handling of received payload from client

    def send(self, data):
        self.request.sendall(json.dumps(data))

    def timestamp():
        return str(datetime.now())

    def login(self, username):
        if not re.match('[A-Za-z0-9_]{2,}', username): #A-Z a-z 0-9
            send({'timestamp':timestamp(), 'sender':username, 'response':'login', 'error':'invalid username'})
            return
        if not in active_users:
            send({'timestamp':timestamp(), 'sender':username, 'response':'login', 'info':'login was successfull'})
        else:
            send({'timestamp':timestamp(), 'sender':username, 'response':'login', 'error':'already logged in'})
        return

    def logout(self, username):
        if not in active_users:
            send({'timestamp':timestamp(), 'sender':username, 'response':'logout', 'error':'you suck'})
        else:
            send({'timestamp':timestamp(), 'sender':username, 'response':'logout', 'info':'successfully logged out'})

    def message():
        pass

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations is necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations is necessary
    """
    HOST, PORT = 'localhost', 9998
    print 'Server running...'

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
