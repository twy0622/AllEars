"""
Script to generate monologue/dialogue passages with questions
"""

from google import genai
from google.genai import types

import constants
import time
import json

client = genai.Client(api_key=constants.APIKEY)

def process_json_output(output: str):
    if output.startswith("```json"):
        output = output[7:]
    if output.endswith("```"):
        output = output[:-3]
    return output

def generate(prompt):
    retry_limit = 3
    for attempt in range(retry_limit):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=prompt, config=types.GenerateContentConfig(temperature=0.7, max_output_tokens=1024)
            )
            return process_json_output(response.text)
        except:
            print("Request failed. Retrying...")
            time.sleep(5) # wait 5 seconds before sending another request to Gemini
            continue
    return False

monologue = json.loads(generate(constants.MONOLOGUE_PROMPT))

# print(constants.GRADING_PROMPT.format(user_answer="test", expected_answer="test2"))