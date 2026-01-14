class DataTransformer:
    def transform(self, data):
        if not isinstance(data, dict):
            raise ValueError("Transformer expects a dictionary as input.")
        try:
            # Example: Create a new field
            if "name" in data and "city" in data:
                data["full_info"] = f"{data['name']} from {data['city']}"
        except Exception as e:
            raise RuntimeError(f"Error during transformation: {e}")
        
        return data

