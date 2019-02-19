#!/usr/bin/env python3
# by William Hofferbert
# udp server.
# expects time.time() data and computes latency diff
import socket
import time

ip = "192.168.1.185"
port = 5005

# udp
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

def float_diff(comma_sep_float):
    arr = comma_sep_float.split(",")
    diff = float(arr[0]) - float(arr[1])
    return diff

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data_time = "%.6f" % time.time()
    if data:
        diff_str = data_time + "," + data.decode('utf-8')
        diff_calc = float_diff(diff_str) * 1000

        sent = sock.sendto(data_time.encode('utf-8'), addr)

        out = str(addr) + "\t" + str(diff_calc) + " ms"
        print(out)
    
