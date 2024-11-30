# src/response_generator.py
import yaml
import logging
from datetime import datetime

class ResponseGenerator:
    def __init__(self, response_file='config/responses.yml'):
        self.responses = self.load_responses(response_file)
        self.setup_logging()
    
    def setup_logging(self):
        logging.basicConfig(
            filename='logs/response_generator.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def load_responses(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return yaml.safe_load(file)
        except Exception as e:
            logging.error(f"Error loading responses: {e}")
            return {}
    
    def generate_response(self, intent, entities=None):
        try:
            if intent in self.responses:
                response = self.responses[intent]
                logging.info(f"Generated response for intent: {intent}")
                return response
            return "I'm sorry, I don't have information about that yet."
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return "I'm having trouble generating a response right now."
