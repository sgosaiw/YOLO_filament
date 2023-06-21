import sys
from moviepy.editor import *

def adjust_gamma(image_array, gamma):
    return image_array**(1/gamma)

def convert_gif_adjust_gamma(gif_path, output_path, gamma):
    clip = VideoFileClip(gif_path)
    gray_clip = clip.fx(vfx.blackwhite)
    gamma_clip = gray_clip.fl_image(lambda img: adjust_gamma(img, gamma))
    gamma_clip.write_videofile(output_path, codec="libx264")

# Usage
if len(sys.argv) < 4:
    print("Please provide input filename, output filename, and gamma value as command-line arguments.")
else:
    gif_filename = sys.argv[1]
    output_filename = sys.argv[2]
    gamma_value = float(sys.argv[3])
    gif_path = os.path.join(os.getcwd(), gif_filename)
    output_path = os.path.join(os.getcwd(), output_filename)
    convert_gif_adjust_gamma(gif_path, output_path, gamma_value)
