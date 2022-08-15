from fileinput import filename
from moviepy.editor import *
import numpy as np
import os
from datetime import timedelta
import sys
#no_of_frames_per_sec = 10

def format_timedelta(td):
    result=str(td)
    try:
        result,ms=result.split(".")
    except ValueError:
        return result+".00".replace(":","-")
    ms=int(ms)
    ms=round(ms/1e4)
    return f"{result}.{ms:02}".replace(":","-") 

def main(video_file):
    no_of_frames_per_sec = 24
    #loading the video clip
    video_clip=VideoFileClip(video_file,audio=False)
    #making a folder with video file name for saving frames
    filename, _ = os.path.splitext(video_file)
    filename += "-moviepy"
    if not os.path.isdir(filename):
        os.mkdir(filename)
    no_of_frames_per_sec=min(video_clip.fps,no_of_frames_per_sec)
    step= 1/video_clip.fps if no_of_frames_per_sec==0 else 1/no_of_frames_per_sec
    #looping over each frame
    for current_duration in np.arange(0,video_clip.duration,step):
        frame_duration_formatted= format_timedelta(timedelta(seconds=current_duration)).replace(":","-")
        frame_filename= os.path.join(filename,f"frame{frame_duration_formatted}.jpg")
        video_clip.save_frame(frame_filename,current_duration)

#clip=VideoFileClip("C:\\Users\\User\\Desktop\\giraffes.mp4")
if __name__ == "__main__":
    import sys
    video_file="F:\Semesters\\Summer'22[222]\\CSE499A-Azk\\exploratory project work\\mr_bean.mp4"
    main(video_file)    

