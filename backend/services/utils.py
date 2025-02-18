import re

def process_json_output(output: str):
    # remove json code blocks
    if output.startswith("```json"):
        output = output[7:]
    if output.endswith("```"):
        output = output[:-3]
        
    # regex: remove trailing commas in {}
    output = re.sub(r',\s*([}\]])', r'\1', output)
    
    # strip: remove trailing and leading whitespace
    output = output.strip()
    
    return output

def parse_questions(data, num_questions_per_type):
    questions = []
    n = 1
    
    for question_type, count in num_questions_per_type.items():
        # loops through NUM_QUESTION_PER_PASSAGE -> { mcq: 2, gapfill: 2, subjective: 1 }
        for _ in range(count):
            question = data[f"question{n}"]
            if question_type == "mcq":
                question['type'] = "mcq"
            elif question_type == "gapfill":
                question['type'] = "gapfill"
            elif question_type == "subjective":
                question['type'] = "subjective"
            questions.append(question)
            n += 1
    
    return questions