#!/usr/bin/env python3
# by William Hofferbert
# talks to the server, gives time.time(), 
# gets cvs of server time.time()
# diff them
import socket
import sys
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "192.168.1.185"
port = 5005

def float_diff(comma_sep_float):
    arr = comma_sep_float.split(",")
    diff = float(arr[0]) - float(arr[1])
    return diff

while True:
    # Send data
    message = "%.6f" % time.time()
    sent = sock.sendto(message.encode('utf-8'), (ip, port))

    # Receive response
    data, server = sock.recvfrom(4096)
    recv_time = "%.6f" % time.time()
    one_way_diff = float_diff(data.decode('utf-8')) * 1000

    total_str = recv_time + "," + message
    total_diff = float_diff(total_str) * 1000

    out = "one way = " + str(one_way_diff) + " ms\ttotal rtt = " + str(total_diff) + " ms"
    print (out)

