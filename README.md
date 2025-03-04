# AllEars 🎧  
AI-powered English listening tests

## Overview

This projects creates an English Listening Test similar to CEFL (Cambridge English for Life) listening assessments with the help of AI tools.

- [Gemini 2.0 Flash](https://deepmind.google/technologies/gemini/flash/): Automatic Monologue/Dialogue & Question Generation
- [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M): High-quality TTS Generation 

## Features
- **Dynamic Test Generation**: Automatically creates two unique listening passages and a set of 10 questions.  
- **High-Quality Audio**: Powered by Kokoro TTS for natural-sounding playback.  
- **Realistic Test Simulation**: Includes a 10-minute timer, no replay options, and instant score display.  
- **Feedback Mode**: Shows incorrect answers with solutions side-by-side after the test.  
- **Configurable Passage Count**

## How It Works
1. **Start Test**: Click "Start Test" on the home page.  
2. **Test Begins**:  
   - Two passages are generated, along with 10 comprehension questions.  
   - TTS audio is played twice with a 30-second break in between.  
   - No replay option (simulates real test conditions).  
3. **Test Ends**:  
   - Displays your score.  
   - Shows incorrect answers with solutions side-by-side.  
   - Option to replay the generated audio or try again with a new test.  

## Development Roadmap
- [x] Core audio generation with Kokoro TTS
- [x] Monologue/Dialogue Generation
- [x] Question Generation
- [x] Web UI Development - Streamlit

## Future Enhancements
- **React Web UI**  
  - Modern interface with progress visualization  
  - (Currently self-learning React)  

- **CEFR Reference Integration**  
  - Add B1/B2 sample transcripts to prompts  
  - Validate generated content against CEFR criteria  

- **Local Leaderboard**  
  - SQLite database implementation  
  - Track test scores and CEFR progress

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
