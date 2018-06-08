import socket # Sockets, duh.
import asyncore # Async socket handling.
import sys # For arguments.

banner = '''
 __   __        ____  
 \ \ / /__  ___|  _ \ 
  \ V / _ \/ __| | | |
   | |  __/\__ \ |_| |
   |_|\___||___/____/

	 "The Daemon that nobody asked for."

==========================================

Usage: python yesd.py [port] 
[port] Defaults to 8080.
'''

if len(sys.argv) < 2:
	port = 8080
else:
	port = int(sys.argv[1])

class Server(asyncore.dispatcher): # Serves all the clients.
	def __init__(self, host, port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind((host, port))
		self.listen(5)

	def handle_accept(self):
		sock, addr = self.accept()
		
		if sock is not None:
			sock.send("y\r\n")

def init():
	print(banner) # Banners are still hip right?
	server = Server('localhost', port)
	print("[*] Listening on port: " + str(port))
	asyncore.loop()

def main():
	init()

if __name__ == "__main__":
	main()
