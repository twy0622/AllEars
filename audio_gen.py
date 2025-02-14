"""
Script to generates text to speech using Kokoro
TODO: need to fix KPipeline for british lang_code = 'b'
"""
from kokoro import KPipeline
import soundfile as sf
import random
import numpy as np

pipeline = KPipeline(lang_code='a') # misaki[en]

text = '''
The moment I landed in Bali, I knew this trip would be unforgettable. The warm breeze greeted me like an old friend, carrying the scent of frangipani flowers. My heart raced with excitement as I stepped off the plane, ready to explore every corner of this paradise.

Our villa was nestled near [Ubud](/uːˈbud/), surrounded by lush rice paddies that stretched endlessly. Waking up to the sound of birds chirping felt surreal. Each morning began with a cup of local coffee, its rich aroma filling the air. It tasted like pure happiness in liquid form.

One day, we visited [Tegalalang](/tɛgələˈlɑːŋ/) Rice Terrace. Walking through those emerald-green fields felt magical. The sun cast golden light over everything, making it look like a dream. We took countless photos but none could capture its true beauty. Every step revealed something new and breathtaking.

I tried surfing for the first time at [Kuta](/kuːˈtɑː/) Beach. Falling into the waves became part of the fun! Locals cheered us on from the shore, their laughter infectious. By sunset, my arms ached, but I couldn’t stop smiling. Surfing turned out to be exhilarating.

At night, we wandered through bustling markets filled with vibrant colors. Street vendors offered delicious snacks like [satay](/səˈteɪ/) skewers and fresh coconut drinks. Haggling over prices added to the adventure. These small interactions made me feel connected to the culture here.

We ended our journey watching dolphins near [Lovina](/loʊˈviːnə/). Their playful leaps left me awestruck. As they danced alongside the boat, I realized how lucky I was. This vacation wasn’t just about seeing beautiful places—it was about feeling alive.
'''

#* preselected 4 voices
voice_list = [
    'af_heart',     # american female
    'am_puck',      # american male
    'bf_emma',      # british female
    'bm_daniel'     # british male
]

voice = random.choice(voice_list)
generator = pipeline(
    text, voice='af_heart',
    speed=1, split_pattern=r'\n+'
)
data = []
for i, (gs, ps, audio) in enumerate(generator):
    data.append(audio)
data = np.concatenate(data)
sf.write(f'listening_test/audio/test.wav', data, 24000) # save each audio file
