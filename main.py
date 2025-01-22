#read data from yaml file
import yaml
import sys
from rich.console import Console

console = Console()

def load_yaml_file(file_path):
    try:
        with open(file_path, 'r') as stream:
            return yaml.safe_load(stream)
    except FileNotFoundError:
        console.print(f"Error: File '{file_path}' not found.")
        return None
    except yaml.YAMLError as e:
        console.print(f"Error: Failed to load YAML file '{file_path}': {e}")
        return None

def main():
    if len(sys.argv) != 2:
        console.print("Error: Please provide the YAML file path as a command-line argument.")
        return

    file_path = sys.argv[1]
    yaml_data = load_yaml_file(file_path)

    if yaml_data is None:
        return

    for key, value in yaml_data.items():
        console.print(key + " : " + str(value))

if __name__ == "__main__":
    main()

#in terminal : python .\main.py basic.yaml