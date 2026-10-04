# project_8.py
# NumPy Analyzer

A beginner-friendly **NumPy Analyzer** built in Python using **Object-Oriented Programming (OOP)**.

This project provides an interactive menu-driven program for creating and analyzing **1D, 2D, and 3D NumPy arrays**.

---

## 📌 Project Overview

The NumPy Analyzer allows users to perform different NumPy operations through a simple menu-driven terminal program.

### Main Features

* Create 1D, 2D and 3D NumPy arrays
* Perform array indexing
* Perform array slicing
* Perform mathematical operations
* Combine arrays
* Split arrays
* Search values
* Sort arrays
* Filter array values
* Calculate statistical values
* Calculate correlation coefficient
* Handle invalid user input
* Demonstrate Python OOP concepts

---

## 🚀 Features

### 1. Create NumPy Arrays

The program supports:

* 1D Array
* 2D Array
* 3D Array

Users can enter the dimensions and values directly through the terminal.

---

### 2. Indexing

The program supports indexing for different types of arrays.

For example:

```python
array[index]
```

For a 2D array:

```python
array[row, column]
```

For a 3D array:

```python
array[depth, row, column]
```

---

### 3. Slicing

The project supports array slicing.

For a 1D array:

```python
array[start:end]
```

For a 2D array:

```python
array[row_start:row_end, column_start:column_end]
```

---

### 4. Mathematical Operations

The program provides the following operations:

* Addition
* Subtraction
* Multiplication
* Division
* Dot Product

It also checks for division by zero.

---

### 5. Combine and Split Arrays

The project allows users to combine arrays using:

```python
np.vstack()
```

Arrays can also be split using:

```python
np.array_split()
```

---

### 6. Search, Sort and Filter

The analyzer provides:

#### Search

Search for a particular value using:

```python
np.where()
```

#### Sorting

Arrays can be sorted in:

* Ascending order
* Descending order

Using:

```python
np.sort()
```

#### Filtering

Users can filter values using conditions such as:

```text
> 30
< 30
>= 30
<= 30
```

---

### 7. Aggregate and Statistical Operations

The project supports:

* Sum
* Mean
* Median
* Standard Deviation
* Variance
* Minimum
* Maximum
* Percentile
* Correlation Coefficient

Examples of NumPy functions used:

```python
np.sum()
np.mean()
np.median()
np.std()
np.var()
np.min()
np.max()
np.percentile()
np.corrcoef()
```

---

# 🧑‍💻 OOP Concepts Used

This project uses Object-Oriented Programming.

## Class

The main class is:

```python
class DataAnalytics:
```

The class is responsible for managing and analyzing NumPy arrays.

## Constructor

The constructor initializes the array:

```python
def __init__(self, array=None):
```

If no array is provided, an empty NumPy array is created.

## Private Methods

The project uses private methods for internal operations:

```python
__validate_array()
__display_array()
```

## Class Method

A class method is used to create an object from a list:

```python
@classmethod
def from_list(cls, values):
```

## Static Method

A static method is used to get the installed NumPy version:

```python
@staticmethod
def get_numpy_version():
```

---

# 🛠️ Technologies Used

* Python 3
* NumPy
* Object-Oriented Programming
* Command Line / Terminal

---

# 📥 Installation

## 1. Install Python

Make sure Python 3 is installed.

Check the Python version:

```bash
python --version
```

## 2. Install NumPy

Run:

```bash
pip install numpy
```

Check NumPy installation:

```bash
python -c "import numpy; print(numpy.__version__)"
```

---

# ▶️ How to Run

Open the project folder in VS Code or Terminal.

Run the Python file:

```bash
python numpy_analyzer.py
```

The program will display:

```text
========================================
Welcome to the NumPy Analyzer!
========================================

Choose an option:
1. Create a NumPy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
```

Select an option by entering its number.

---

# 📋 Main Menu

| Option | Description                       |
| ------ | --------------------------------- |
| 1      | Create a NumPy Array              |
| 2      | Perform Mathematical Operations   |
| 3      | Combine or Split Arrays           |
| 4      | Search, Sort, or Filter Arrays    |
| 5      | Compute Aggregates and Statistics |
| 6      | Exit                              |

---

# 🔢 NumPy Functions Used

Important NumPy functions used in this project:

```python
np.array()
np.reshape()
np.vstack()
np.array_split()
np.where()
np.sort()
np.any()
np.dot()
np.sum()
np.mean()
np.median()
np.std()
np.var()
np.min()
np.max()
np.percentile()
np.corrcoef()
```

---

# ⚠️ Error Handling

The project handles different types of invalid inputs, including:

* Invalid numbers
* Incorrect number of elements
* Invalid array dimensions
* Index out of range
* Invalid slicing input
* Division by zero
* Invalid percentile
* Invalid menu choices

The program uses `try` and `except` to handle errors and prevent the program from crashing.

---

# 📁 Project Structure

```text
NumPy-Analyzer/
│
├── numpy_analyzer.py
│
└── README.md
```

> If your Python file has a different name, replace `numpy_analyzer.py` with your actual file name.

---

# 🎯 Learning Objectives

This project helps in understanding and practicing:

* NumPy arrays
* 1D arrays
* 2D arrays
* 3D arrays
* Array indexing
* Array slicing
* Array reshaping
* Mathematical operations
* Searching arrays
* Sorting arrays
* Filtering arrays
* Combining arrays
* Splitting arrays
* Statistical operations
* Correlation
* Exception handling
* Python OOP
* Class
* Object
* Constructor
* Private methods
* Class methods
* Static methods

---

# 🔮 Future Improvements

Some possible improvements for this project:

* Add matrix multiplication for 2D arrays
* Add more NumPy operations
* Add CSV file support
* Add Matplotlib visualization
* Add a graphical user interface
* Add unit testing
* Improve input validation
* Add more advanced statistical functions

---

# 👨‍💻 Author

**Hitesh**

---

# 📄 License

This project is created for **learning and educational purposes**.
