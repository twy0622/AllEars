APIKEY = "abc123" #! USE YOUR OWN GEMINI API KEY

MONOLOGUE_PROMPT = """
You are an expert content creator and assessment designer. 
Your task is to generate a monologue in the first-person POV, with each paragraph having a maximum of 50 words. 
The monologue **MUST be at least 300 words long**.

** Topic Guidelines **

*   **Travel and Tourism:** Planning a trip, describing a vacation, reviewing a hotel or attraction.
*   **Education and Learning:** Describing a course, giving study tips, talking about a school project.
*   **Hobbies and Leisure Activities:** Describing a hobby, reviewing a film or book, discussing a cultural event.
*   **Health and Well-being:** Giving advice on healthy eating, discussing exercise, talking about stress management.
*   **Environment and Nature:** Talking about environmental issues, describing a landscape, discussing conservation.
*   **Work and Career:** Describing a job, giving career planning advice, talking about workplace issues.

**The monologue should also include the following features: **

*   Personal anecdotes
*   Opinions and attitudes
*   Descriptive language
*   Advice and recommendations
*   A clear structure (introduction, body, conclusion)
*   Relatable content (avoiding overly technical or specialized language)
*   Use simple, common vocabulary that is easy to spell and transcribe accurately. Avoid complex or rarely-used words.

After the monologue, generate five comprehension questions based on the monologue: two multiple-choice questions, two gap-fill questions (one requiring an *exact single-word* answer and the other requiring an *exact phrase* answer), and one subjective question with a sample reference answer.  Make sure the gap-fill questions use words and phrases that are not easily guessable and MUST require careful attention to the monologue to answer correctly.

You **MUST** follow these strict formatting rules to ensure machine readability:

*   Format the output as a JSON object with the following schema, paying close attention to the example values and data types:*

```json
{{
  "text": "The monologue text goes here. It must hav",
  "gender": "male or female",
  "question1": {{
    "question": "Multiple-choice question 1",
    "choices": {{
      "a": "Choice A",
      "b": "Choice B",
      "c": "Choice C",
      "d": "Choice D"
    }},
    "answer": "Correct choice (e.g., 'a')"
  }},
  "question2": {{
    "question": "Multiple-choice question 2",
    "choices": {{
      "a": "Choice A",
      "b": "Choice B",
      "c": "Choice C",
      "d": "Choice D"
    }},
    "answer": "Correct choice (e.g., 'b')"
  }},
  "question3": {{
    "question": "Gap-fill question requiring a single-word answer. Ensure the word is context-specific, non-obvious, and cannot be guessed without careful reading.",
    "answer": "Exact single-word answer"
  }},
  "question4": {{
    "question": "Gap-fill question requiring a phrase answer. Ensure the phrase is precise, directly tied to a key detail in the monologue, and not easily guessable without attentive reading.",
    "answer": "Exact phrase answer"
  }},
  "question5": {{
    "question": "Subjective question that requires reflection or summarization of a key insight from the monologue.",
    "expected_answer": "Expected answer"
  }}
}}
```

*   Ensure the questions are directly relevant to the monologue and test comprehension of key details.
*   When creating the gap-fill questions, use chain-of-thought reasoning to craft answers that are specific, integral to the narrative, and require focused attention to identify. Avoid generic or predictable terms.  **The gap-fill answers should not be able to be guessed without attentively reading the monologue.**
*   Choose a random gender (male or female) for the monologue.
*   ONLY IF non-English terms appear, annotate them with IPA transcriptions like [word](/IPA/). e.g. [Kokoro](/kˈOkəɹO/). Otherwise, ignore this instruction.
"""

DIALOGUE_PROMPT = ""

GRADING_PROMPT = """Compare the user's answer to the expected answer. Determine if the user's answer is semantically similar enough to be considered correct. Respond with 'Correct' or 'Incorrect'.  
User's Answer: {user_answer}
Expected Answer: {expected_answer}"""