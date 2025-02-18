"""NON-FASTAPI implementation for testing"""

from services.constants import *
from services.passage_gen import generate_monologue, generate_dialogue
from services.audio_gen import synthesize_monologue, synthesize_dialogue
from config import *
from services.utils import *

import json

def generate_test():
    """Generate a full listening test with multiple passages"""
    try:
        passages = []
        questions = []
        for i in range(NUM_MONOLOGUE):
            # data = generate_monologue()
            # with open(f"{TEXT_OUTPUT_DIR}monologue{i}.txt", "w") as f:
            #     f.write(data)
            with open(f"{TEXT_OUTPUT_DIR}monologue{i}.txt", "r") as f:
                data = f.read()
            data = json.loads(data, strict=False)
            audio_path = synthesize_monologue(data['text'], data['gender'], f"{AUDIO_OUTPUT_DIR}monologue{i}.wav")
            
            passages.append({
                "content": data,
                "audio_url": audio_path
            })
            
            questions.append(parse_questions(data, NUM_QUESTION_PER_PASSAGE))
        
        for i in range(NUM_DIALOGUE):
            # data = generate_dialogue()
            # with open(f"{TEXT_OUTPUT_DIR}dialogue{i}.txt", "w") as f:
            #     f.write(data)
            with open(f"{TEXT_OUTPUT_DIR}/dialogue{i}.txt", "r") as f:
                data = f.read()
            data = json.loads(data, strict=False)
            audio_path = synthesize_dialogue(data['dialogue'], f"{AUDIO_OUTPUT_DIR}dialogue{i}.wav")
            
            passages.append({
                "content": data,
                "audio_url": audio_path
            })
              
            questions.append(parse_questions(data, NUM_QUESTION_PER_PASSAGE))
              
        return {"passages": passages}
        
    except Exception as e:
        print(str(e))

print(json.dumps(generate_test(), indent=2))