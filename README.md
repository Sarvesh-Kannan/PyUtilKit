# PyUtilKit

A **multi-purpose Python utility package** that provides ready-to-use, frequently-needed helper functions for everyday coding tasks — saving time, reducing boilerplate, and improving code readability.

## 🚀 Installation

You can install PyUtilKit using pip:

```bash
pip install pyutilkit
```

## 🧩 Core Modules

PyUtilKit is organized into several modules, each focusing on specific utility functions:

### 1. `string_utils`

String manipulation and validation utilities.

```python
from pyutilkit.string_utils import to_snake_case, remove_punctuation, is_palindrome

# Case conversion
to_snake_case("HelloWorld")  # Output: "hello_world"
to_camel_case("hello_world")  # Output: "helloWorld"
to_pascal_case("hello-world")  # Output: "HelloWorld"

# String manipulation
remove_punctuation("Hello, world!")  # Output: "Hello world"
remove_digits("Hello123World")  # Output: "HelloWorld"
remove_whitespace("Hello   world", keep_single_spaces=True)  # Output: "Hello world"
truncate("Hello world", 8)  # Output: "Hello..."
pad_string("Hello", 10, pad_char="-", align="center")  # Output: "--Hello---"

# String validation
is_palindrome("racecar")  # Output: True
is_anagram("listen", "silent")  # Output: True
```

### 2. `file_utils`

File and directory management utilities.

```python
from pyutilkit.file_utils import read_json, write_csv, get_file_size

# File I/O
data = read_json("data.json")
write_csv("output.csv", data, delimiter=",")
content = read_text("file.txt", encoding="utf-8")
write_text("output.txt", "Hello, world!", append=True)

# File metadata
size = get_file_size("large_file.txt", unit="MB")  # Get size in megabytes
last_modified = get_last_modified_time("file.txt", as_datetime=True)
extension = get_file_extension("document.pdf", with_dot=False)  # Output: "pdf"

# File management
create_file("new_file.txt", "Initial content")
create_directory("new_directory", exist_ok=True)
rename_file("old_name.txt", "new_name.txt", overwrite=False)
delete_file("temp.txt", missing_ok=True)
merge_csv_files(["part1.csv", "part2.csv"], "merged.csv")
merge_json_files(["config1.json", "config2.json"], "merged.json", merge_mode="merge_objects")
```

### 3. `math_utils`

Mathematical utilities and statistics.

```python
from pyutilkit.math_utils import safe_divide, mean, is_prime

# Arithmetic
safe_divide(10, 0, default=0)  # Output: 0
percent_change(100, 150)  # Output: 50.0
normalized = normalize([1, 2, 3, 4, 5])  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
z_scores = z_score([2, 4, 6])  # Output: [-1.0, 0.0, 1.0]

# Statistics
mean([1, 2, 3, 4, 5])  # Output: 3.0
median([1, 3, 5, 7, 9])  # Output: 5
mode([1, 2, 2, 3, 3, 3, 4])  # Output: 3
std_dev = standard_deviation([1, 2, 3, 4, 5])  # Population standard deviation

# Number theory
is_prime(17)  # Output: True
factorial(5)  # Output: 120
gcd(8, 12)  # Output: 4
lcm(4, 6)  # Output: 12
```

### 4. `list_utils`

List manipulation and analysis utilities.

```python
from pyutilkit.list_utils import flatten, chunk, get_frequency

# List manipulation
flatten([1, [2, 3], [4, [5, 6]]])  # Output: [1, 2, 3, 4, 5, 6]
chunked = chunk([1, 2, 3, 4, 5, 6, 7], 3)  # Output: [[1, 2, 3], [4, 5, 6], [7]]
unique = remove_duplicates([1, 2, 2, 3, 1, 4])  # Output: [1, 2, 3, 4]

# List analysis
freq = get_frequency([1, 2, 2, 3, 1, 3, 3, 4])  # Output: {1: 2, 2: 2, 3: 3, 4: 1}
most_common = most_frequent([1, 2, 2, 3, 1, 3, 3, 4], n=2)  # Output: [(3, 3), (1, 2)]
least_common = least_frequent([1, 2, 2, 3, 1, 3, 3, 4], n=1)  # Output: [(4, 1)]

# List transformation
str_list = to_string_list([1, 2.5, True, None])  # Output: ['1', '2.5', 'True', 'None']
int_list = to_int_list(['1', '2', '3'])  # Output: [1, 2, 3]
float_list = to_float_list(['1', '2.5', '3'])  # Output: [1.0, 2.5, 3.0]
```

## 📖 Full Documentation

For complete documentation of all functions and examples, visit [https://github.com/Sarvesh-Kannan/PyUtilKit](https://github.com/Sarvesh-Kannan/PyUtilKit).

## 🧪 Testing

PyUtilKit includes a comprehensive test suite. To run the tests:

```bash
# Install pytest if you don't have it
pip install pytest

# Run tests
pytest -v
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📬 Contact

Sarvesh Kannan - [your.email@example.com](mailto:sarveshkannan30@gmail.com)

Project Link: [https://github.com/Sarvesh-Kannan/PyUtilKit](https://github.com/Sarvesh-Kannan/PyUtilKit) 
