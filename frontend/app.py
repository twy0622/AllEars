import streamlit as st
import requests
import json

# Backend API URL
BACKEND_URL = "http://localhost:8181"

# Initialize session state
if "test_data" not in st.session_state:
    st.session_state.test_data = None
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "score" not in st.session_state:
    st.session_state.score = None

# Fetch test data from the backend
def fetch_test():
    try:
        response = requests.post(f"{BACKEND_URL}/generate_test/")
        if response.status_code == 200:
            st.session_state.test_data = response.json()
        else:
            st.error("Failed to fetch test data.")
    except Exception as e:
        st.error(f"Error fetching test data: {e}")

# Display passages and questions
def display_test():
    if st.session_state.test_data:
        for passage in st.session_state.test_data["passages"]:
            st.subheader(f"{passage['type'].capitalize()}: {passage['topic']}")
            
            # Play audio
            st.audio(passage["audio_url"], format="audio/wav")
            
            # Display questions
            for i, question in enumerate(passage["questions"]):
                st.write(f"**Question {i+1}:** {question['question']}")
                
                # Display MCQ questions
                if question["type"] == "mcq":
                    options = list(question["choices"].values())  # Extract choice values
                    answer_keys = list(question["choices"].keys())  # Extract choice keys (A, B, C, D)
                    
                    # Use st.radio to display options and get user selection
                    user_choice = st.radio(
                        f"Select an option for Question {i+1}", 
                        options, 
                        key=f"{passage['type']}_{i}"
                    )
                    
                    # Store the corresponding key (A, B, C, D) in session state
                    user_answer_key = answer_keys[options.index(user_choice)]
                    st.session_state.user_answers[f"{passage['type']}_{i}"] = user_answer_key
                
                elif question["type"] == "gapfill":
                    answer = st.text_input(f"Answer for Question {i+1}", key=f"{passage['type']}_{i}")
                    st.session_state.user_answers[f"{passage['type']}_{i}"] = answer
                
                elif question["type"] == "subjective":
                    answer = st.text_area(f"Answer for Question {i+1}", key=f"{passage['type']}_{i}")
                    st.session_state.user_answers[f"{passage['type']}_{i}"] = answer

# Calculate score
def calculate_score():
    score = 0
    for passage in st.session_state.test_data["passages"]:
        for i, question in enumerate(passage["questions"]):
            user_answer = st.session_state.user_answers.get(f"{passage['type']}_{i}")
            
            if question["type"] in ["mcq", "gapfill"]:
                if user_answer == question["answer"]:
                    score += 1
            
            elif question["type"] == "subjective":
                # Call grading endpoint for subjective answers
                response = requests.post(
                    f"{BACKEND_URL}/grade_subjective/",
                    json={
                        "user_answer": user_answer,
                        "expected_answer": question["expected_answer"],
                        "question_text": question["question"],
                        "passage_text": passage["content"]
                    }
                )
                if response.status_code == 200:
                    grade = response.json().get("grade")
                    if grade == "Correct":
                        score += 1
                    elif grade == "Partial":
                        score += 0.5
    
    st.session_state.score = score

# Main app
def main():
    st.title("AllEars 🎧 - English Listening Test")

    if st.button("Start Test"):
        fetch_test()

    if st.session_state.test_data:
        display_test()

        if st.button("Submit Answers"):
            calculate_score()
            st.success(f"Your score: {st.session_state.score}/{len(st.session_state.user_answers)}")

if __name__ == "__main__":
    main()