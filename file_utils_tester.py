"""
Test script for PyUtilKit file utilities.
This script demonstrates safe usage of file operations.
"""
import os
import json
import tempfile
from pathlib import Path

# Import the file utility functions
from pyutilkit.file_utils import (
    get_file_extension, create_file, create_directory, 
    delete_file, rename_file
)

# Try to import other functions, with fallbacks if they haven't been implemented
try:
    from pyutilkit.file_utils import read_json, write_json
    has_json_functions = True
except ImportError:
    has_json_functions = False
    print("Note: read_json/write_json functions not found, skipping those tests")

try:
    from pyutilkit.file_utils import read_text, write_text
    has_text_functions = True
except ImportError:
    has_text_functions = False
    print("Note: read_text/write_text functions not found, skipping those tests")

try:
    from pyutilkit.file_utils import get_file_size, get_last_modified_time
    has_metadata_functions = True
except ImportError:
    has_metadata_functions = False
    print("Note: file metadata functions not found, skipping those tests")

# Create a temporary directory for our tests
temp_dir = tempfile.mkdtemp(prefix="pyutilkit_test_")
print(f"Created temporary directory for tests: {temp_dir}")

# Test file extension functions
print("\n--- Testing file extension functions ---")
pdf_ext = get_file_extension("document.pdf", with_dot=False)
print(f"get_file_extension('document.pdf', with_dot=False): {pdf_ext}")
jpg_ext = get_file_extension("image.jpg", with_dot=True)
print(f"get_file_extension('image.jpg', with_dot=True): {jpg_ext}")

# Test file creation/directory functions
print("\n--- Testing file/directory creation ---")
test_dir = os.path.join(temp_dir, "test_dir")
create_directory(test_dir, exist_ok=True)
print(f"Created directory: {test_dir}")

test_file = os.path.join(temp_dir, "hello.txt")
create_file(test_file, "Hello, world!")
print(f"Created file: {test_file}")

# Test text file functions if available
if has_text_functions:
    print("\n--- Testing text file functions ---")
    content = read_text(test_file)
    print(f"read_text('{test_file}'): {content}")
    
    append_file = os.path.join(temp_dir, "append_test.txt")
    write_text(append_file, "First line\n")
    write_text(append_file, "Second line\n", append=True)
    content = read_text(append_file)
    print(f"Content after appending: {content}")

# Test JSON functions if available
if has_json_functions:
    print("\n--- Testing JSON functions ---")
    sample_data = {"name": "John", "age": 30, "city": "New York"}
    json_file = os.path.join(temp_dir, "sample.json")
    
    with open(json_file, 'w') as f:
        json.dump(sample_data, f)
    
    loaded_data = read_json(json_file)
    print(f"read_json('{json_file}'): {loaded_data}")
    
    # Modify and write back
    loaded_data["age"] = 31
    write_json(json_file, loaded_data)
    reloaded_data = read_json(json_file)
    print(f"Updated data: {reloaded_data}")

# Test file metadata functions if available
if has_metadata_functions:
    print("\n--- Testing file metadata functions ---")
    size = get_file_size(test_file)
    print(f"get_file_size('{test_file}'): {size} bytes")
    
    modified_time = get_last_modified_time(test_file)
    print(f"get_last_modified_time('{test_file}'): {modified_time}")

# Test file renaming
print("\n--- Testing file renaming ---")
renamed_file = os.path.join(temp_dir, "hello_renamed.txt")
rename_file(test_file, renamed_file)
print(f"Renamed {test_file} to {renamed_file}")
print(f"File exists after rename: {os.path.exists(renamed_file)}")

# Test file deletion
print("\n--- Testing file deletion ---")
delete_file(renamed_file)
print(f"Deleted file {renamed_file}")
print(f"File exists after deletion: {os.path.exists(renamed_file)}")

# Clean up the temporary directory
print("\n--- Cleaning up ---")
try:
    for root, dirs, files in os.walk(temp_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(temp_dir)
    print(f"Removed temporary directory: {temp_dir}")
except Exception as e:
    print(f"Note: Could not completely clean up temporary directory: {e}")

print("\nFile utility tests completed!") 