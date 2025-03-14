import os

#* Set up your own API key first according to your OS (insert into environment variables)
#  https://ai.google.dev/gemini-api/docs/api-key
APIKEY = os.environ['GEMINI_API_KEY']

#* Claude-optimized prompt
MONOLOGUE_PROMPT = """
# MONOLOGUE ASSESSMENT GENERATOR
## Core Instructions

You are an expert assessment content creator specializing in language evaluation. Your task has two parts:
1. Generate an authentic first-person monologue
2. Create targeted comprehension questions based on that monologue

### MONOLOGUE SPECIFICATIONS
- First-person perspective only
- Length: MUST be 400-500 words total
- Paragraph structure: Each paragraph MUST contain 50 words maximum
- Voice: Choose ONE gender (male or female) and maintain consistency
- Language level: B1-B2 (intermediate) with common vocabulary
- Style: Conversational, relatable, avoiding technical jargon

### TOPIC
{topic}

### REQUIRED ELEMENTS
The monologue MUST include ALL of the following:
- At least one specific personal anecdote with concrete details
- Clear expression of at least two distinct opinions or attitudes
- Minimum three instances of descriptive language (sensory details)
- At least two pieces of advice or recommendations
- A three-part structure: introduction (setting context), body (developing ideas), conclusion (reflection)

### QUESTION DESIGN REQUIREMENTS
After creating the monologue, design five questions that test genuine comprehension:

1. Multiple-choice question #1: Focus on a key detail that requires careful reading
2. Multiple-choice question #2: Focus on an inference or implied meaning
3. Gap-fill question #1: Require an EXACT SINGLE WORD that is:
   - Content-specific
   - Not easily inferred from context
   - Integral to understanding a key point
4. Gap-fill question #2: Require an EXACT PHRASE that:
   - Is a continuous 2-4 word sequence DIRECTLY FROM THE TEXT
   - Forms a complete syntactic unit (noun phrase, verb phrase, prepositional phrase)
   - Contains a unique combination that only makes sense in context
   - Example of VALID: "morning jog routine" or "reusable shopping bags"
   - Example of INVALID: "loop me" (nonsensical) or "sustainable energy" (common combo)
5. Subjective question: 
   - Asks about a specific viewpoint, argument, or theme presented in the monologue
   - Requires the reader to explain or interpret a particular aspect in their own words
   - Tests deeper understanding of the author's perspective or reasoning
   - Has a sample answer that shows comprehension of the specific point while allowing for personal expression

## OUTPUT FORMAT
Return a JSON object with the following exact structure:

```json
{{
  "text": "Full monologue text",
  "gender": "male/female",
  "topic": "Provided topic",
  "question1": {{
    "question": "Multiple-choice question about a specific detail",
    "choices": {{
      "a": "Choice A",
      "b": "Choice B",
      "c": "Choice C",
      "d": "Choice D"
    }},
    "answer": "a/b/c/d"
  }},
  "question2": {{
    "question": "Multiple-choice question requiring inference",
    "choices": {{
      "a": "Choice A",
      "b": "Choice B",
      "c": "Choice C",
      "d": "Choice D"
    }},
    "answer": "a/b/c/d"
  }},
  "question3": {{
    "question": "Gap-fill question with blank for a single word",
    "answer": "specific_word"
  }},
  "question4": {{
    "question": "Gap-fill question with blank for a phrase",
    "answer": "specific phrase"
  }},
  "question5": {{
    "question": "Question asking for interpretation of a specific viewpoint or theme from the monologue",
    "expected_answer": "Sample response demonstrating understanding of the specific point while using own words"
  }}
}}
```

## VALIDATION CHECKLIST
Before finalizing, verify that:
- [ ] Monologue is between 400-500 words
- [ ] Each paragraph is 50 words or less
- [ ] All required elements are present
- [ ] Gap-fill answers cannot be guessed without reading
- [ ] Questions test different levels of comprehension
- [ ] JSON structure follows the exact format specified
- [ ] No placeholders or template language remains
- [ ] Line breaks use \\n in the JSON output

## EXECUTION PROCESS
1. Understand the provided topic
2. Draft the monologue meeting all requirements
3. Count words to ensure 400-500 total
4. Create the five questions following specifications
5. Validate against the checklist
6. Format the final response in proper JSON with escaped newlines

If any IPA transcriptions are needed for non-English terms, use the format: [word](/IPA/) e.g. [Kokoro](/kˈOkəɹO/)
"""

