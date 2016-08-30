import sys
from Tkinter import *
from tkFileDialog import askopenfilename

class ScrolledText(Frame):
  def __init__(self, parent=None, text='', file=None):
    Frame.__init__(self, parent)
    self.pack(expand=YES, fill=BOTH)                 # make me expandable
    self.makewidgets()
    self.settext(text, file)
  def makewidgets(self):
    sbar = Scrollbar(self)
    text = Text(self, relief=SUNKEN)
    sbar.config(command=text.yview)                  # xlink sbar and text
    text.config(yscrollcommand=sbar.set)             # move one moves other
    sbar.pack(side=RIGHT, fill=Y)                    # pack first=clip last
    text.pack(side=LEFT, expand=YES, fill=BOTH)      # text clipped first
    self.text = text
  def settext(self, text='', file=None):
    if file: 
      text = open(file, 'rb').read()
      self.text.delete('1.0', END)                     # delete current text
      self.text.insert('1.0', text)                    # add at line 1, col 0
      self.text.mark_set(INSERT, '1.0')                # set insert cursor
      self.text.focus()                                # save user a click
  def gettext(self):                                   # returns a string
    return self.text.get("sel.first", "sel.last") 
  def quit(self):
    self.root.destroy() 
def main():
  try:
    root = Tk()
    st = ScrolledText(file=sys.argv[1])
    def show(event): print repr(st.gettext(text))            # show as raw string
    root.wm_iconbitmap(bitmap="pafap.ico")
    root.title(sys.argv[1])
    root.geometry(sys.argv[2])
    root.bind('<Key-Escape>', quit)
    root.mainloop()
  except:
    print "window.py file 700x200"
main()
