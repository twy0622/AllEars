from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, data):
        self.question = data['question']
    
    def display(self):
        print(f"Question: {self.question}")
        
    @abstractmethod
    def check_answer(self, response):
        pass

class MCQ(Question):
    def __init__(self, data):
        super().__init__(data)
        self.choices = data['choices']
        self.answer = data['answer']
    
    def display(self):
        super().display()
        print("Choices:")
        for key, value in self.choices.items():
            print(f"  {key}: {value}")
        print(f"Answer: {self.answer}")
        
    def check_answer(self, response):
        return self.answer == response

class GapFill(Question):
    def __init__(self, data):
        super().__init__(data)
        self.answer = data['answer']
    
    def display(self):
        super().display()
        print(f"Answer: {self.answer}")
    
    def check_answer(self, response):
        """convert answer and response to lower case for consistency"""
        return self.answer.lower() == response.lower()

class Subjective(Question):
    def __init__(self, data):
        super().__init__(data)
        self.expected_answer = data['expected_answer']
    
    def display(self):
        super().display()
        print(f"Expected Answer: {self.expected_answer}")

    def check_answer(self, response):
        """Use LLM here to determine whether the answer is correct"""
        # print(constants.GRADING_PROMPT.format(user_answer="test", expected_answer="test2"))
        return True