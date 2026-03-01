from wx import App, Frame, Panel

class ChatBoxFrame(Frame):
  def __init__(self, parent=None, id=-1, title=''):
    super().__init__(self, parent, id, title, size=(1150, 700))

    top = Panel(self)



    self.Layout()

class ChatBox(App):
  def OnInit(self):
    frame = ChatBoxFrame(title='chatbox')
    frame.Show(True)
    self.SetTopWindow(frame)
    return True

if __name__ == '__main__':
  app = ChatBox()
  app.MainLoop()
