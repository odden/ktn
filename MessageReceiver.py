# -*- coding: utf-8 -*-
from threading import Thread

class MessageReceiver(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and permits
    the chat client to both send and receive messages at the same time
    """

    def __init__(self, client, connection):
        """
        This method is executed when creating a new MessageReceiver object
        """

        # Flag to run thread as a deamon
        self.daemon = True
        self.listener = client
        self.connection = connection
        super(MessageReceiver, self).__init__()

        # TODO: Finish initialization of MessageReceiver


    def run(self):
        # TODO: Make MessageReceiver receive and handle payloads
        while True:
            data = self.connection.recv(1024).strip()
            if data:
                self.listener.message_received(data, self.connection)

