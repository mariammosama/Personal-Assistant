import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from gtts import gTTS
import pygame
import random
from googletrans import Translator

# Function to speak text
def speak(text, lang='ar'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.quit()
    os.remove("output.mp3")


# Function to listen to user input
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='ar')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


# Function to greet user
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("صباح الخير!")
    elif 12 <= hour < 18:
        speak("مساء الخير!")
    else:
        speak("مساء الخير!")
    speak("أنا فوزية مساعدتك الافتراضية\. كيف يمكنني مساعدتك؟")


# Function to open websites
def open_website(query):
    if 'افتح يوتيوب' in query:
        webbrowser.open("https://www.youtube.com")
    elif 'افتح جوجل' in query:
        webbrowser.open("https://www.google.com")
    elif 'افتح ستاك اوفر فلو' in query:
        webbrowser.open("https://stackoverflow.com")
    elif 'افتح تويتر' in query:
        webbrowser.open("https://www.twitter.com")
    elif 'افتح الفيسبوك' in query:
        webbrowser.open("https://www.facebook.com")
    elif 'افتح انستقرام' in query:
        webbrowser.open("https://www.instagram.com")
    elif 'افتح امازون' in query:
        webbrowser.open("https://www.amazon.com")
    elif 'افتح جيت هاب' in query:
        webbrowser.open("https://www.github.com")
    elif 'افتح لينكد ان' in query:
        webbrowser.open("https://www.linkedin.com")


# Function to search on Wikipedia
def wikipedia_search(query):
    speak("البحث في ويكيبيديا...")
    query = query.replace("ويكيبيديا", "")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("وفقًا لويكيبيديا")
        print(results)
        speak(results, lang='en')
    except wikipedia.exceptions.PageError as e:
        speak("عذرًا، لم أتمكن من العثور على نتائج في ويكيبيديا.")


# Function to open applications
def open_application(query):
    if 'افتح المفكره' in query:
        os.system("notepad.exe")
    elif 'افتح الاله الحاسبه' in query:
        os.system("calc.exe")
    elif 'افتح البريد الالكتروني' in query:
        os.system("start mailto:")
    elif 'افتح الوورد' in query:
        os.system("start winword")
    elif 'افتح الاكسل' in query:
        os.system("start excel")
    elif 'افتح باوربوينت' in query:
        os.system("start powerpnt")
    elif 'افتح الكاميرا' in query:
        os.system("start microsoft.windows.camera:")
    elif 'افتح فوتوشوب' in query:
        os.startfile("C:\\Program Files\\Adobe\\Adobe Photoshop 2021\\Photoshop.exe")
    elif 'افتح اليستريتور' in query:
        os.startfile(
            "C:\\Program Files\\Adobe\\Adobe Illustrator 2021\\Support Files\\Contents\\Windows\\Illustrator.exe")


# Function to play music
def play_quran():
    quran_dir = "D:\\Qura'an"
    quran = os.listdir(quran_dir)
    random_surah = random.choice(quran)
    os.startfile(os.path.join(quran_dir, random_surah))


def get_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"الوقت الآن هو {time}")


def get_date():
    date = datetime.datetime.now().strftime("%d-%m-%Y")
    speak(f"التاريخ اليوم هو {date}")


def search(query):
    if 'يوتيوب' in query:
        youtube_search(query)
    else:
        google_search(query)


def youtube_search(query):
    speak("البحث على يوتيوب...")
    query = query.replace("ابحث على يوتيوب عن", "")
    query = query.replace("ابحث في يوتيوب عن", "")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")


def google_search(query):
    query = query.replace("ابحث عن", "")
    query = query.replace("على الانترنت", "")
    webbrowser.open(f"https://www.google.com/search?q={query}")


def translate_to_english(query):
    translator = Translator()
    query = query.replace("ترجم إلى الإنجليزية", "").strip()
    query = query.replace("ترجم", "").strip()
    try:
        translation = translator.translate(query, src='ar', dest='en')
        translated_text = translation.text
        speak("الترجمة إلى الإنجليزية هي:")
        print(translated_text)
        speak(translated_text, lang='en')
    except Exception as e:
        speak("عذرًا، حدث خطأ أثناء الترجمة.")
        print(e)


greetings = ["مرحبا", "مرحبًا", "هلا", "أهلا"]
responses = ["مرحباً، كيف يمكنني مساعدتك؟", "مرحبًا، أنا هنا للمساعدة، كيف يمكنني خدمتك؟"]

# Main function
if __name__ == "__main__":
    greet()
    while True:
        query = listen().lower()

        query = query.replace("فوزية", "")
        query = query.replace("فوزيه", "").strip()

        if any(word in query for word in greetings):
            speak(random.choice(responses))

        elif 'شكرا' in query:
            speak("أنا في خدمتك دائما.")

        elif 'كيف حالك' in query or 'كيفك' in query:
            speak("أنا بخير، شكراً لسؤالك.")

        elif 'ويكيبيديا' in query:
            wikipedia_search(query)

        elif 'افتح' in query:
            open_website(query)
            open_application(query)

        elif 'الوقت' in query:
            get_time()

        elif 'التاريخ' in query or 'تاريخ' in query:
            get_date()

        elif 'ابحث' in query:
            search(query)

        elif 'قران' in query:
            play_quran()

        elif 'ترجم' in query:
            translate_to_english(query)

        elif 'وداعا' in query or 'مع السلامه' in query:
            speak("وداعاً!")
            break

        elif 'يلا غوري' in query:
            speak("غور انت كمان!")
            break

        else:
            speak("آسفة، لم أفهم ذلك.")