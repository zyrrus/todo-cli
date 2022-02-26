import json
import pathlib


class Storage:
    def __init__(self, path_to_data):
        self.path = path_to_data  # Use pathlib
        self.data = self.load_data()

    def load_data(self):
        with open(self.path, "r") as input_file:
            return json.load(input_file)

    def save_data(self):
        data = json.dumps(self.data, indent=4)

        with open(self.path, "w") as output_file:
            output_file.write(data)
