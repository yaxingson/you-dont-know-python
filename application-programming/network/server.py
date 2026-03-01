from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from socketserver import TCPServer, StreamRequestHandler
from time import ctime

ADDR = ('localhost', 9528)
BUFSIZE = 1024

class TcpServer:
  def __init__(self):
    self.sock = socket(AF_INET, SOCK_STREAM)
    self.sock.bind(ADDR)
    self.sock.listen(5)

  def run(self):
    try:
      while True:
        print('waiting for connection ^_^')
        sock, addr = self.sock.accept()
        print(addr)
        while True:
          content = sock.recv(BUFSIZE).decode()
          if content == 'bye' or not content:
            break
          sock.send(f'[{ctime()}]: {content}'.encode())
        sock.close()
    except (EOFError, KeyboardInterrupt):
      self.sock.close()


class UdpServer:
  def __init__(self):
    self.sock = socket(AF_INET, SOCK_DGRAM)
    self.sock.bind(ADDR)

  def run(self):
    try:
      while True:
        byte_content, addr = self.sock.recvfrom(BUFSIZE)
        content = str(byte_content)
        print(addr)
        if not content or str(content) == 'bye':
          break
        self.sock.sendto(f'{content[::-1]}'.encode(), addr)
    except (EOFError, KeyboardInterrupt):
      self.sock.close()


class TranslateRequestHandler(StreamRequestHandler):
  def handle(self):
    print('waiting for connection ...')
    print(self.client_address)
    content = self.rfile.readline().decode()
    self.wfile.write(f''.encode())


def createTcpServer():
  return TCPServer(ADDR, TranslateRequestHandler)

if __name__ == '__main__':
  # TcpServer().run()
  # UdpServer().run()
  createTcpServer().serve_forever()

