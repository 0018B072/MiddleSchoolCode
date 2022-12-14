# chat_server.py
import sys
import socket
import select
import datetime
import random

HOST = '' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 9009

def chat_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)
 
    print "Chat server started on port " + str(PORT)
	

password = ()

tday = datetime.date.today()

a = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 
			'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l'
			, 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 
			'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X',
			'x', 'Y', 'y', 'Z', 'z']
rand_items = random.sample(a, 10)



if tday.day / 3 != float():
	print("New Password: ", rand_items)
	password = rand_items
elif tday.day / 3 == float():
	password = rand_items
else:
	print("error")
 
while 1:

        # get the list sockets which are ready to be read through select
        # 4th arg, time_out  = 0 : poll and never block
			ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
			for sock in ready_to_read:
            # a new connection request recieved
			
				if sock == server_socket: 
					print("Please Enter Password:\n")
					if input != password:
						print("incorrect!")
					elif input == password:
						sockfd, addr = server_socket.accept()
						SOCKET_LIST.append(sockfd)
						print "Client (%s, %s) connected" % addr
						broadcast(server_socket, sockfd, "[%s:%s] entered our chatting room\n" % addr)
			
            # a message from a client, not a new connection
			else:
                # process data recieved from client, 
				try:
                    # receiving data from the socket.
					data = sock.recv(RECV_BUFFER)
					if data:
                        # there is something in the socket
						broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)  
					else:
                        # remove the socket that's broken    
						if sock in SOCKET_LIST:
							SOCKET_LIST.remove(sock)

                        # at this stage, no data means probably the connection has been broken
						broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr) 

                # exception 
				

						server_socket.close()
    
# broadcast chat messages to all connected clients
				def broadcast (server_socket, sock, message):
					for socket in SOCKET_LIST:
        # send the message only to peer
						if socket != server_socket and socket != sock :
							try :
								socket.send(message)
							except :
                # broken socket connection
							socket.close()
                # broken socket, remove it
								if socket in SOCKET_LIST:
								SOCKET_LIST.remove(socket)
 
if __name__ == "__main__":

    sys.exit(chat_server())     