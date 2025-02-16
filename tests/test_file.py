# Import
from jeu.cmd_line import cmd_line


def test_initial_file_not_empty() -> None:
    """Test if the initial file is empty."""
    args= cmd_line()

    with open(args.input_file) as f:
        n= len(f.read())
    assert n>0

def test_output_file_not_empty() -> None:
    """Test if the initial file is empty."""
    args= cmd_line()

    with open(args.output_file) as f:
        n= len(f.read())
    assert n>0