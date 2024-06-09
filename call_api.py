
import openai
from openai import OpenAI
from tqdm import tqdm
import re


client = OpenAI(api_key="", base_url="https://api.deepseek.com")

def call_model(input_prompt):
    try:
        response = client.chat.completions.create(
         model="deepseek-chat",
        messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},],
            stream=False,
            temperature=0.5,
            max_tokens=20,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Correctly extract the predicted answer
        predicted_answer = response.choices[0].message.content
        return predicted_answer
    except Exception as e:
        return f"An error occurred: {e}"
    
if __name__ == '__main__':
    call_model()
