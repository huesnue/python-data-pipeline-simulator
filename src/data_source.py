import json
import csv
import os

class DataSource:
    def __init__(self, path: str):
        self.path = path

    def load(self):
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
