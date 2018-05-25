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
        bucket_name = 'multiserverbucketrololo'

        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        username = str(self.data)
        username = username[2:]
        username = username[:-1]
        print("{} wrote:".format(self.client_address[0]) + " " + username)

        # Once we got the username (data is in Bytes) we now do things here
        os.system("instagram-scraper " + username + " -u usernam -p paswd -t image --media-metadata -d "+ os.getcwd())

        # Uploads the given file using a managed uploader, which will split up large
        # files automatically and upload parts in parallel.
        filename = os.getcwd()+"/"+username+".json"

        jsonfile = username+".json"
        s3.upload_file(jsonfile, bucket_name, jsonfile, ExtraArgs={'ACL':'public-read'})

        url = "https://s3-eu-west-1.amazonaws.com/multiserverbucketrololo/"+username+".json"
        # TODO generate URL (normally = bucketURL + filename)
        # TODO example: https://s3-eu-west-1.amazonaws.com/multiserverbucketrololo/file.txt

        # for deleting files:
        # TODO remove local Json with this:
        os.remove(filename)


        # Reeturn whadever
        data = bytearray(url, 'utf8')
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

