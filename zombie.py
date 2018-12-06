#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket


# ==========================================================

RHOST = 'localhost'
RPROT = 1337
RADDR = RHOST, RPROT

DEBUG = True

def main():

    while True:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect_ex(RADDR)

        while True:

            data = s.recv(1024)
            data = data.decode('utf-8')
            if DEBUG: print("[DEBUG] {}".format(data))
            if data == 'quit':
                break

        s.shutdown(socket.SHUT_RDWR)
        s.close()
        break

if __name__ == '__main__':
    main()