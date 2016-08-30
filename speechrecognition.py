import speech_recognition as sr

class TalkToJarvis:

  def listening(self):
    try:
      while 1:
        r = sr.Recognizer()
        r.dynamic_energy_threshold = True
        with sr.Microphone() as source:               
          audio = r.listen(source)                  

        try:
          return r.recognize_google(audio)   
        except sr.UnknownValueError:                            
          return "waiting"
    except LookupError:
      pass

t2j = TalkToJarvis()      
print t2j.listening()        