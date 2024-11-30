# src/nlp_processor.py
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import logging

class NLPProcessor:
    def __init__(self):
        self.setup_nltk()
        self.setup_logging()
    
    def setup_nltk(self):
        try:
            nltk.download('punkt')
            nltk.download('stopwords')
            nltk.download('averaged_perceptron_tagger')
        except Exception as e:
            logging.error(f"Error setting up NLTK: {e}")
    
    def setup_logging(self):
        logging.basicConfig(
            filename='logs/nlp_processor.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def process_query(self, text):
        try:
            tokens = word_tokenize(text.lower())
            stop_words = set(stopwords.words('english'))
            filtered_tokens = [w for w in tokens if w not in stop_words]
            return filtered_tokens
        except Exception as e:
            logging.error(f"Error processing query: {e}")
            return []
