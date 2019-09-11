import sys
inFile = sys.argv[1]
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
clip = VideoFileClip(inFile)
a = (clip.duration )

i = 0

while i < clip.duration:
    
    outFile = '../test2/' + inFile + str(i) + "_to_"+str(i+10)+ ".mp4"
    
    ffmpeg_extract_subclip(inFile, i, i+10, targetname=outFile)

    i += 10
