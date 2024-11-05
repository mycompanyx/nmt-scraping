import json

# Load the JSON file
file_path = 'data/segmented_phrases.json'  # Replace with the actual file path


# Load the JSON data from the file
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Initialize a counter for the total number of phrases
phrase_count = 0

# Loop through each item in the data and count the phrases
for item in data:
    phrase_count += len(item["phrases"])

# Print the total number of phrases
print(f"Total number of phrases: {phrase_count}")
