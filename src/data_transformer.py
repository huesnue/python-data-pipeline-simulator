class DataTransformer:
    def transform(self, data):
        # Example: Create a new field
        if "name" in data and "city" in data:
            data["full_info"] = f"{data['name']} from {data['city']}"
        
        return data

