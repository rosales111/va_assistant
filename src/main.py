# src/main.py
from voice_handler import VoiceHandler
from nlp_processor import NLPProcessor
from wake_word import WakeWordDetector
from response_generator import ResponseGenerator
import logging

class VeteransAssistant:
    def __init__(self):
        self.voice_handler = VoiceHandler()
        self.nlp_processor = NLPProcessor()
        self.wake_detector = WakeWordDetector()
        self.response_generator = ResponseGenerator()
        self.setup_logging()
    
    def setup_logging(self):
        logging.basicConfig(
            filename='logs/va_assistant.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def run(self):
        print("Veterans Voice Assistant is starting...")
        while True:
            try:
                text = self.voice_handler.listen()
                if text:
                    processed_text = self.nlp_processor.process_query(text)
                    response = self.response_generator.generate_response("default")
                    self.voice_handler.speak(response)
            except KeyboardInterrupt:
                print("Shutting down...")
                break
            except Exception as e:
                logging.error(f"Error in main loop: {e}")

if __name__ == "__main__":
    assistant = VeteransAssistant()
    assistant.run()
