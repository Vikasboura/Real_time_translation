import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os
import time

# --- Configuration ---
YOUR_LANGUAGE = "hi"  # Hindi
YOUR_LANGUAGE_CODE = "hi-IN"
MEETING_LANGUAGE = "en" # English
MEETING_LANGUAGE_CODE = "en-US"

def speak_text(text, lang):
    """Text ko audio mein badal kar bolta hai."""
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        filename = "temp_audio.mp3"
        tts.save(filename)
        print(f"🔊 Bol raha hoon: \"{text}\"")
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"Error: Aawaz play karte waqt galti hui - {e}")

def get_cable_output_index():
    """Virtual Cable ke 'Output' device ka index dhoondhta hai."""
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if "CABLE Output" in name:
            print(f"✅ Virtual Cable Output device Index {index} par mila.")
            return index
    print(" Error: 'CABLE Output (VB-Audio Virtual Cable)' device nahi mila.")
    return None

def translate_meeting_audio():
    """Meeting ki aawaz sunkar use translate karta hai."""
    recognizer = sr.Recognizer()
    cable_index = get_cable_output_index()
    if cable_index is None:
        return

    print("\n--- Meeting Translator Mode ---")
    print("🎧 Meeting ki aawaz sun raha hoon... (Band karne ke liye Ctrl+C dabayein)")
    
    while True:
        try:
            with sr.Microphone(device_index=cable_index) as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)
            
            print("Aawaz ko pehchan raha hoon...")
            text = recognizer.recognize_google(audio, language=MEETING_LANGUAGE_CODE)
            print(f"Meeting mein kaha gaya: \"{text}\"")

            translated_text = GoogleTranslator(source=MEETING_LANGUAGE, target=YOUR_LANGUAGE).translate(text)
            speak_text(translated_text, YOUR_LANGUAGE)

        except sr.UnknownValueError:
            print("...Aawaz samajh nahi aayi, dobara sun raha hoon.")
        except Exception as e:
            print(f"Ek galti hui: {e}")
            time.sleep(2)

def translate_my_voice():
    """Aapki aawaz sunkar use meeting ke liye translate karta hai."""
    recognizer = sr.Recognizer()
    print("\n--- My Voice Translator Mode ---")
    print("🎤 Aapki aawaz sun raha hoon... (Band karne ke liye Ctrl+C dabayein)")

    while True:
        try:
            with sr.Microphone() as source: # Aapka default microphone
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("\nAb boliye...")
                audio = recognizer.listen(source)
            
            print("🔍 Aapki aawaz ko pehchan raha hoon...")
            text = recognizer.recognize_google(audio, language=YOUR_LANGUAGE_CODE)
            print(f"Aapne kaha: \"{text}\"")

            translated_text = GoogleTranslator(source=YOUR_LANGUAGE, target=MEETING_LANGUAGE).translate(text)
            speak_text(translated_text, MEETING_LANGUAGE)

        except sr.UnknownValueError:
            print("...Aawaz samajh nahi aayi, dobara sun raha hoon.")
        except Exception as e:
            print(f"Ek galti hui: {e}")
            time.sleep(2)

if __name__ == "__main__":
    while True:
        print("\n--- Real-Time Translator ---")
        print("1. Meeting ki aawaz ko translate karein (Listen to Meeting)")
        print("2. Apni aawaz ko translate karein (Speak to Meeting)")
        print("3. Bahar niklein (Exit)")
        choice = input("Apna vikalp chunein (1, 2, ya 3): ")

        if choice == '1':
            print("\nSetup: Apne Zoom/Meet ke Speaker ko 'CABLE Input' par set karein.")
            time.sleep(3)
            translate_meeting_audio()
        elif choice == '2':
            print("\nSetup: Apne default microphone mein bolein.")
            time.sleep(3)
            translate_my_voice()
        elif choice == '3':
            break
        else:
            print("Galat vikalp. Kripya 1, 2, ya 3 chunein.")
