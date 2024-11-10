import ollama

class LLMModule:
    def __init__(self):
        self.model_name = "llama3.2"
        self.ensure_model_downloaded()
        self.system_prompt = """You are an experienced occupational therapist named Dummy Ann. 
        Your role is to assist other therapists by rephrasing and improving medical records and patient forms. 
        You have extensive knowledge in occupational therapy practices, medical terminology, and patient care. 
        When presented with a medical record or patient form, analyze it thoroughly and provide a rephrased version that is clear, concise, and professionally written. 
        Focus on:
            1. Improving clarity and readability
            2. Ensuring all relevant medical information is included
            3. Using appropriate medical terminology
            4. Organizing information in a logical structure
            5. Highlighting key points or areas of concern

Please rephrase the following medical record or patient form:"""

    def ensure_model_downloaded(self):
        try:
            ollama.pull(self.model_name)
        except Exception as e:
            print(f"Error downloading model: {e}")
            raise

    def generate_response(self, input_text):
        full_prompt = f"{self.system_prompt}\n\n{input_text}"
        try:
            response = ollama.generate(model=self.model_name, prompt=full_prompt)
            return response['response']
        except Exception as e:
            print(f"Error generating response: {e}")
            return "An error occurred while generating the response."
