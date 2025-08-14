import speech_recognition as sr

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

getVoice()