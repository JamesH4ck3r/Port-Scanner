import os
import socket

s=socket.socket()
ip=input("Enter Target IP: ")
port=input("Enter Target Port: ")
for i in range(0, 65535):
  if (s.connect_ex((ip, port))==0):
      print("Port",i,"Is Open")
     
