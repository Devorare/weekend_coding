#!/usr/bin/env python36

import socket
import json

def is_json(jsonexample):
    try:
        json_input = json.loads(jsonexample)
    except ValueError:
        return(b"Not JSON, sorry\n")
    return(b"JSON? Thanks!\n")

def main():
    port = 0
    r = range(1, 65535)

    while(int(port) not in r):
        port = (input("What port will we be listening on? : "))
        if(port.isdigit()):
            if(int(port) not in r):
                print("Invalid port.")
                port = 0
            else:
                port = int(port)
        else:
            print("Not digit")
            port = 0

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.bind(("127.0.0.1",port))

    mySocket.listen(1)
    
    while True:
        conn, addr = mySocket.accept()
        print("Connection from: " + str(addr))
        data = conn.recv(1024)
        test = data
        if not data:
            break
        else:
            conn.send(is_json(test))

main()
