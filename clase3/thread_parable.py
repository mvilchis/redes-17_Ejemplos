from threading import Thread
from SimpleXMLRPCServer import SimpleXMLRPCServer

class WebServiceServer(Thread):
    def __init__(self, ip, port):
        super(WebServiceServer, self).__init__()
        self.running = True
        self.server = SimpleXMLRPCServer((ip, port))
        self.server.register_introspection_functions()

    def register_function(self, function):
        self.server.register_function(function)

    def run(self):
        self.server.serve_forever()

    def stop_server(self):
        self.server.shutdown()
        self.server.server_close()

print("starting server")
webService = WebServiceServer("localhost", 8010)
webService.start()
print("stopping server")
webService.stop_server()
webService.join()
print("server stopped")
