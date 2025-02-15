

class Pattern:
    def __init__(self, pattern: list[list[int]]):
        self._pattern= [[0]*(100) for _ in range(100)]
        self.place_pattern(pattern)

    def place_pattern(self, pattern):
        """Place le pattern au centre de la grille"""
        width, height = len(pattern[0]), len(pattern)
        for x in range(height):
            for y in range(width):
                new_x = x + (100 - height) // 2
                new_y = y + (100 - width) // 2
                if 0 <= new_x < 100 and 0 <= new_y < 100:
                    self._pattern[new_x][new_y] = pattern[x][y]
                else:
                    print(f" Problème d'indexation : ({new_x}, {new_y}) hors limites")


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
