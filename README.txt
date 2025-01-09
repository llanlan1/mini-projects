Intro to my mini projects:

----------------------------------------------------------------------

ic_checker.py
## ID Checker for validity of NRIC/FIN (Singapore ID)

The IC Checker module validates Singapore NRIC (National Registration Identity Card) and FIN (Foreign Identification Number) using an official checksum algorithm. This script ensures IDs are accurate and conform to the required format.

### Features
- Validates NRIC and FIN numbers using prefix and checksum rules.
- Supports both NRIC (e.g., S1234567D) and FIN (e.g., G1234567Q) formats.
- Provides clear error messages for invalid or improperly formatted IDs.

### Use Case
Ideal for scenarios where quick and reliable validation of Singapore IDs is required, such as in personal projects, applications requiring user ID verification, or for learning purposes.

### Example in Python

from ic_checker import validate_id

id_number = "S1234567D"
if validate_id(id_number):
    print("Valid NRIC/FIN!")
else:
    print("Invalid NRIC/FIN.")


------------------------------------------------------------------------


largest_product.py
## LargestProductSeries

The `LargestProductSeries` module is designed to compute the largest product of `n` consecutive digits in a numeric series. This functionality can be applied to solve sequence-based problems efficiently.

### Features
- Calculates the product of any specified number of consecutive elements (`n`).
- Handles both numeric strings and arrays of integers.
- Validates input to ensure the series contains only digits or numbers.

### Use Case
Ideal for scenarios requiring maximum product calculations within a sliding window, such as solving Project Euler challenges or analyzing financial data trends.

### Example in Python

from largest_product_series import calculate_largest_product

series = "73167176531330624919225119674426574742355349194934"
n = 6
result = calculate_largest_product(series, n)
print(f"The largest product of {n} consecutive digits is: {result}")


