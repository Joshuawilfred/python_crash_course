# 0x04. Python - More Data Structures: Set, Dictionary

Python project by Guillaume.

This project covers the topic of sets and dictionaries in Python. It includes various tasks aimed at improving your understanding and usage of these data structures. By completing this project, you will gain knowledge and skills related to sets, dictionaries, lambda functions, and the map, reduce, and filter functions.

## Learning Objectives

Upon completing this project, you should be able to:

- Explain the awesomeness of Python programming
- Understand sets and their usage in Python
- Identify and use common methods of sets
- Differentiate between sets and lists
- Iterate over a set
- Understand dictionaries and their usage in Python
- Determine when to use dictionaries instead of lists or sets
- Understand keys in dictionaries
- Iterate over a dictionary
- Define lambda functions
- Utilize the map, reduce, and filter functions

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the project folder, is mandatory
- Your code should use the pycodestyle (version 2.8.\*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks

### 0. Squared simple

Write a function that computes the square value of all integers in a matrix.

- Prototype: `def square_matrix_simple(matrix=[]):`
- `matrix` is a 2-dimensional array
- Returns a new matrix:
  - Same size as `matrix`
  - Each value should be the square of the corresponding value in the input
- The initial matrix should not be modified
- You are not allowed to import any module

### 1. Search and replace

Write a function that replaces all occurrences of an element by another element in a new list.

- Prototype: `def search_replace(my_list, search, replace):`
- `my_list` is the initial list
- `search` is the element to replace in the list
- `replace` is the new element
- You are not allowed to import any module

### 2. Unique addition

Write a function that adds all unique integers in a list (once for each integer).

- Prototype: `def uniq_add(my_list=[]):`
- You are not allowed to import any module

### 3. Present in both

Write a function that returns a set of common elements in two sets.

- Prototype: `def common_elements(set_1, set_2):`
- You are not allowed to import any module

### 4. Only differents

Write a function that returns a set of all elements present in only one set.

- Prototype: `def only_diff_elements(set_1, set_2):`
- You are not allowed to import any module

### 5. Number of keys

Write a function that returns the number of keys in a dictionary.

- Prototype: `def number_keys(a_dictionary):`
- You are not allowed to import any module

### 6. Print sorted dictionary

Write a function that prints a dictionary by ordered keys.

- Prototype: `def print_sorted_dictionary(a_dictionary):`
- You can assume that all keys are strings
- Keys should be sorted in alphabetical order
- Only sort keys of the first level (don't sort keys of a dictionary inside the main dictionary)
- Dictionary values can have any type
