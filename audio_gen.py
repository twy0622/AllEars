from kokoro import KPipeline
import soundfile as sf
import random
import numpy as np
import re

VOICE_LIST = [
    'af_heart',     # american female
    'am_puck',      # american male
    'bf_emma',      # british female
    'bm_daniel'     # british male
]

def synthesize_monologue(text, gender, output_path="audio/monologue.wav"):
    """Synthesize a monologue with random voice selection"""
    # Random voice selection and lang_code determination
    if gender == "male":
        voice = random.choice([voice for voice in VOICE_LIST if voice.startswith("am") or voice.startswith("bm")])
    elif gender == "female":
        voice = random.choice([voice for voice in VOICE_LIST if voice.startswith("af") or voice.startswith("bf")])
    else:
        voice = random.choice(VOICE_LIST)

    lang_code = 'a' if voice.startswith("a") else 'b'
    
    # Create pipeline and process text
    pipeline = KPipeline(lang_code=lang_code)
    generator = pipeline(
        text, 
        voice=voice,
        speed=1,
        split_pattern=r'\n+'
    )
    
    # Generate and concatenate audio
    audio_chunks = []
    for _, _, audio in generator:
        audio_chunks.append(audio)
    
    if audio_chunks:
        full_audio = np.concatenate(audio_chunks)
        sf.write(output_path, full_audio, 24000)

def synthesize_dialogue(text, output_path="audio/dialogue.wav"):
    """Synthesize dialogue with alternating voices from same language group"""
    # Split text into speaking turns
    turns = re.split(r'\n+', text.strip())
    
    # Choose language group and voices
    lang_group = random.choice(['american', 'british'])
    if lang_group == 'american':
        voices = ['af_heart', 'am_puck']
        lang_code = 'a'
    else:
        voices = ['bf_emma', 'bm_daniel']
        lang_code = 'b'
    
    random.shuffle(voices)
    voice_mapping = {'A': voices[0], 'B': voices[1]}
    
    # Create pipeline and process dialogue
    pipeline = KPipeline(lang_code=lang_code)
    audio_chunks = []
    
    for turn in turns:
        if not turn:
            continue
            
        # Parse speaker and content
        speaker, content = re.match(r'^([AB]):\s*(.*)', turn).groups()
        voice = voice_mapping[speaker]
        
        # Generate audio for this turn
        generator = pipeline(
            content,
            voice=voice,
            speed=1,
            split_pattern=None  # No splitting within a single turn
        )
        
        for _, _, audio in generator:
            audio_chunks.append(audio)
    
    if audio_chunks:
        full_audio = np.concatenate(audio_chunks)
        sf.write(output_path, full_audio, 24000)