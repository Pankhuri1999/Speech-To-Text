# This code of for converting audio files to text.
with sr.AudioFile('Name of your audio file') as source:
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('Working on...')
        print(text)
    except:
        print('Sorry.. run again...')
