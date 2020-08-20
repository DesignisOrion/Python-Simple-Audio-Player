# This app is called PyAudio, in which is a music player made in Python.

from pygame import mixer  # importing mixer from pygame framework

mixer.init()  # start the mixer

mixer.music.load("KBSC.mp3")  # Load the song
mixer.music.set_volume(0.7)  # set the volume
mixer.music.play()  # Play the mixer

while True:
    print("Press 'p' to pause 'r' to resume ")
    print("Press 'e' to exit the program")
    query = input(">>> ")

    if query == 'p':
        mixer.music.pause()  # Pause music
    elif query == 'r':
        mixer.music.unpause()  # Resume music
    elif query == 'e':
        mixer.music.stop()  # Stop the mixer
        break
