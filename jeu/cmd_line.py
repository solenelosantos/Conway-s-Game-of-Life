import argparse
from pathlib import Path

def cmd_line():
    parser = argparse.ArgumentParser(description='Some description.')
    parser.add_argument('-i', '--input_file', type=Path, help="Set the path to the initial pattern file", default="my_initial_file.txt")
    parser.add_argument('-o', '--output_file', type=Path, help="Set the path to the output file, contains the final state of our simulation", default="my_output_file.tx")
    parser.add_argument('-d', type=bool, help='Display flag. When enabled, pygame is enabled and we display each step of the simulation', default=True)
    parser.add_argument('--fps', type= int, help= 'The number of frames per second to use with pygame', default=10)
    parser.add_argument('-W','--width', type=int, help='The width of the pygame screen', default=800)
    parser.add_argument('-H', '--height', type=int, help='The height of the pygame screen', default=600)
    parser.add_argument('--cell_size', type = int, help= 'The size of a cell', default=10)

    args=parser.parse_args()
    return args
    