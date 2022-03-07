from lark_parser import parse_speech
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please be silent while the speech recognizer does ambient noise calibration!")
    r.adjust_for_ambient_noise(source, 3)
    print("Say something!")
    audio = r.listen(source)

print("Converting audio to text...")
speech_text_output = None
# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    speech_text_output = r.recognize_google(audio)
    print(f"Google Speech Recognition thinks you said: '{speech_text_output}'")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

if speech_text_output:
    print("Parsing text...")
    try:
        code = parse_speech(speech_text_output)
        print(parse_speech(speech_text_output))

        fileName = input("What would you like to name your output?\n")
        with open(fileName + ".cpp", 'w') as f:
            f.write(code)
    except Exception as e:
        print(f"Error while parsing! {e}")