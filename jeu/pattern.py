from .cmd_line import cmd_line

class Pattern:
    def __init__(self, pattern: list[list[int]]):
        args=cmd_line()
        self._pattern= [[0]*args.width for _ in range(args.height)]
        width, height= len(pattern[0]), len(pattern)
        for x in range(height):
            for y in range(width):
                self._pattern[x+int((args.width-width)/2)][y+int((args.height-height)/2)]=pattern[x][y]


    def get_pattern(self) -> list[list[int]]:
        return self._pattern
    

    @staticmethod
    def load(filename: str = "my_initial_file.txt") -> "Pattern":
        """Load pattern from a text file or create a file with default pattern if it doesn't exist."""
        try:
            with open(filename, "r") as f:
                # Read lines and convert convert it into a list of lists of integers.
                initial_pattern = [[int(char) for char in line.strip()] for line in f if line.strip()]
                if not initial_pattern:  # Vérifier si le fichier était vide
                    print("File exists but is empty. Creating default pattern.")
                    return Pattern.default()
                return Pattern(initial_pattern)
        except FileNotFoundError:
            print(f"File {filename} not found, creating a new file with default initial pattern.")  # Debug
            # If the file doesn't exist, create one with default initial pattern
            return Pattern.default()
        

    @staticmethod
    def default() -> "Pattern":
        """Return a default instance with predefined initial pattern."""
        return Pattern(
            pattern=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
            )
