import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator

class Translator:
    def __init__(self):
        self.recognizer = sr.Recognizer() 
        self.engine = pyttsx3.init()
        self.languages = {"English": ["en", "en-US"], # English
                    "Japanese": ["ja", "ja-JP"], # Japanese
                    "Hebrew": ["iw", "he-IL"], # Hebrew
                    "Chinese": ["zh-TW", "zh-TW"], # Chinese
                    "Arabic": ["ar", "ar-SA"]} # Arabic


    def change_voice(self, language):
        for voice in self.engine.getProperty('voices'):
            if language in voice.name:
                self.engine.setProperty('voice', voice.id)

                return True


    def speak_text(self, command, lang):
        translated = GoogleTranslator(source='auto', target=self.languages[lang][0]).translate(command)
        self.engine.say(translated) 
        self.engine.runAndWait()


    def get_speech(self, lang):
        try:
            with sr.Microphone() as source2:
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level 
                self.recognizer.adjust_for_ambient_noise(source2, duration=0.2)
                
                audio2 = self.recognizer.listen(source2)
                
                myText = self.recognizer.recognize_google(audio2, language=self.languages[lang][1])
                myText = myText.lower()
    
                print("Did you say ", myText)
                
                return myText
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")


if __name__ == "__main__":
    fromLang = "Hebrew"
    toLang = "English"

    trns = Translator()
    text = trns.get_speech(fromLang)
    trns.change_voice(toLang)    
    trns.speak_text(text, toLang)