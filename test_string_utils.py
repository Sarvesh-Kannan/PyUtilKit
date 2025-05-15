"""
Test script for PyUtilKit string utilities.
This script tests all the string manipulation functions mentioned in the example.
"""

print("Testing all string utility functions in PyUtilKit:")
print("-" * 60)

# Import all the required string utility functions
from pyutilkit.string_utils import (
    to_snake_case, to_camel_case, to_pascal_case,
    remove_punctuation, remove_digits, remove_whitespace,
    truncate, pad_string,
    is_palindrome, is_anagram
)

# Case conversion
print("Case Conversion:")
print(f"to_snake_case('HelloWorld'): {to_snake_case('HelloWorld')}")
print(f"to_camel_case('hello_world'): {to_camel_case('hello_world')}")
print(f"to_pascal_case('hello-world'): {to_pascal_case('hello-world')}")
print("-" * 60)

# String manipulation
print("String Manipulation:")
print(f"remove_punctuation('Hello, world!'): {remove_punctuation('Hello, world!')}")
print(f"remove_digits('Hello123World'): {remove_digits('Hello123World')}")
print(f"remove_whitespace('Hello   world', keep_single_spaces=True): {remove_whitespace('Hello   world', keep_single_spaces=True)}")
print(f"truncate('Hello world', 8): {truncate('Hello world', 8)}")
print(f"pad_string('Hello', 10, pad_char='-', align='center'): {pad_string('Hello', 10, pad_char='-', align='center')}")
print("-" * 60)

# String validation
print("String Validation:")
print(f"is_palindrome('racecar'): {is_palindrome('racecar')}")
print(f"is_anagram('listen', 'silent'): {is_anagram('listen', 'silent')}")
print("-" * 60)

print("All string utility tests completed!") 