from pathlib import Path

def open_file():
    path = Path(__file__).parent
    path = path / "sample_path" / "dummy.txt"

    try:
        file = path.open("r")
        content = file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print(f"{path} does not exist")
    except Exception as e:
        print(f"Unexpected error occurred : {e}")


def main():
    open_file()


if __name__ == "__main__":
    main()

# Output
# E:\file_errors\sample_path\dummy.txt does not exist
