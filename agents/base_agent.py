import os
from google import genai
from utils.logger import log_event

class BaseAgent:
    def __init__(self, name, role, instructions):
        self.name = name
        self.role = role
        self.instructions = instructions
        
        api_key = os.environ.get("GEMINI_API_KEY")

        if not api_key:
            log_event(self.name, "CRITICAL: No API Key found in Environment or .env")
            raise ValueError(f"Agent {self.name} is missing its API Key.")

        self.client = genai.Client(api_key=api_key)

    def execute(self, state_content):
        log_event(self.name, "Processing information...")
        
        full_prompt = (
            f"Persona: {self.role}\n"
            f"Instructions: {self.instructions}\n"
            f"Input Context: {state_content}"
        )
        
        
        models_to_try = ['gemini-2.5-flash', 'gemini-2.0-flash']
        
        for model_name in models_to_try:
            try:
                response = self.client.models.generate_content(
                    model=model_name, 
                    contents=full_prompt
                )
                
                if response and response.text:
                    log_event(self.name, f"Task completed successfully using {model_name}.")
                    return response.text
            except Exception as e:
                if "404" in str(e):
                    log_event(self.name, f"Model {model_name} not found, trying next...")
                    continue
                log_event(self.name, f"Error: {str(e)[:100]}")
                
        return f"Agent {self.name} failed: No compatible models found."