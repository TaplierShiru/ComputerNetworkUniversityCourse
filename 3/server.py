from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler

authorizer = DummyAuthorizer()
authorizer.add_user("lokesh", "123", "T:/University/Сеть ЭВМ/Лабораторные", perm="elradfmw")
authorizer.add_anonymous("T:/University/Сеть ЭВМ/Лабораторные", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server=FTPServer(("localhost",8080),handler)
server.serve_forever()