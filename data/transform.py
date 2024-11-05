import json

# Load the JSON data from the uploaded file
with open("data/output-beginner.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Define the output format
formatted_data = []

# Segment each item
for item in data:
    # Split the page content into sentences (phrases) using newline as a separator
    phrases = item["page_content"].split("\n - ")
    
    # Clean and format each phrase with the full context
    phrase_entries = [
        {
            "phrase": phrase.strip(),
            "context": item["page_content"].strip()
        }
        for phrase in phrases if phrase.strip()  # Ensure non-empty phrases
    ]
    
    # Construct the formatted item
    formatted_item = {
        "link_text": item["link_text"],
        "url": item["url"],
        "phrases": phrase_entries
    }
    
    # Add to the formatted data list
    formatted_data.append(formatted_item)

# Save the formatted data to a new JSON file
with open("data/beginner_output.json", "w", encoding="utf-8") as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)

print("Data has been segmented and saved to formatted_output.json")
