import uvicorn
from fastapi import FastAPI, HTTPException
from services.passage_gen import *
from services.audio_gen import synthesize_monologue, synthesize_dialogue
from config import *
from services.constants import *
import json

app = FastAPI(title="AllEars", version="1.0.0")

@app.post("/generate_test")
async def generate_test():
    """Generate a full listening test with multiple passages"""
    try:
        passages = []
        for i in range(NUM_MONOLOGUE):
            #* Generate
            data = generate_monologue()
            with open(f"{TEXT_OUTPUT_DIR}monologue{i}.txt", "w") as f:
                f.write(data)
            
            #* Read (for testing purposes, read existing generated monologue)
            # with open(f"{TEXT_OUTPUT_DIR}monologue{i}.txt", "r") as f:
            #     data = f.read()
                
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
            data = generate_dialogue()
            with open(f"{TEXT_OUTPUT_DIR}dialogue{i}.txt", "w") as f:
                f.write(data)
            
            #* Read (for testing purposes, read existing generated dialogue)
            # with open(f"{TEXT_OUTPUT_DIR}/dialogue{i}.txt", "r") as f:
            #     data = f.read()
                
            data = json.loads(data, strict=False)
            audio_path = synthesize_dialogue(data['dialogue'], f"{AUDIO_OUTPUT_DIR}dialogue{i}.wav")
            
            passages.append({
                "type": "dialogue",
                "topic": data['scenario'],
                "content": data['dialogue'],
                "audio_url": audio_path,
                "questions": parse_questions(data, NUM_QUESTION_PER_PASSAGE)
            })
        
        return {"passages": passages}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/grade_subjective/")
async def grade_subjective(data:dict):
    try:
        user_answer = data.get("user_answer")
        expected_answer = data.get("expected_answer")
        question_text = data.get("question_text")
        passage_text = data.get("passage_text")

        # Validate inputs
        if not all([user_answer, expected_answer, question_text, passage_text]):
            raise HTTPException(status_code=400, detail="Missing required fields.")
        
        grading_input = GRADING_PROMPT.format(
            passage_text=passage_text,
            question5_text=question_text,
            expected_answer=expected_answer,
            user_answer=user_answer
        )
        response = generate(grading_input, 512)
        grading_result = json.loads(response, strict=False)
        
        return grading_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/test_json/")
async def test_json(data: dict):
    return data.get("user_answer")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8181)