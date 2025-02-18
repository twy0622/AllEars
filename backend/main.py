from fastapi import FastAPI, HTTPException
from services.passage_gen import *
from services.audio_gen import synthesize_monologue, synthesize_dialogue
from config import *
from backend.services.constants import *
import json

app = FastAPI(title="AllEars", version="1.0.0")

@app.post("/generate_test")
async def generate_test():
    """Generate a full listening test with multiple passages"""
    try:
        passages = []
        for i in range(NUM_MONOLOGUE):
            data = generate_monologue()
            data = json.loads(data, strict=False)
            with open(f"{TEXT_OUTPUT_DIR}monologue{i}.txt", "w") as f:
                f.write(data)
            audio_path = synthesize_monologue(data['text'], data['gender'], f"{AUDIO_OUTPUT_DIR}monologue{i}.wav")
            
            passages.append({
                "content": data,
                "audio_url": audio_path
            })
        
        for i in range(NUM_DIALOGUE):
            data = generate_dialogue()
            data = json.loads(data, strict=False)
            with open(f"{TEXT_OUTPUT_DIR}dialogue{i}.txt", "w") as f:
                f.write(data)
            audio_path = synthesize_dialogue(data['text'], data['gender'], f"{AUDIO_OUTPUT_DIR}dialogue{i}.wav")
            
            passages.append({
                "content": data,
                "audio_url": audio_path
            })
        
        return {"passages": passages}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))