import logging
class DataTransformer:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        
    def transform(self, data):
        self.logger.info("Transforming data")
        
        if not isinstance(data, dict):
            self.logger.error("Transformer expects a dictionary as input.")
            raise ValueError("Transformer expects a dictionary as input.")
        try:
            # Example: Create a new field
            if "name" in data and "city" in data:
                data["full_info"] = f"{data['name']} from {data['city']}"
                self.logger.info("Added field 'full_info'")
        except Exception as e:
            self.logger.error(f"Error during transformation: {e}")
            raise RuntimeError(f"Error during transformation: {e}")
        
        return data

