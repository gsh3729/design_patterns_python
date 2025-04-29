'''
defines the skeleton of an algorithm in a base class, 
allowing subclasses to override specific steps of the algorithm without changing its overall structure.
'''

from abc import ABC, abstractmethod

class FileProcessor(ABC):
    def process_file(self, filepath):
        self.open_file(filepath)
        content = self.read_content()
        result = self.process_content(content)
        self.close_file()
        return result

    def open_file(self, filepath):
        self.file = open(filepath, 'r')
        print(f"Opened {filepath}")

    def read_content(self):
        print("Reading content")
        return self.file.read()

    @abstractmethod
    def process_content(self, content):
        pass

    def close_file(self):
        self.file.close()
        print("Closed file")

import csv
from io import StringIO

class CSVProcessor(FileProcessor):
    def process_content(self, content):
        print("Processing CSV content")
        reader = csv.reader(StringIO(content))
        return [row for row in reader]

import json

class JSONProcessor(FileProcessor):
    def process_content(self, content):
        print("Processing JSON content")
        return json.loads(content)

# Assume "sample.csv" and "sample.json" exist with appropriate content
csv_proc = CSVProcessor()
csv_data = csv_proc.process_file('sample.csv')
print(csv_data)

json_proc = JSONProcessor()
json_data = json_proc.process_file('sample.json')
print(json_data)
