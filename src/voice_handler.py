# src/voice_handler.py
import speech_recognition as sr
import pyttsx3
import logging
from datetime import datetime

class VoiceHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.setup_logging()
    
    def setup_logging(self):
        logging.basicConfig(
            filename='logs/voice_handler.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                logging.info(f"Recognized: {text}")
                return text
            except Exception as e:
                logging.error(f"Error recognizing audio: {e}")
                return None
    
    def speak(self, text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
            logging.info(f"Spoke: {text}")
        except Exception as e:
            logging.error(f"Error speaking: {e}")
