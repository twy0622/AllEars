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
- [ ] Monologue/Dialogue Generation
- [ ] Question Generation
- [ ] Web UI Development

## Future Enhancements
- **Kokoro ONNX Integration**: Less dependencies and can run on edge devices.
- **Local Leaderboard**: Track your progress over time.  
- **Difficulty Settings**: Customize tests for Elementary (A2-B1), Intermediate (B2), Advanced (C1), and Proficient (C2) levels.  
- **Multi-User**: Redis database to keep track of user data.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
