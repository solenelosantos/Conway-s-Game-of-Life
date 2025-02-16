# Standart
import argparse
from pathlib import Path

# Default values
DEFAULT_WIDTH= 400
DEFAULT_HEIGHT= 400
DEFAULT_CELL_SIZE=4

def cmd_line()-> argparse.Namespace:
    """Read command line arguments."""
    # Create parser & set description
    parser = argparse.ArgumentParser(description="Some description.")

    # Files arguments
    parser.add_argument("-i", "--input_file", type=Path,
                        help="Set the path to the initial pattern file",
                        default="my_initial_file.txt")
    parser.add_argument("-o", "--output_file", type=Path,
                        help="Set the path to the output file,contains the final state",
                        default="my_output_file.txt")

    # FPS
    parser.add_argument("--fps", type= int,
                        help= "The number of frames per second to use with pygame",
                        default=20)

    # Game options
    parser.add_argument("-d", type=bool,
                        help="Display flag : launch Pygame and the simulation.",
                        default=True)
    parser.add_argument("-m", type= int,
                        help="Set the number of steps to run.",
                        default= 500)

    # Size of the screen and cells
    parser.add_argument("-W","--width", type=int,
                        help="The width of the pygame screen",
                        default=DEFAULT_WIDTH)
    parser.add_argument("-H", "--height", type=int,
                        help="The height of the pygame screen",
                        default=DEFAULT_HEIGHT)
    parser.add_argument("--cell_size", type = int,
                        help= "The size of a cell",
                        default=DEFAULT_CELL_SIZE)

    return parser.parse_args()
