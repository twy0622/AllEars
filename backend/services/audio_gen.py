from kokoro import KPipeline
import soundfile as sf
import random
import numpy as np
import re

VOICE_LIST = [
    #* american female
    'af_sky,af_bella,af_heart',
    'af_sarah,af_sarah,af_heart',
    #* american male
    'am_puck,am_fenrir,am_michael',
    'am_liam,am_liam,am_puck',
    #* british female
    'bf_emma,bf_isabella,bf_isabella',
    'bf_alice,bf_isabella',
    #* british male
    'bm_fable,bm_daniel',
    'bm_lewis,bm_lewis,bm_daniel,bm_fable'
]

def synthesize_monologue(text, gender, output_path="audio/monologue.wav"):
    """Synthesize a monologue with random voice selection"""
    # Random voice selection and lang_code determination
    try:
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
        audio_chunks = [audio for _, _, audio in generator]
        
        if audio_chunks:
            full_audio = np.concatenate(audio_chunks)
            sf.write(output_path, full_audio, 24000)
            return output_path
        return None
    except Exception as e:
        print(f"Error synthesizing monologue: {e}")
        return None

def synthesize_dialogue(text, output_path="audio/dialogue.wav"):
    """Synthesize dialogue with alternating voices from same language group"""
    try:
        # Split text into speaking turns
        turns = re.split(r'\n+', text.strip())
        
        lang_code = random.choice(['a','b'])
        
        if lang_code == 'a':
            male_voice = random.choice([voice for voice in VOICE_LIST if voice.startswith('am')])
            female_voice = random.choice([voice for voice in VOICE_LIST if voice.startswith('af')])
        elif lang_code == 'b':
            male_voice = random.choice([voice for voice in VOICE_LIST if voice.startswith('bm')])
            female_voice = random.choice([voice for voice in VOICE_LIST if voice.startswith('bf')])
        
        voice_mapping = {'A': female_voice, 'B': male_voice}
        
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
                speed=1.1,
                split_pattern=None  # No splitting within a single turn
            )
            
            for _, _, audio in generator:
                audio_chunks.append(audio)
        
        if audio_chunks:
            full_audio = np.concatenate(audio_chunks)
            sf.write(output_path, full_audio, 24000)
            return output_path
        return None
    except Exception as e:
        print(f"Error synthesizing dialogue: {e}")
        return None