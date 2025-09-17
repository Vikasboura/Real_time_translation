import sys
import json
import struct
import speech_recognition as sr
from googletrans import Translator
import logging
import os

# --- Logging Setup ---
# Yeh aapke user folder (C:/Users/vikas) mein ek log file banayega
log_file = os.path.join(os.path.expanduser("~"), "translator_host.log")
logging.basicConfig(filename=log_file, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# --- Communication Functions ---
def send_message(message):
    """Chrome extension ko message bhejta hai"""
    try:
        encoded_content = json.dumps(message).encode('utf-8')
        encoded_length = struct.pack('@I', len(encoded_content))
        
        sys.stdout.buffer.write(encoded_length)
        sys.stdout.buffer.write(encoded_content)
        sys.stdout.buffer.flush()
    except Exception as e:
        logging.error(f"FATAL: Message bhejte waqt error: {e}")

def read_message():
    """Chrome extension se message padhta hai"""
    try:
        raw_length = sys.stdin.buffer.read(4)
        if len(raw_length) == 0:
            return None # Connection band ho gaya
        
        message_length = struct.unpack('@I', raw_length)[0]
        message = sys.stdin.buffer.read(message_length).decode('utf-8')
        return json.loads(message)
    except Exception as e:
        logging.error(f"FATAL: Message padhte waqt error: {e}")
        return None

# --- Core Translation Logic ---
def perform_translation(config):
    """Audio sunkar, translate karke, subtitle bhejta hai"""
    recognizer = sr.Recognizer()
    # --- YEH LINE BADLI GAYI HAI ---
    translator = Translator(service_urls=['translate.google.com'])
    
    mic_index = config.get("meeting_audio_index")
    source_lang = config.get("meeting_language", "en-US")
    target_lang = config.get("your_language", "hi-IN")

    try:
        with sr.Microphone(device_index=mic_index) as source:
            send_message({"status": "info", "text": "Sun raha hoon..."})
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)

        # Step 1: Aawaz ko pehchane (Recognize speech)
        try:
            text = recognizer.recognize_google(audio, language=source_lang)
            send_message({"status": "recognized", "text": f"Suna: {text}"})
        except sr.UnknownValueError:
            send_message({"status": "info", "text": "Aawaz samajh nahi aayi."})
            return
        except sr.RequestError as e:
            raise Exception(f"Recognition service mein error: {e}")

        # Step 2: Text ko translate kare (Translate text)
        try:
            translation = translator.translate(text, src=source_lang.split('-')[0], dest=target_lang.split('-')[0])
            translated_text = translation.text
            send_message({"status": "translated", "text": translated_text})
        except Exception as e:
            # Yeh sabse zaroori hissa hai
            logging.error(f"Translation service fail ho gayi: {e}")
            send_message({"status": "error", "text": "Translation Failed! (Service may be down)"})
            return

    except Exception as e:
        error_message = f"Translation pipeline mein error: {e}"
        logging.error(error_message)
        send_message({"status": "error", "text": error_message})

# --- Main Application Loop ---
def main():
    logging.info("--- Native host shuru hua ---")
    while True:
        try:
            message = read_message()
            if message is None:
                logging.info("Chrome ne connection band kar diya.")
                break 
            
            if message.get("command") == "start":
                logging.info(f"Start command mila. Config: {message.get('config')}")
                perform_translation(message.get("config", {}))
        except Exception as e:
            logging.error(f"FATAL error in main loop: {e}")
            break
    
    logging.info("--- Native host band hua ---")

if __name__ == '__main__':
    main()