#* Claude-generated prompt based off of monologue prompt
DIALOGUE_PROMPT = """
# DIALOGUE ASSESSMENT GENERATOR
## Core Instructions

You are an expert assessment content creator specializing in conversational language evaluation. Your task has two parts:
1. Generate an authentic dialogue between two speakers
2. Create targeted comprehension questions based on that dialogue

### DIALOGUE SPECIFICATIONS
- Format: A conversation between Speaker A (female) and Speaker B (Male)
- Length: MUST be 200-300 words total
- Structure: Clear turn-taking with alternating speakers
- Character consistency: Each speaker must have a distinct voice/personality
- Language level: B1-B2 (intermediate) with common vocabulary

### SCENARIO
{topic}

### REQUIRED ELEMENTS
The dialogue MUST include ALL of the following:
- At least one disagreement or different perspective
- Exchange of specific information (facts, details, or data)
- Expression of emotions or attitudes
- Problem-solving or decision-making process
- A clear beginning, middle, and conclusion to the conversation
- At least one instance of clarification or follow-up questions

### QUESTION DESIGN REQUIREMENTS
After creating the dialogue, design five questions that test genuine comprehension:

1. Multiple-choice question #1: Focus on specific information exchanged in the dialogue
2. Multiple-choice question #2: Focus on inference about speaker attitudes or relationships
3. Gap-fill question #1: Require an EXACT SINGLE WORD that is:
   - Dialogue-specific
   - Critical to understanding a key point
   - Not easily guessed without reading
4. Gap-fill question #2: Require an EXACT PHRASE that:
   - Is a verbatim 2-4 word sequence SPOKEN BY A CHARACTER
   - Forms a meaningful utterance when standing alone
   - Represents a specific turn of phrase from the dialogue
   - Example of VALID: "weekly team sync" or "eco-friendly packaging"
   - Example of INVALID: "her in" (fragment) or "project timeline" (too generic)
5. Subjective question: 
   - Asks about a specific viewpoint, argument, or dynamic presented in the dialogue
   - Requires explaining or interpreting a particular speaker's perspective
   - Tests deeper understanding of underlying motivations or reasoning

## OUTPUT FORMAT
Return a JSON object with the following exact structure:

```json
{{
  "dialogue": "A: [First speaker line]\\nB: [Second speaker line]\\nA: [Next line]\\n...",
  "scenario": "Provided scenario",
  "question1": {{
    "question": "Multiple-choice question about specific information",
    "choices": {{
      "a": "Choice A",
      "b": "Choice B",
      "c": "Choice C",
      "d": "Choice D"
    }},
    "answer": "a/b/c/d"
  }},
  "question2": {{
    "question": "Multiple-choice question requiring inference",
    "choices": {{
      "a": "Choice A",
      "b": "Choice B",
      "c": "Choice C",
      "d": "Choice D"
    }},
    "answer": "a/b/c/d"
  }},
  "question3": {{
    "question": "Gap-fill question with blank for a single word",
    "answer": "specific_word"
  }},
  "question4": {{
    "question": "Gap-fill question with blank for a phrase",
    "answer": "specific phrase"
  }},
  "question5": {{
    "question": "Question asking for interpretation of a specific viewpoint or dynamic",
    "expected_answer": "Sample response demonstrating understanding of the specific perspective"
  }}
}}
```

## VALIDATION CHECKLIST
Before finalizing, verify that:
- [ ] Dialogue is between 200-300 words
- [ ] Speakers alternate consistently (A, B, A, B...)
- [ ] All required elements are present
- [ ] Each speaker has a consistent voice/personality
- [ ] Gap-fill answers cannot be guessed without reading
- [ ] Questions test different levels of comprehension
- [ ] JSON structure follows the exact format specified
- [ ] Line breaks use \\n in the JSON output

## EXECUTION PROCESS
1. Understand the provided scenario
2. Create speaker profiles with distinct traits/roles
3. Draft the dialogue meeting all requirements
4. Count words to ensure 200-300 total
5. Create the five questions following specifications
6. Validate against the checklist
7. Format the final response in proper JSON with escaped newlines

If any IPA transcriptions are needed for non-English terms, use the format: [word](/IPA/) e.g. [Kokoro](/kˈOkəɹO/)
"""

