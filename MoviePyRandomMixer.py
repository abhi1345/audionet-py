# Dependencies: pydub, moviepy
# https://github.com/jiaaro/pydub, https://zulko.github.io/moviepy/
import random
import sys
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.editor import *
from pydub import AudioSegment

inFile = sys.argv[1]
outPathVideo = sys.argv[2]
audioFile = sys.argv[3]
name = sys.argv[4]

videoSilencePath = "/data/abhi/silence.mp4"
audioSilencePath = "/data/abhi/silence.wav"

vClip = VideoFileClip(inFile)
d = vClip.duration

aClip = AudioSegment.from_file(audioFile, format="wav")

vSilence = ColorClip(vClip.size, (0,0,0), duration=5)
aSilence = AudioSegment.silent(duration=5000)

vArray = []
aArray = []

i = 0
index = 0

finalAudio = AudioSegment.empty()

while i < d:
    index += 1
    vtemp = vClip.subclip(i, min(i+10, d))
    vtemp2 = concatenate_videoclips([vtemp, vSilence])
    atemp = aClip[i*1000:(i+10)*1000] + aSilence
    seed = random.randrange(index)
    aArray.insert(seed, atemp)
    vArray.insert(seed, vtemp2)
    i += 8

for i in aArray:
    finalAudio += i

final_clip = concatenate_videoclips(vArray)

fullOutAudioPath = '/data/abhi/videos/Randomized/audio/' + 'randomized_' + name + ".wav"

axp = finalAudio.export(fullOutAudioPath, format="wav")

final_clip.write_videofile(outPathVideo + 'randomized' + name + '.mp4',
  codec='libx264',
  audio_codec='aac',
  temp_audiofile='temp-audio.m4a',
  remove_temp=True)
