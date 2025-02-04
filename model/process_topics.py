import json

# File paths
txt_file = "data/nave/topics.txt"
json_file = "data/nave/topics.json"

# Define the field names for the JSON structure
fields = ["topic_name", "vector"]

# Read and process the text file
data = []
with open(txt_file, 'r') as file:
    for line in file:
        values = line.strip().split('\t')
        entry = {
            "topic_name": values[1],
            "vector": None
        }
        data.append(entry)

# Write to JSON file
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Conversion completed. JSON saved to {json_file}")
