import speech_recognition as sr

import time
from clapDetector import ClapDetector, printDeviceInfo

#function that figures out what the user is saying using Google Speech Recognition
def getVoice():
    # Create a recognizer object
    r = sr.Recognizer()
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        # Recognize speech using Google Speech Recognition
        print("processing speech...")
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "cannot understand audio error"
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return "could not request results from service error"

#initialisation text to let the user know some info before starting
print("""
      --------------------------------
      The application initially attempts to use the system's default audio device. If this doesn't work or if you prefer to use a different device, you can change it. Below are the available audio devices. Find the one you are using and change the 'inputDevice' variable to the name or index of your preferred audio device. Then, restart the program, and it should properly capture audio.
      --------------------------------
      """)
printDeviceInfo()

#settings for clap detector
thresholdBias = 6000
lowcut=200               #< increase this to make claps detection more strict 
highcut=3200             #< decrease this to make claps detection more strict
clapDetector = ClapDetector(inputDevice=-1, logLevel=10)
clapDetector.initAudio()

#regular variables
lastPhrase = ""

try:
   while True:
      audioData = clapDetector.getAudio()

      result = clapDetector.run(thresholdBias=thresholdBias, lowcut=lowcut, highcut=highcut, audioData=audioData)
      resultLength = len(result)
      if resultLength > 0:
            lastPhrase=getVoice()
            if "exit" == lastPhrase or "stop" == lastPhrase or "exit stop" == lastPhrase or "stop exit" == lastPhrase:
                break
      time.sleep(1/60)

except KeyboardInterrupt:
    print("Exited gracefully")
except Exception as e:
    print(f"error: {e}")
finally:
    clapDetector.stop()
