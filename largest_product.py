# Task A: Create the largest series product with an example fixed length of 3

series = "63915"

series1 = series[0:3]
series2 = series[1:4]
series3 = series[2:5]

product1 = int(series1[0]) * int(series1[1]) * int(series1[2])
product2 = int(series2[0]) * int(series2[1]) * int(series2[2])
product3 = int(series3[0]) * int(series3[1]) * int(series3[2])

# Use max (built-in python function) to obtain the largest product value
largest_product = max(product1, product2, product3)

print(f"Did you know that the largest product of a series with 3 consecutive digits in {series} is", largest_product,"?")



# Task B + Bonus Task: Create a largest series product calculator with user input

print("Find out what is the largest product of a series of numbers here!")

from math import prod
import traceback
import time

def lp(series, n):
    # Remove negative sign and split series into individual digits
    series_digits = [int(char) for char in series if char.isdigit()]
    
    if n > len(series_digits):
        raise ValueError("Length of series has exceeded the number of digits in the sequence. Please try again!")
    if n < 0:
        raise ValueError("This cannot be negative! Please try again.")
    if n == 0:
        raise ValueError("Length cannot be zero. Please try again!")
    
    # Simulate processing delay
    print("Calculating...")
    time.sleep(1.6)
    
    return max(
        prod(series_digits[i:i+n])
        for i in range(len(series_digits) - n + 1)
    )

def main():
    while True:
        try:
            # Loop to handle series input
            while True:
                try:
                    series = input("Enter a sequence of digits to be analysed: ")
                    if not series.isdigit() or int(series) <= 0:
                        raise ValueError("Invalid characters spotted! Numbers only... Try again!")
                    break  # Break loop if no error
                except ValueError as e:
                    print(e)
                    traceback.print_exc()
            
            # Loop to handle length input
            while True:
                try:
                    length = input("Please enter the desired length of series: ")
                    if not length.isdigit() or int(length) <= 0:
                        raise ValueError("Length must be at least 1. Please try again!")
                    length = int(length)  # Convert length to integer
                    
                    # Validate the length input using the lp function
                    result = lp(series, length)
                    print(f"The highest product of any {length} consecutive digits in the sequence {series} is {result}. Fascinating, isn't it?")
                    break  # Break loop if no error
                except ValueError as e:
                    print(e)
                    traceback.print_exc()
            
            # Prompt to calculate again
            again = input("Enter 'yes' to continue: ")
            if again.lower() != 'yes':
                raise ValueError("Invalid key! Enter 'yes' to start over.")
        
        except ValueError as e:
            print(e)
            traceback.print_exc()
            break  # Exit the loop on error

if __name__ == "__main__":
    main()