#* Claude-generated prompt
GRADING_PROMPT = """# GRADING PROMPT FOR SUBJECTIVE QUESTION (Question 5)
You are an expert assessment evaluator specializing in open-ended responses. Your task is to evaluate a user's answer to a subjective comprehension question about a monologue.

## Input Data
- Original Monologue: {passage_text}
- Question: {question5_text}
- Expected Answer: {expected_answer}
- User's Answer: {user_answer}

## Evaluation Criteria
Score the answer as "Correct," "Partial," or "Incorrect" based on the following criteria:

### Core Understanding (Required)
- Does the answer demonstrate comprehension of the specific viewpoint, argument, or theme mentioned in the question?
- Does it show that the user grasped the author's perspective or reasoning on this particular point?

### Evidence of Engagement (Required)
- Does the answer reference relevant details, examples, or statements from the monologue?
- Is there clear evidence that the user read and processed the specific aspect being asked about?

### Personal Expression (Acceptable)
- The answer may use different wording, structure, or emphasis than the expected answer
- The answer may include additional perspectives or interpretations
- The answer may be shorter or longer than the expected answer

## Grading Process
1. Identify the key elements in the expected answer that demonstrate understanding
2. Check if the user's answer contains equivalent elements, even if expressed differently
3. Determine if the response shows genuine engagement with the specific aspect asked about
4. Ignore minor grammar, spelling, or style differences

## Decision Rules
Mark as "Correct" if:
- The answer demonstrates clear understanding of the specific viewpoint/theme/argument
- There is evidence the user engaged with the relevant part of the monologue
- The core meaning aligns with the expected answer, even if expressed uniquely

Mark as "Partial" if:
- The answer shows some understanding but misses key aspects of the viewpoint/theme/argument
- There is limited evidence of engagement with the monologue
- Some core elements are correct while others are missing or misunderstood
- The response is somewhat vague but shows basic comprehension

Mark as "Incorrect" if:
- The answer completely misses or misunderstands the specific viewpoint/theme/argument
- There is no evidence of engagement with the relevant part of the monologue
- The response is completely unrelated or contradicts the monologue's message
- The answer is too vague or general to demonstrate any specific understanding

## Output Format
```json
{{
 "grade": "Correct/Partial/Incorrect",
 "explanation": "Brief explanation of why the answer was marked as correct, partial, or incorrect, referencing specific elements from the user's response and noting any missing key points for partial grades"
}}
```"""

# text = "A: Hi Sarah, thanks for meeting me to discuss the Johnson project. I wanted to get your input on the marketing strategy before we finalize it.\nB: Hi Mark, thanks for including me. I’ve reviewed the initial plan, and while I think the overall concept is strong, I have some concerns about the target demographic. \nA: Oh? What are your specific concerns? I thought targeting millennials was a safe bet, given their online presence.\nB: I understand the logic, but I think we're overlooking a significant portion of potential customers: the 35-50 age group. They have more disposable income and are actively looking for solutions like the one Johnson provides. \nA: That's a fair point. We did consider that demographic initially, but the data suggested millennials were more responsive to online advertising campaigns. We were aiming for quick results and maximum reach. \nB: I see. But are we prioritizing speed over long-term sustainability? The 35-50 group might be slower to convert, but they are also more likely to become loyal customers. Plus, they often rely on word-of-mouth, which can be incredibly powerful.\nA: Okay, you’ve given me something to think about. Perhaps we could explore a dual-pronged approach? Target millennials with our initial online campaign, but also allocate some resources to reach the older demographic through more traditional channels, like print ads or targeted social media campaigns.\nB: That sounds much more balanced. We could also tailor the messaging to resonate with each group. Millennials might be drawn to the innovative aspects of the product, while the older group might be more interested in its reliability and practicality.\nA: Exactly! And we can track the results of each campaign to see which approach is more effective. What kind of budget adjustments would we need to make to accommodate this dual approach?\nB: I think we can reallocate about 15% of the online advertising budget to the print and targeted social media campaigns. I'll draft a revised budget proposal for you by the end of the week.\nA: Fantastic. I really appreciate your insights, Sarah. It’s good to have a different perspective. I think this revised strategy will give us a much better chance of success.\nB: Glad I could help, Mark. I think it will too. Collaboration is key!"

# import re
# turns = re.split(r'\n+', text.strip())
# for turn in turns:
#   print(re.match(r'^([AB]):\s*(.*)', turn).groups())