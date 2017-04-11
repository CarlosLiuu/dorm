#!/usr/bin/python3
#-*- coding:utf-8 -*-
"""
Raspberry Pi serial receive and write to mysql
"""

import time
import sqlite3
import binascii
import serial

SER = serial.Serial('/dev/ttyUSB0', 115200, timeout=0, interCharTimeout=0.001)


class RecevData(object):
    """
    recevData
    """

    def __init__(self):
        self.messageType = 0
        self.devID = 0
        self.devName = 0
        self.devStatus = 0
        self.nRelays = 0
        self.router = 0
        self.data = 0
        self.relay = 0
        self.stop = 0

    def info_match(self, data):
        """
        Match infomation from receive message.

        Data Format:
        information type : 1 Byte (data[0])
        device ID : 2 Byte (data[1:3])
        reservation : 3 Byte (data[3:6])
        distance from terminal : 1 Byte (data[6])
        relay1 ~ relay5 : 1 Byte (data[7] ~ data[11])
        stop : 1 Byte (data[12])
        """
        if ((cmp(data[0], "\xf1") == 0) and
                (cmp(data[12], "\xfe") == 0)):
            # Upstream data
            back = data[1:3] + "FF"
            SER.write(back)
            self.messageType = data[0]
            self.devID = data[1:3]
            self.data = data[3:6]
            self.nRelays = data[6]
            self.stop = data[12]
            return True
        elif ((cmp(data[0], "\xf3") == 0) and
              (cmp(data[12], "\xfc") == 0)):
            # Ask for network
            # Send devID + 'FF' to device to comform received
            back = data[1:3] + "FF"
            SER.write(back)
            ptr = 0
            # Get the number of relays
            for i in data[7:12]:
                if i != '\xf6':
                    ptr = ptr + 1
            # Get infomation matched
            self.messageType = binascii.hexlify(data[0])
            self.devID = binascii.hexlify(data[1:3])
            self.devStatus = binascii.hexlify(data[3:6])
            self.relay = binascii.hexlify(data[7:12])
            # calcualte the router
            # replace data[7+ptr] with devID
            self.router = binascii.hexlify(
                data[7:7 + ptr] + data[4] + data[8 + ptr:12])
            if data[3] == '0':
                ans_f4_relay(data, ptr)
            else:
                ans_f4_dev(data)
            return True
        elif ((cmp(data[0], "\xf5") == 0) and
              (cmp(data[12], "\xfa") == 0)):
            # Reservation
            pass
        else:
            return False


def ans_f4_relay(data, ptr):
    """
    Answer \xf4 ... \xfb data to relay
    replace data[7:12] with router
    """
    back = "\xf4" + "FF" + data[3:6] + "\x07" + \
        data[7:7 + ptr] + data[4] + data[8 + ptr:12] + "\xfb"
    print('back:   ', binascii.hexlify(back))
    SER.write(back)
    return True


def ans_f4_dev(data):
    """
    Answer common f4
    """
    back = "\xf4" + "FF" + data[3:6] + "\x07" + data[7:12] + "\xfb"
    print('back:   ', binascii.hexlify(back))
    SER.write(back)
    return True


def read_serial(ser):
    """
    Read serial and write into db.sqlite3.
    """
    if ser.inWaiting() < 13:
        return False
    else:
        r_data = SER.readline()
        for i, temp_data in enumerate(r_data):
            if (temp_data == '\xf1') or (temp_data == '\xf3'):
                data = r_data[i:i + 13]
                print('receive:', binascii.hexlify(data))
                ser.flushInput()
                rec = RecevData()
                if rec.info_match(data) is True:
                    write_router_to_database(rec)
                    return True
            else:
                return False


def write_router_to_database(data):
    """
    Write data into database.
    """
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("insert into dormdb_dorm (devID,\
            devStatus,nRelays,relay,time)\
            values ('" + str(data.devID) +
                   "','" + str(data.devStatus) +
                   "','" + str(data.nRelays) +
                   "','" + str(data.relay) +
                   "',datetime('now','localtime'))")
    cursor.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    while True:
        read_serial(SER)
        time.sleep(0.0001)
