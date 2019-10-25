#!/usr/bin/env python
import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Slim PyFTP Server configuration
ftpUser = 'slimpyftp'
ftpPassword = 'slimpyftp'
ftpBanner = 'Slim PyFTP Server'
ftpPort = 2121
ftpPassiveMin = 60000
ftpPassiveMax = 65535
ftpMaxConcurrentConnections = 256
ftpMaxConnectionsIP = 10

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user(ftpUser, ftpPassword, os.getcwd(), perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = ftpBanner
    handler.passive_ports = range(ftpPassiveMin, ftpPassiveMax)
    address = ('', ftpPort)
    server = FTPServer(address, handler)
    server.max_cons = ftpMaxConcurrentConnections
    server.max_cons_per_ip = ftpMaxConnectionsIP
    server.serve_forever()

if __name__ == '__main__':
    main()