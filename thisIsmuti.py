import socketserver
import time
import newProcesser

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]) + " " + str(self.data))

        # WAIT 5 SECONDS
        time.sleep(5)

        # Reeturn whadever
        data = b"http://www.This-Is-A-URL-lol.com/124141241412421412421/sjnsjfbsfah/helloworld"
        print("returning: " + str(data))
        self.request.sendall(data)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    print("Server listening...")

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()