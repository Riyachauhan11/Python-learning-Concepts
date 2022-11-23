from abc import ABC, abstractmethod


class TextReaderAbstract(ABC):

    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    @abstractmethod  # this is just an interface or "RULE"
    def get_path(self):
        pass

    @abstractmethod
    def get_filename(self):
        pass


class TextReader(TextReaderAbstract):

    def get_path(self):
        return self.path

    def get_filename(self):
        return self.filename


myobj = TextReader("/users/download", 'SAMPLE.txt')
print(myobj.get_filename())
print(myobj.get_path())
