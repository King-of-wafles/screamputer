import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    # Recognize speech using Google Speech Recognition
    text = r.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))