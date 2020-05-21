A workaround to DeepRemaster's low resolution limitation.

Since Satoshi Iizuka's DeepRemaster functions well only with small videos (432 x 320), a solution for coloring higher resolution videos is to extract the chroma from the small video and layer it over the larger-sized black and white video.

The program takes two inputs: The original black and white mp4, and the colored mp4 output from DeepRemaster. The output is a folder of all the video frames, with the color transferred over to the original black and white frames.

Usage: python3 chroma_blend.py [black_and_white.mp4] [colorized.mp4]


Since this program as a whole relies on two smaller modules, the modules themselves can be used as standalone programs.
The modules located in the "cblend_modules" directory are:

colorizer.py - For colorizing the frames. Usage: python3 colorizer.py [bw_image] [colorized_image]

vid2pngs.py - For splitting videos into pngs. A directory is created for the output pngs. Usage: python3 vid2pngs.py [input_video]




