class PipelineManager:
    def __init__(self, source, validator, transformer):
        self.source = source
        self.validator = validator
        self.transformer = transformer

    def run(self):
        raise NotImplementedError("run() must be implemented.")
