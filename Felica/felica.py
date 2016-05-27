#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/pi/nfcpy/')
import binascii
import nfc
import time

def connected(tag):
    # タグのIDなどを出力する
    # print(tag)
    res = binascii.b2a_hex(tag.idm)
    # res = str(tag.idm).encode("hex")
    print "IDm=" + res

if __name__ == "__main__": 
    clf = nfc.ContactlessFrontend('usb')
    clf.connect(rdwr={'on-connect': connected})
    clf.close()