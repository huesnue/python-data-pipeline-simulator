class DataSource:
    def __init__(self, path: str):
        self.path = path

    def load(self):
        raise NotImplementedError("load() must be implemented by subclasses or extended.")
