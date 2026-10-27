import speech_recognition as sr

recognizer = sr.Recognizer()


with sr.AudioFile('Order.wav') as source:
   audio_data = recognizer.record(source)
print("transcribing...")

try:
    text = recognizer.recognize_google(audio_data)
    print("\nTranscription: ")
    print(text)
except sr.UnknownValueError:
    print("google speech recognition could not understand audio.")
except sr.RequestError:
    print("could not request results from google speech recognition service.")
    
