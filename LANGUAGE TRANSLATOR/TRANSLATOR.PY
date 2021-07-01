from google_trans_new import google_translator
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
translator = google_translator()
input_lang = 'en'
output_lang = 'hi'
try:
    with sr.Microphone() as source:
        print('Speak Now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)
except:
    pass

translated = translator.translate(text, lang_src=input_lang, lang_tgt=output_lang)
print(translated)

# converted_audio = gtts.gTTS(translated.text, lang=output_lang)
# converted_audio.save('romantic.mp3')
# playsound.playsound('romantic.mp3')
# print(googletrans.LANGUAGES)