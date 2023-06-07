from abc import ABC, abstractmethod


class IFileReader(ABC):
    @abstractmethod
    def read(self):
        pass


class AMSFileReader(IFileReader):
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""

    def read(self):
        with open(self.file_path, 'r') as file:
            self.content = file.read()
        return self.content


class FileReaderFactory:
    @staticmethod
    def create(file_path):
        if file_path.endswith(".ams"):
            return AMSFileReader(file_path)
        raise ValueError("Invalid file format. Only 'ams' files are supported.")

