# 1. integer to float
s = 12
a = float(s)

print("a =", a)

# 2. Float to Integer Conversion

b = int(a)
print("b =", b)

# 3. String to Integer Conversion
c = "12"
d = int(c)
print("d =", d)

# 4. String to Float Conversion
e = "12.5"

f = float(e)
print("f = ", f)

# 5. Integer to String Conversion

g = 12
f = str(g)
print("g = ", g)

# 6. Float to String Conversion
h = 12.5
i = str(h)
print("i = ", i)

# 7. String Concatenation with Numbers
j = "12"
k = "12.5"
l = j + k
# print("l = ", l)

# 8. Arithmetic Operations with Different Types

m = 12
n = 12.5
o = m + n
print("o = ", o)
p = m - n
print("p = ", p)
q = m * n
print("q = ", q)
r = m / n
print("r = ", r)

# 9. User Input and Type Casting

name = input("Enter your name: ")
age = input("Enter your age: ")
print(type(age))
print(type(name))

# 10. Temperature Conversion
temp = input("Enter the temperature in Celsius: ")
temp = float(temp)

temp_in_Fahrenheit = (9 / 5) * temp + 32
print(temp_in_Fahrenheit)

# 11. List of Strings to Integers
list_of_strings = ["12", "15", 13.4, "17"]
list_of_integers = []
for item in list_of_strings:
  list_of_integers.append(int(item))

print(list_of_integers)

# 12. List of Integers to Strings
int_list = [1, 2, 3, 4, 5]
str_list = [str(num) for num in int_list]
print(str_list)

# 13.  Mixed Data Types in a List
mixed_list = [1, 2.5, "3", 4, "5.5"]
float_list = [float(item) for item in mixed_list]
print(float_list)

# 14.  Dictionary Values Type Casting
my_dict = {"a": "5", "b": 10.5, "c": "3.2"}
converted_dict = {
    k: float(v) if isinstance(v, str) else v
    for k, v in my_dict.items()
}
print(converted_dict)

# 15. Boolean to String Conversion
bool_var = True
str_var = str(bool_var)
print(str_var)

# 16. String to Boolean Conversion
str_var = "True"
bool_var = str_var.lower() == "true"
print(bool_var)

# 17. List to Tuple Conversion
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)

# 18. Tuple to List Conversion

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)

# 19. Joining Strings
word_list = ["Hello", "world", "in", "Python"]
sentence = " ".join(word_list)
print(sentence)

# 20. Splitting String to List
sentence = "This is a sample sentence"
word_list = sentence.split()
print(word_list)

# 21. Extracting Digits from String
mixed_string = "abc123def456"
digits = ''.join(char for char in mixed_string if char.isdigit())
print(digits)

# 22. Binary to Decimal Conversion
binary = "1010"
decimal = int(binary, 2)
print(decimal)

# 23. Decimal to Binary Conversion
decimal = 10

binary = bin(decimal)[2:]
print(binary)

# 24. Hexadecimal to Decimal Conversion

hexadecimal = "A5"
decimal = int(hexadecimal, 16)
print(decimal)

# 25. Decimal to Hexadecimal Conversion
decimal = 165
hexadecimal = hex(decimal)[2:]
print(hexadecimal)
