import pyttsx3
import speech_recognition as sr
from PyDictionary import PyDictionary

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speaking(text):
    engine.say(text)
    engine.runAndWait()

def dictionary():
    speaking("Which word do you want to find:")
    try:
        with sr.Microphone() as source:
            print("Listening for the word...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
        query = recognizer.recognize_google(audio).lower()
        print(f"You said: {query}")
        dic = PyDictionary()
        word = dic.meaning(query)
        if word:
            for state in word:
                print(word[state])
                speaking("The meaning is " + ', '.join(word[state]))
        else:
            speaking("Sorry, I couldn't find the meaning of the word.")
    except sr.UnknownValueError:
        speaking("Sorry, I did not understand the audio.")
    except sr.RequestError as e:
        speaking(f"Could not request results; {e}")
    except Exception as e:
        speaking(f"Error: {e}")

if __name__ == "__main__":
    print("--------------------------- DICTONARY ASSISTANT----------------------------\n\n")
    print("""    1). It's a virtual Dictionary module.
    2). It's name is Jenny . You need to call Jenny Whenever you want to active it.\n\n""")
    speaking("Hello, My name is Jenny , how may I help you?")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

            word = recognizer.recognize_google(audio).lower()

            if word == "jenny":
                speaking("Yes?")
                dictionary()


        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
            speaking("Sorry, I did not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speaking(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")
            speaking(f"Error: {e}")
