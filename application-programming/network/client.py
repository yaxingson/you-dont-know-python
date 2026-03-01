from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
import tkinter as tk

ADDR = ('localhost', 9528)
BUFSIZE = 1024

class TcpClient:
  def __init__(self):
    self.sock = socket(AF_INET, SOCK_STREAM)
    self.sock.connect(ADDR)

  def run(self):    
    while True:
      send_content = input('> ')
      if not send_content or send_content == 'bye':
        break
      self.sock.send(send_content.encode())
      
      content = self.sock.recv(BUFSIZE).decode()
      print(content)

    self.sock.close()

class UdpClient:
  def __init__(self):
    self.sock = socket(AF_INET, SOCK_DGRAM)

  def run(self):
    while True:
      send_content = input('> ')
      if not send_content or send_content == 'bye':
        break
      self.sock.sendto(send_content.encode(), ADDR)

      content, addr = self.sock.recvfrom(BUFSIZE)
      print(content.decode())
      print(addr)

    self.sock.close()


class ChatRoom:
  def __init__(self):
    self.top = tk.Tk()
    tk.Entry(self.top).pack()

  def setup(self):
    self.top.mainloop()


if __name__ == '__main__':
  # TcpClient().run()
  UdpClient().run()
