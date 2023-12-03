import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator


r = sr.Recognizer() 
engine = pyttsx3.init()

languages = {"en": ["English", "en-US"], # English
             "ja": ["Japanese", "ja-JP"], # Japanese
             "he": ["Hebrew", "he-IL"], # Hebrew
             "zh": ["Chinese", "zh-TW"], # Chinese
             "ar": ["Arabic", "ar-SA"]} # Arabic

fromLang = "he"
toLang = "ja"

def change_voice(language):
    for voice in engine.getProperty('voices'):
        if language in voice.name:
            engine.setProperty('voice', voice.id)

            return True


def speak_text(command, lang):
    change_voice(languages[lang][0])
    translated = GoogleTranslator(source='auto', target=lang).translate(command)
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


if __name__ == "__main__":
    speechText = get_speech(languages[fromLang][1])
    speak_text(speechText, toLang)