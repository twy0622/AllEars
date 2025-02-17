import json
import re

from constants import *
from classes.Assessment import *
from classes.Question import *
from passage_gen import process_json_output, generate
from audio_gen import synthesize_monologue, synthesize_dialogue

def clean_json(data: str):
    return re.sub(r',\s*([}\]])', r'\1', data).strip()

def main():
    """MONOLOGUE PROCESSING"""
    print("Generating Monologue...")
    monologue_data = generate(MONOLOGUE_PROMPT)
    with open("text/monologue.txt", "w") as f:
        f.write(clean_json(monologue_data))
    monologue_data = json.loads(monologue_data, strict=False)
    monologue = Monologue(monologue_data)
    
    synthesize_monologue(
        text=monologue.content,
        gender=monologue.gender,
        output_path="audio/monologue.wav"
    )
    print("Monologue generated and audio synthesized. Saved to audio/monologue.wav")
    
    print("\nGenerating Dialogue...")
    # Generate Dialogue
    dialogue_data = generate("dialogue")
    with open("text/dialogue.txt", "w") as f:
        f.write(clean_json(dialogue_data))
    dialogue_data = json.loads(dialogue_data, strict=False)
    dialogue = Dialogue(dialogue_data)
    
    # Synthesize Dialogue Audio
    synthesize_dialogue(
        text=dialogue.content,
        output_path="audio/dialogue.wav"
    )
    print("Dialogue generated and audio synthesized. Saved to audio/dialogue.wav")
    
#* text, gender, topic, question1 & question2[question,choices[a,b,c,d],answer], question3 & question4[question, answer], question5[question, expected_answer]

# print(GRADING_PROMPT.format(user_answer="test", expected_answer="test2"))

if __name__ == "__main__":
    main()