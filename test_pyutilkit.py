"""
Test script for PyUtilKit library.
This script demonstrates the usage of various utility functions from the PyUtilKit package.
"""

# Import the package version to confirm it's installed correctly
from pyutilkit import __version__, __author__
print(f"PyUtilKit version: {__version__}")
print(f"PyUtilKit author: {__author__}")
print("-" * 50)

# Test string utilities
print("Testing string_utils:")
from pyutilkit.string_utils import to_snake_case, to_camel_case, remove_punctuation, is_palindrome

snake_case = to_snake_case("HelloWorld")
print(f"to_snake_case('HelloWorld'): {snake_case}")

camel_case = to_camel_case("hello_world")
print(f"to_camel_case('hello_world'): {camel_case}")

no_punctuation = remove_punctuation("Hello, world!")
print(f"remove_punctuation('Hello, world!'): {no_punctuation}")

palindrome_check = is_palindrome("racecar")
print(f"is_palindrome('racecar'): {palindrome_check}")
print("-" * 50)

# Test math utilities
print("Testing math_utils:")
from pyutilkit.math_utils import safe_divide, mean, is_prime

result = safe_divide(10, 2)
print(f"safe_divide(10, 2): {result}")

safe_result = safe_divide(10, 0, default="Error: Division by zero")
print(f"safe_divide(10, 0, default='Error: Division by zero'): {safe_result}")

mean_result = mean([1, 2, 3, 4, 5])
print(f"mean([1, 2, 3, 4, 5]): {mean_result}")

prime_check = is_prime(17)
print(f"is_prime(17): {prime_check}")
print("-" * 50)

# Test list utilities
print("Testing list_utils:")
from pyutilkit.list_utils import flatten, chunk, remove_duplicates

flat_list = flatten([1, [2, 3], [4, [5, 6]]])
print(f"flatten([1, [2, 3], [4, [5, 6]]]): {flat_list}")

chunked_list = chunk([1, 2, 3, 4, 5, 6, 7], 3)
print(f"chunk([1, 2, 3, 4, 5, 6, 7], 3): {chunked_list}")

unique_items = remove_duplicates([1, 2, 2, 3, 1, 4])
print(f"remove_duplicates([1, 2, 2, 3, 1, 4]): {unique_items}")
print("-" * 50)

print("All tests completed successfully!") 