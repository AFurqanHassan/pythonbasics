# 1. Hello, World!
print("Hello, World!")

# 2. Variable Assignment
name = "Ahmad Furqan Hassan"
age = 24
country = "PAKISTAN"
print(name)
print(age)
print(country)

# 3. Basic Math Operations
print(15 + 3)
print(15 - 3)
print(15 * 3)
print(15 / 3)

# 4. Type Conversion
num_str = "6969"
num_int = int(num_str)
print(num_int)

float_num = 12.345
int_num = int(float_num)
print(int_num)

# 5. User Input
name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))
print("Hello, {}! In 5 years, you will be {} years old.".format(name, age + 5))

# 6. Simple Interest Calculator
principal = 1000
rate = 0.03
time = 5
simple_interest = principal * rate * time
print("Simple Interest: {}".format(simple_interest))

# 7. Area of a Circle
import math

radius = 5
area = math.pi * radius ** 2
print("Area of the circle: {}".format(area))

# 8. Swapping Variables
a = 5
b = 10
print("Before swapping: a = {}, b = {}".format(a, b))
a, b = b, a
print("After swapping: a = {}, b = {}".format(a, b))

# 9. String Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

# 10. Checking Data Types
var_str = "Python"
var_int = 42
var_float = 3.14
print(type(var_str))
print(type(var_int))
print(type(var_float))

# 11. List Creation
fruits = ["apple", "banana", "orange", "grape", "mango"]
print(fruits)

# 12. Indexing in Strings
word = "Python"
print("First character: {}".format(word[0]))
print("Last character: {}".format(word[-1]))

# 13. Multiplication Table
for i in range(1, 11):
    print("7 x {} = {}".format(i, 7 * i))

# 14. Comparing Numbers
num1 = float(raw_input("Enter the first number: "))
num2 = float(raw_input("Enter the second number: "))
if num1 > num2:
    print("{} is larger".format(num1))
elif num2 > num1:
    print("{} is larger".format(num2))
else:
    print("The numbers are equal")

# 15. Even or Odd
num = 23
if num % 2 == 0:
    print("{} is even".format(num))
else:
    print("{} is odd".format(num))

# 16. String Length
text = "Data Science"
print("Length of '{}': {}".format(text, len(text)))

# 17. Count Vowels
word = "Programming"
vowels = "aeiouAEIOU"
count = sum(1 for char in word if char in vowels)
print("Number of vowels in '{}': {}".format(word, count))

# 18. Reverse a String
word = "Python"
reversed_word = word[::-1]
print("Reversed '{}': {}".format(word, reversed_word))

# 19. List Slicing
numbers = [1, 2, 3, 4, 5, 6]
sublist = numbers[1:4]
print(sublist)

# 20. Sum of a List
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print("Sum of the list: {}".format(total))

# 21. Minimum and Maximum
numbers = [1, 2, 3, 4, 5]
print("Minimum: {}".format(min(numbers)))
print("Maximum: {}".format(max(numbers)))

# 22. Removing Elements
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)

# 23. Dictionary Basics
person = {"name": "Jawad Zahid", "age": 25}
print(person)

# 24. Accessing Dictionary Elements
person = {"name": "Haroon", "age": 25}
print("Age: {}".format(person['age']))

# 25. Updating Dictionary
person = {"name": "Abu Bakar", "age": 25}
person["country"] = "Pakistan"
print(person)
