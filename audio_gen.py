"""
generate a passage in the first person pov of a girl named sarah (not needed to mentioned in the passage) talking about her vacation in bali and how much fun she had. with at least 300 words. each paragraph should have a maximum of 60 words and no minimum.

i need u to annotate the text if it has a certain pronunciation as i will be passing this passage into a text to speech model and i dont want it to botch the pronunciations. annotate it like this e.g. [Kokoro](/kˈOkəɹO/). Do not annotate English words, only Names or Words in a different language.

The (pronunciation) tag should follow the indicated word, not the entire phrase.
e.g.
[Kokoro Language](/kˈOkəɹO/) is wrong.
[Kokoro](/kˈOkəɹO/) is correct.
"""
# 3️⃣ Initalize a pipeline
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

voice_list = [
    'af_heart',
    'am_puck',
    'bf_emma',
    'bm_daniel'
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
