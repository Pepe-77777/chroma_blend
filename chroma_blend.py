#!/usr/bin/env python3

'''
The main module of the chroma_blend package.
(Improved, and adheres to OOP principles)
'''

import os
import argparse
import shutil
import cv2
from cblend_modules.colorizer import BColors as fontc
from cblend_modules.colorizer import Colorizer
from cblend_modules.vid2pngs import Vid2PNGs


class CBlend:

    def __init__(self: object): # Initialize (Think: A constructor)
        # Currently, there are no variables
        # that are shared between methods. 
        # No need for class-wide variables yet.
        pass





    def folders_manager(self: object): # No input
        '''
        Manages the folders required
        for the operations. If they're there, folders are cleaned.
        If not, the folders are created.
        '''
        if not os.path.isdir("bw_frames"):
            print(
                fontc.YELLOW +
                "Creating folder: bw_frames. This will contain the black and white frames." +
                fontc.ENDC)
            os.mkdir("bw_frames")
        else:
            print("bw_frames directory found. Clearing contents..")
            shutil.rmtree('bw_frames/')
            os.mkdir("bw_frames")

        if not os.path.isdir("source_frames"):
            print(
                fontc.YELLOW +
                "Creating folder: bw_folder. This will contain the colored source frames." +
                fontc.ENDC)
            os.mkdir("source_frames")
        else:
            print("source_frames directory found. Clearing contents..")
            shutil.rmtree('source_frames/')
            os.mkdir("source_frames")

        if not os.path.isdir("output_frames"):
            print(
                fontc.YELLOW +
                """Creating folder: output_frames.
                This will contain the final higher-res colored frames.
                """
                + fontc.ENDC)
            os.mkdir("output_frames")
        else:
            print("output_frames directory found. Clearing contents..")
            shutil.rmtree('output_frames/')
            os.mkdir("output_frames")

def main ():
    '''
    Main function of chroma_blend.py
    Manages provded arguments, runs folder checks, calls other modules.
    '''

    # First objective of main is to collected provided arguments.
    # It'll hold them, initalize a chroma_blend object, and then give it the held arguments.

    source_frames_count = 0
    bw_frames_count = 0
    loop_len_count = 0

    print(fontc.OKBLUE + "Cblend activated." + fontc.ENDC)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "bw_vid_input",
        help="The black and white .mp4 input to blend colors on.")
    parser.add_argument(
        "colored_vid_input",
        help="The .mp4 with the chroma that you want to blend the b&w mp4's luma on.")
    user_input = parser.parse_args()


    cblend_instance = CBlend()

    # Check if all directories are in place.
    # If they're not there, they're created
    # If they're already there, clear them.
    cblend_instance.folders_manager()


    v2p_instance = Vid2PNGs()
    source_frames_count = v2p_instance.frame_extract(user_input.colored_vid_input, "source_frames")
    bw_frames_count = v2p_instance.frame_extract(user_input.bw_vid_input, "bw_frames")


    print(
        fontc.CYAN +
        "Colored frames counted: " +
        fontc.ENDC +
        str(source_frames_count))
    print(
        fontc.WHITE +
        "Black and white frames counted: " +
        fontc.ENDC +
        str(bw_frames_count))

    if source_frames_count != bw_frames_count:
        print(
            fontc.YELLOW +
            "Warning: Inconsistent number of frames. Some frames will not be generated." +
            fontc.ENDC)
    else:
        loop_len_count = source_frames_count

    if source_frames_count < bw_frames_count:
        loop_len_count = source_frames_count
    elif bw_frames_count < source_frames_count:
        loop_len_count = bw_frames_count


    for counter in range(loop_len_count + 1):

        bw_name = "bw_frames/" + str(counter) + ".png"
        cl_name = "source_frames/" + str(counter) + "_c.png"
        final_name = "output_frames/" + str(counter) + "_f.png"
        #print("File names are: " + bw_name + " and " +  cl_name)

        colblend_instance = Colorizer()
        final_output = colblend_instance.color_blend(bw_name, cl_name)
        final_output.save(final_name)

    print("Cleaning up extracted frames...")
    shutil.rmtree('bw_frames/')

    print("All done!")


if __name__ == "__main__":
    main()
