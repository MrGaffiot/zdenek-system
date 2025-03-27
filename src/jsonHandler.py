import json


def read(file_path: str = "data/posts.json") -> dict:
    """Reads a JSON file and returns its contents as a dictionary."""
    with open(file_path, "r") as file:
        return json.load(file)


def write(data: list, file_path: str = "data/posts.json") -> None:
    """Writes a list of data to a JSON file, appending it to the existing data."""
    with open(file_path, "r+") as file:
        file_data = read(file_path)
        file_data["posts"].extend(data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.truncate()

if __name__ == "__main__":
    print(read)
    write([[input("> ") for i in range(3)]])
