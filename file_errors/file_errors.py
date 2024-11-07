from pathlib import Path

def open_file():
    path = Path(__file__).parent
    path = path / "sample_path" / "dummy.txt"
    path.open("r")


def main():
    open_file()

if __name__ == "__main__":
    main()