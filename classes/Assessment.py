from abc import ABC
from classes.Question import *

class Assessment(ABC):
    def __init__(self, mcq=2, gapfill=2, subjective=1):
        self.mcq = mcq
        self.gapfill = gapfill
        self.subjective = subjective
        self.questions = {}
        self.content = ""
        
    def initialize_questions(self, data):
        q_num = 1
        
        # Initialize MCQs
        for i in range(self.mcq):
            self.questions[f"question{q_num}"] = MCQ(data[f'question{q_num}'])
            q_num += 1
        
        # Initialize GapFills
        for i in range(self.gapfill):
            self.questions[f"question{q_num}"] = GapFill(data[f'question{q_num}'])
            q_num += 1
        
        # Initialize Subjectives
        for i in range(self.subjective):
            self.questions[f"question{q_num}"] = Subjective(data[f'question{q_num}'])
            q_num += 1
    
        # q_num overcounts by 1 but does not affect the correctness of this code
        
class Monologue(Assessment):
    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        self.content = data['text'].replace("\n\n ", "\n")
        self.gender = data['gender']
        self.topic = data['topic']
        self.initialize_questions(data)

class Dialogue(Assessment):
    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        self.content = data['text'].replace("\n\n ", "\n")
        self.gender = data['gender']
        self.topic = data['topic']
        self.initialize_questions(data)