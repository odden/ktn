# -*- coding: utf-8 -*-
import socket
import threading
import json

class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.run()

        # TODO: Finish init process with necessary code


    def run(self):
        # Initiate the connection to the server
        #self.__init__()
        self.connection.connect((self.host, self.server_port))
        self.thread = threading.Thread(target = self.receive_message)
        self.thread.setDeamon(True)
        self.thread.start()

        print "Welcome to AwzmChat<3 write something awezome - aand be awezome."
        
        self.logged_in = False

        while not logged_in:
            self.username = raw_input('Username: ')
            self.login()
            resp = self.connection.recv(1024).strip()
            self.handle_json(resp)

        while logged_in:
            receive_message()

        self.connection.close()


    def login(self):
        self.send(self.parse({'request':'login', 'username':self.username}))
        logged_in = True

    def disconnect(self):
        # TODO: Handle disconnection
        self.send(self.parse({'request':'logout'}))

    def receive_message(self, message):
        # TODO: Handle incoming message
        while():
            received = self.connection.recv(1024).strip()
            self.process_json(received)            

    def send_payload(self, data):
        # TODO: Handle sending of a payload
        data = raw_input("Type something: ")
        self.connection.sendall(data)
        self.send(self.parse({'request':'msg', 'content':data }))

    def parse(self, data):
        return json.dumps(data)

    def handle_json(self, data):
        index = 0
        while data.find("{", index) >= 0:
            start = data.find("{", index)
            end = data.find("}", start)
            index = end
            self.handle_data(data[start:end+1])
    
    def handle_data(self, data):
        decoded = json.loads(data)
        if decoded.get("response", "") == "login":
            if decoded.get("error", "") != "":
                print decoded["error"], "(%s)"%decoded.get("username", "")
            else:
                self.logged_in = True
            if decoded.get("messages", "") != "":
                print decoded["messages"].encode('utf-8')

        if not self.logged_in:
            return
        
        if decoded.get("response", "") == "logout":
            self.logged_in = False

        if decoded.get("response", "") == "message":
            print decoded["message"].encode('utf-8')


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations is necessary
    """
    client = Client('localhost', 9998)
