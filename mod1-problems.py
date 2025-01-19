# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
# Print the iconic opening lines from Avatar: The Last Airbender
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")
# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
# Get two numbers from the user
first = float(input("What is your first number? "))
second = float(input("What is your second number? "))

# Perform basic arithmetic operations and print the results
print("Sum:", first + second)
print("Difference:", first - second)
print("Product:", first * second)
print("Quotient:", first / second)
# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
# Import the math module for the square root function
import math

# Get the lengths of the triangle's sides from the user
a = float(input("What is the length of the first side of your triangle? "))
b = float(input("What is the length of the second side of your triangle? "))
c = float(input("What is the length of the third side of your triangle? "))

# Calculate the semi-perimeter (s)
s = (a + b + c) / 2

# Calculate the area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Print the result
print("The area of the triangle is:", area)
# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
import math
import statistics

# Get input from the user
first = float(input("What is your first number? "))
second = float(input("What is your second number? "))
third = float(input("What is your third number? "))
fourth = float(input("What is your fourth number? "))
fifth = float(input("What is your fifth number? "))
numbers = (first, second, third, fourth, fifth)

# Calculate the statistics
total = sum(numbers)
average = statistics.mean(numbers)
minimum = min(numbers)
maximum = max(numbers)
range_ = maximum - minimum  # Corrected the range calculation 

# Calculate standard deviation
def calculate_std_dev(numbers):
  """Calculates the standard deviation of a list of numbers."""
  mean = sum(numbers) / len(numbers)
  variance = sum([((x - mean) ** 2) for x in numbers]) / len(numbers)
  std_dev = math.sqrt(variance)
  return std_dev

std_dev = calculate_std_dev(numbers)

# Print the results
print("Total:", total)
print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)  # Added maximum to the output
print("Range:", range_)
print("Standard Deviation:", std_dev)
