""" Assessment Configuration """

#* PASSAGE
NUM_MONOLOGUE = 1
NUM_DIALOGUE = 1

#* QUESTION
NUM_QUESTION_PER_PASSAGE = {
    "mcq": 2,
    "gapfill": 2,
    "subjective": 1
}

#* PASSAGE PATH
TEXT_OUTPUT_DIR = "text/"

#* AUDIO PATH
AUDIO_OUTPUT_DIR = "audio/"

#* ASSESSMENT DURATION
TEST_TIMER_DURATION = 300 * (NUM_MONOLOGUE + NUM_DIALOGUE) # 5 minutes per Passage