from fileinput import filename
import moviepy.editor as mpy
import numpy as np
import os
import sys

image_folder=r"F:\Semesters\\Summer'22[222]\\CSE499A-Azk\exploratory project work\\animals\\giraffes-moviepy"
fps=1
image_files=[image_folder+'/'+img for img in os.listdir(image_folder) if img.endswith(".jpg")]
clip=mpy.ImageSequenceClip(image_files,fps=1)
clip.write_videofile("F:\Semesters\Summer'22[222]\CSE499A-Azk\exploratory project work\giraffes2.mp4",audio=False)
