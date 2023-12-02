import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator


r = sr.Recognizer() 
engine = pyttsx3.init()

languages = {"en": "en_US",
             "he": "he_IL",
             "zh": "zh-TW",
             "ar": "ar-SA"}


def change_voice(language):
    for voice in engine.getProperty('voices'):
        if language in voice.languages:
            engine.setProperty('voice', voice.id)

            return True


def speak_text(command, lang):
    change_voice(lang)
    translated = GoogleTranslator(source='auto', target=lang[:2]).translate(command)
    engine.say(translated) 
    engine.runAndWait()


def get_speech(lang):
    try:
         
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            audio2 = r.listen(source2)
             
            myText = r.recognize_google(audio2, language=lang)
            myText = myText.lower()
 
            print("Did you say ", myText)
            
            return myText
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")


speak_text(get_speech(languages["he"]), 'en')