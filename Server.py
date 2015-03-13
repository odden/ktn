# -*- coding: utf-8 -*-
import SocketServer
from datetime import datetime
import threading
import json
import re

msg_history = []
active_users = []

class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    global active_users
    global msg_history

    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
        self.logged_in = False

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

    #sends 
    def send(self, data):
        self.request.sendall(json.dumps(data))

    #timestamp with date and hour:minute
    def timestamp(self):
        return str(datetime.now().strftime('%Y/%m/%d %H:%M'))

    #broadcasts data to all connected clients
    def broadcast(self, data):
        msg_history.append(data)

    def login(self, username):
        if not re.match('[A-Za-z0-9_]{2,}', username): #A-Z a-z 0-9
            send({'timestamp':timestamp(), 'sender':username, 'response':'error', 'content':'invalid username :('})
            return
        if not in active_users:
            self.username = username
            active_users.append(username)
            self.logged_in = True
            send({'timestamp':timestamp(), 'sender':self.username, 'response':'info', 'content':'login was successfull'})
            self.broadcast('<3 ' + self.username + ' joined AwzmChat<3.')
            history()
        else:
            send({'timestamp':timestamp(), 'sender':username, 'response':'error', 'content':'already logged in or name already taken :('})

    def logout(self):
        try:
            active_users.remove(self.username)
            self.logged_in = False
            self.send({'timestamp':timestamp(), 'sender':self.username, 'response':'info', 'content':'successfully logged out'})
            self.broadcast({'<3 ' + self.username + ' left AwzmChat<3.'})
        except Exception, e:
            send({'timestamp':timestamp(), 'sender':self.username, 'response':'error', 'content':'when not logged in you can only use the login and help request!'})

    #sends message history to users who just logged in
    def history(self):
        send({'timestamp':timestamp(), 'user':username, 'response':'history', 'content':msg_history})

    def disconnect(self):
        try:
            active_users.remove(self.username)
        except:
            pass

    def handle_data(self, data):
        decoded = json.loads(data)

        if decoded['request'] == 'login':
            self.login(decoded.get('username', ''))

        if not self.logged_in:
            return

        if decoded['request'] == 'logout':
            self.logout()

        if decoded['request'] == 'message':
            if decoded.get('message', '') != '':
                p = ' '*(len(max(active_users, key=len))-len(self.username))
                msg = self.timestamp() + p + ' %s| %s'%(self.username, decoded['message'])
                self.broadcast(msg)

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
