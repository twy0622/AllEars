"""NON-FASTAPI implementation for testing"""

from services.constants import *
from services.passage_gen import generate, generate_monologue, generate_dialogue
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
            #* Generate
            # data = generate_monologue()
            # with open(f"{TEXT_OUTPUT_DIR}monologue{i}.txt", "w") as f:
            #     f.write(data)
            
            #* Read
            with open(f"{TEXT_OUTPUT_DIR}monologue{i}.txt", "r") as f:
                data = f.read()
            
            data = json.loads(data, strict=False)
            audio_path = synthesize_monologue(data['text'], data['gender'], f"{AUDIO_OUTPUT_DIR}monologue{i}.wav")
            
            passages.append({
                "type": "monologue",
                "topic": data['topic'],
                "content": data['text'],
                "audio_url": audio_path,
                "questions": parse_questions(data, NUM_QUESTION_PER_PASSAGE)
            })
        
        for i in range(NUM_DIALOGUE):
            #* Generate
            # data = generate_dialogue()
            # with open(f"{TEXT_OUTPUT_DIR}dialogue{i}.txt", "w") as f:
            #     f.write(data)
            
            #* Read
            with open(f"{TEXT_OUTPUT_DIR}/dialogue{i}.txt", "r") as f:
                data = f.read()
            
            data = json.loads(data, strict=False)
            audio_path = synthesize_dialogue(data['dialogue'], f"{AUDIO_OUTPUT_DIR}dialogue{i}.wav")
            
            passages.append({
                "type": "dialogue",
                "topic": data['scenario'],
                "content": data['dialogue'],
                "audio_url": audio_path,
                "questions": parse_questions(data, NUM_QUESTION_PER_PASSAGE)
            })
              
        return { "passages": passages }
        
    except Exception as e:
        print(f"Error: {str(e)}")

def grade_subjective(user_answer: str, expected_answer: str, question_text: str, passage_text: str):
    grading_input = GRADING_PROMPT.format(
        passage_text=passage_text,
        question5_text=question_text,
        expected_answer=expected_answer,
        user_answer=user_answer
    )
    response = generate(grading_input, 512)
    # grading_result = json.loads(response.text, strict=False)
    return response

#! generate_test() output
# print(json.dumps(generate_test(), indent=2))

#! grade_subjective output
with open(f"{TEXT_OUTPUT_DIR}/dialogue0.txt", "r") as f:
    data = f.read()
data = json.loads(data, strict=False)

print(grade_subjective(
    user_answer="It is more cost-effective, and provides quicker results.",
    expected_answer=data['question5']['expected_answer'],
    question_text=data['question5']['question'],
    passage_text=data['dialogue']
))

# user_answer="It is more cost-effective, and provides quicker results."
# expected_answer=data['question5']['expected_answer']
# question_text=data['question5']['question']
# passage_text=data['dialogue']