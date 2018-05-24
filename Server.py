import socketserver
import os
import boto3

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # Create boto3 connection
        s3 = boto3.client('s3')
        filename = 'file.txt'
        bucket_name = 'multiserverbucketrololo'

        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]) + " " + str(self.data))

        # Once we got the username (data is in Bytes) we now do things here
        # TODO do things and get local JSON

        # Uploads the given file using a managed uploader, which will split up large
        # files automatically and upload parts in parallel.
        s3.upload_file(filename, bucket_name, filename)
        # TODO generate URL (normally = bucketURL + filename)
        # TODO example: https://s3-eu-west-1.amazonaws.com/multiserverbucketrololo/file.txt

        # for deleting files:
        # TODO remove local Json with this:
        # os.remove("/tmp/<file_name>.txt")

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

