"""
Script to generate monologue/dialogue passages with questions
"""


from google import genai
from google.genai import types
import time

from services.utils import *
from services.constants import *

client = genai.Client(api_key=APIKEY)

def generate(prompt, max_tokens=1280):
    retry_limit = 3
    for attempt in range(retry_limit):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=prompt, config=types.GenerateContentConfig(temperature=0.7, max_output_tokens=max_tokens)
            )
            return process_json_output(response.text)
        except:
            print("Request failed. Retrying...")
            if attempt != retry_limit-1:
                time.sleep(10) # wait 10 seconds before sending another request to Gemini
            continue
    return False

def generate_monologue():
    """Generate a monologue and its comprehension questions."""
    prompt = MONOLOGUE_PROMPT
    return generate(prompt)

def generate_dialogue():
    """Generate a dialogue and its comprehension questions."""
    prompt = DIALOGUE_PROMPT
    return generate(prompt)

# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# from config import *

# data = generate_monologue()
# with open(f"{TEXT_OUTPUT_DIR}monologue0.txt", "w") as f:
#     f.write(data)

# data = generate_dialogue()
# with open(f"{TEXT_OUTPUT_DIR}dialogue0.txt", "w") as f:
#     f.write(data)