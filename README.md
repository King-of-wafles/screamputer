# screamputer
An application designed to be a simple computer operating system that interfaces entirely by voice

It is planned to be integrated into a custom OS based on Debian that boots into a custom UI that launches some pre-made applications.

Development goals:

- custom home menu that can open a variety of applications with voice
- some kind of game application
- weather application to check the weather
- a notes app
- calculator
- basic or other programming language writing with voice (sounds like a terrible idea, let's do it!)

All these apps should be able to be used entirely with voice, requiring no human interface devices. This is not a practical thing, it is simply a stupid idea that I think would be funny.

Progress so far:
- listening function can detect what the user says through processing the microphone input with Google Speech Recognition
- clap detector that runs the listening function when you clap
- listening function ends the program when you say a phrase with "stop" or "exit". I may change this in the future to only make it so it activates when the word is said in isolation to prevent accidental shutdowns later on
