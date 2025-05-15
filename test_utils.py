# Test script for PyUtilKit string utilities

# Import the package
import pyutilkit
print(f"PyUtilKit version: {pyutilkit.__version__}")

# Test case conversion functions
from pyutilkit.string_utils import to_snake_case
print(f"to_snake_case('HelloWorld'): {to_snake_case('HelloWorld')}")

# Try another function if it's implemented
try:
    from pyutilkit.string_utils import to_camel_case
    print(f"to_camel_case('hello_world'): {to_camel_case('hello_world')}")
except (ImportError, AttributeError):
    print("to_camel_case is not implemented yet")

# Try another function if it's implemented  
try:
    from pyutilkit.string_utils import to_pascal_case
    print(f"to_pascal_case('hello-world'): {to_pascal_case('hello-world')}")
except (ImportError, AttributeError):
    print("to_pascal_case is not implemented yet")

# Test string manipulation functions
try:
    from pyutilkit.string_utils import remove_digits
    print(f"remove_digits('Hello123World'): {remove_digits('Hello123World')}")
except (ImportError, AttributeError):
    print("remove_digits is not implemented yet")

try:
    from pyutilkit.string_utils import remove_whitespace
    print(f"remove_whitespace('Hello   world', keep_single_spaces=True): {remove_whitespace('Hello   world', keep_single_spaces=True)}")
except (ImportError, AttributeError):
    print("remove_whitespace is not implemented yet")

try:
    from pyutilkit.string_utils import truncate
    print(f"truncate('Hello world', 8): {truncate('Hello world', 8)}")
except (ImportError, AttributeError):
    print("truncate is not implemented yet")

try:
    from pyutilkit.string_utils import pad_string
    print(f"pad_string('Hello', 10, pad_char='-', align='center'): {pad_string('Hello', 10, pad_char='-', align='center')}")
except (ImportError, AttributeError):
    print("pad_string is not implemented yet")

# Test validation functions
try:
    from pyutilkit.string_utils import is_anagram
    print(f"is_anagram('listen', 'silent'): {is_anagram('listen', 'silent')}")
except (ImportError, AttributeError):
    print("is_anagram is not implemented yet")

print("Test completed!") 