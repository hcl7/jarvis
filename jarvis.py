import sys
import os
import speechrecognition

class jarvis:
  
  def __init__(self, file, cmd):
    self.file = file
    self.cmd = cmd
  
  # get the commands from data.txt file and puts into two lists.
  def getcmd(self):
    f = open(self.file, "r+")
    command = []
    answer = []
    for line in f:
      command.append(line[line.find("[")+1:line.find("]")])
      answer.append(line[line.find("]")+2:])
    f.close()
    tmp = ''
    for i in range(len(command)):
      if command[i] == self.cmd:
        tmp = answer[i]
    return tmp
  
  #get commands from data commands file  
  def getCmdBy(self, fromchar, tochar):
    f = open(self.file, "r+")
    command = []
    for line in f:
      command.append(line[line.find(fromchar)+1:line.find(tochar)])
    f.close()
    tmp = ''
    for i in range(len(command)):
      if command[i] == self.cmd:
        tmp = command[i]
    return tmp    

  # analize a voice command after is filtered
  def cmdAnalizeAfter(self, cmd, inputcmd):
    inputafter = 'none'
    for word in inputcmd:
      if word in cmd:
        inputafter = cmd.split(word)[1]
        break
    return inputafter.strip()
# end of jarvis class

# filter the voice command before it is used.
def cmdFilter(cmd, inputcmd):
  inputbefore = cmd
  for word in inputcmd:
    if word in cmd:
      inputbefore = cmd.split(word)[0] + word
      break
  return inputbefore

#main
def main():
  try:
    print "[+] Loading general commands!..."
    generalcmd = ['waiting', 'Jarvis', 'shut down', 'shutdown', 'how are you']
    print "[+] Loading input commands!..."
    inputcmd = ['about', 'into', 'Define', 'book']
    t2j = speechrecognition.TalkToJarvis()
    while True:
      #get voice command
      jcmd = t2j.listening()
      print "[+] Given command: " + jcmd
      #check if is there a input command on it
      jtmpcmd = cmdFilter(jcmd, inputcmd)
      #load the commands that will be executed
      jvs = jarvis("data.txt", jtmpcmd)
      cname = jvs.getcmd()
      if cname != '':
        #check for string after input command
        inputcommand = jvs.cmdAnalizeAfter(jcmd, inputcmd)
        print "[+] Input Command: " + inputcommand
        if inputcommand == 'none':
          os.system(cname)
          print "[*] " + cname
          if jcmd not in generalcmd:
            os.system('nircmd.exe speak text "running the command ' + jcmd + ', sir"')
          else:
            if (jcmd == 'shut down' or jcmd == 'shutdown'):
              sys.exit()
        else:
          #replace argumente %1 with string after input command
          runcmd = cname.replace('%1', inputcommand.replace(" ", "+"))
          os.system(runcmd)
          print "[*] " + runcmd
      else:
        os.system('nircmd.exe speak text "This Command is not in my list, sir"')
  except:
    print "[-] Stopping...!"
  finally:
    print "[-] Jarvis is shutting down!"
    
if __name__ == '__main__':
  main()