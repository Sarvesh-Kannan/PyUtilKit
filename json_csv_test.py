"""
Test script for JSON and CSV operations in PyUtilKit.
This script creates sample data files and processes them.
"""
import os
import json
import csv
import tempfile

# Create a temporary directory for our tests
temp_dir = tempfile.mkdtemp(prefix="json_csv_test_")
print(f"Working in temporary directory: {temp_dir}")

# Create sample JSON data
sample_data = [
    {"name": "Alice", "age": 28, "city": "New York"},
    {"name": "Bob", "age": 35, "city": "Boston"},
    {"name": "Charlie", "age": 42, "city": "Chicago"}
]

# Create a sample JSON file
json_file = os.path.join(temp_dir, "data.json")
with open(json_file, 'w') as f:
    json.dump(sample_data, f, indent=2)
print(f"Created sample JSON file: {json_file}")

try:
    # Try to use PyUtilKit's file_utils
    from pyutilkit.file_utils import read_json, write_csv
    
    # Read the JSON data
    print("\n--- Using PyUtilKit functions ---")
    data = read_json(json_file)
    print(f"Data read from JSON: {data}")
    
    # Write to CSV
    csv_file = os.path.join(temp_dir, "output.csv")
    write_csv(csv_file, data)
    print(f"Data written to CSV: {csv_file}")
    
    # Display CSV contents
    print("\nCSV file contents:")
    with open(csv_file, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    
except ImportError:
    print("\n--- PyUtilKit functions not available, using standard library ---")
    # Fallback to standard library if functions aren't implemented
    
    # Read JSON
    with open(json_file, 'r') as f:
        data = json.load(f)
    print(f"Data read from JSON: {data}")
    
    # Write CSV
    csv_file = os.path.join(temp_dir, "output.csv")
    with open(csv_file, 'w', newline='') as f:
        # Get field names from the first record
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(data)
    print(f"Data written to CSV: {csv_file}")
    
    # Display CSV contents
    print("\nCSV file contents:")
    with open(csv_file, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# Clean up
print("\n--- Cleaning up ---")
try:
    for file in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, file))
    os.rmdir(temp_dir)
    print(f"Removed temporary directory: {temp_dir}")
except Exception as e:
    print(f"Note: Could not completely clean up: {e}")

print("\nJSON/CSV test completed!") 