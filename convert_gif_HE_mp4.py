import sys
import cv2
from moviepy.editor import *

def equalize_histogram(image):
    img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    equalized_image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    return equalized_image

def convert_gif_histogram_equalization(gif_path, output_path):
    clip = VideoFileClip(gif_path)
    equalized_clip = clip.fl_image(equalize_histogram)
    equalized_clip.write_videofile(output_path, codec="libx264")

# Usage
if len(sys.argv) < 3:
    print("Please provide input filename and output filename as command-line arguments.")
else:
    gif_filename = sys.argv[1]
    output_filename = sys.argv[2]
    gif_path = os.path.join(os.getcwd(), gif_filename)
    output_path = os.path.join(os.getcwd(), output_filename)
    convert_gif_histogram_equalization(gif_path, output_path)
