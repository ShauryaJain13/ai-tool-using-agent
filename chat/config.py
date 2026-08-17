from dotenv import load_dotenv
from groq import Groq
import os


class Configuration:
    """
    This class creates a connection between the LLM and the Agent,
    so that the user can communicate with the model
    """

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPEN_API_KEY')
        self.client = Groq(api_key=self.api_key)
        self.model_name = os.getenv('MODEL')
