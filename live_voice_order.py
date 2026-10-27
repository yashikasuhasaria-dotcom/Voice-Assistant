import speech_recognition as sr
import sounddevice as sd

recognizer = sr.Recognizer()

sample_rate = 16000;
duration = 7

print("canteen voice ordeing system")
print("speak your order..\n")

audio=sd.rec(
    int(duration*sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype='int16')
sd. wait

print("Recording completed")
print("Transcribing")

audio_data=sr.AudioData(audio.tobytes(), sample_rate, 2)



try:
    text = recognizer.recognize_google(audio_data, language="en-IN")
    PRINT("\n.......CANTEEN ORDER.........")
    print("Your Order: ", text)
    print(text)
except sr.UnknownValueError:
    print("Couldnot understand your order")
except sr.RequestError:
    print("Google service error.", e)
    