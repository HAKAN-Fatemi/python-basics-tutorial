# # Python 01
# Data types, print, Mathematics
# HAKAN Fatemi (09220630140)

# Assigning a number to a variable
number = 10
k, l, m = "Amir", "Hosein", "Mohammad"

print(k)
print(l)
print(m)

n = o = p = "Apple"
print(n)
print(o)
print(p)

# همچین اسم هایی ممکن نیست
# 2myvar = "Amir"
# my-var = "Amir"
# my var = "Amir"
#### Data type & print #####

a = "Hello World"

print(a)
print(type(a))
b = 20
print(b) # display b and type of b
print(type(b)) 
c = 20.5


# This is a comment
# written in more than just one line
# about display c and type of c
print(c)
print(type(c)) 
d = 1j
print(d)
print(type(d)) 
e = ["apple", 10, 5.5, "shiva", "apple"]


# display e and type of e
print(e)
print(type(e)) 
f = ("apple", "banana", "cherry")


# display f and type of f
print(f)
print(type(f))
g = {"name" : "John", "age" : 36}


# display g and type of g
print(g)
print(type(g))
g = {"name" : ["apple", 10, "cherry"], "age" : [36, 20, "l"]}


# display g and type of g
print(g)
print(type(g))
h = {"apple", "banana", "cherry"}


# display h and type of h
print(h)
print(type(h))
i = True


# display i and type of i
print(i)
print(type(i))
print(10 == 10)
print(i != False)
j = None

# display j and type of j
print(j)
print(type(j))


# Display a number
number = 42
print("The number is:", number)


# Display a word
word = "Hello"
print("The word is:", word)


# Get a number from the user
number = float(input("Enter a number: "))
print("You entered:", number)


# Get a word from the user
word = input("Enter a word: ")
print("You entered:", word)


# Integer example
age = 25
print("Age:", age)


# Float example
temperature = 23.5
print("Temperature:", temperature)


# Check data type
x = 42
y = 3.14
z = "Hello"
print("Type of x:", type(x))  # int
print("Type of y:", type(y))  # float
print("Type of z:", type(z))  # str


# Case sensitivity
name = "Python"
print("Is 'Python' equal to 'python'?", name == "python")  # False


# Get user's name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))


# Display a welcome message
print(f"Hello {name}! You are {age} years old.")


### Application in loops ###
# r = r + 3 -> r += 3
# s = s - 3 -> s -= 3

# t = t * 3 -> t *= 3
# u = u / 3 -> u /= 3

# v = v % 3 -> v %= 3

# w = w // 3 -> w //= 3
# y = y ** 3 -> y **= 3


i= 10
i %= 3
print(i)
i= 10
i //= 3
print(i)


### Math operations ###
a = 10
b = 3


print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Exponentiation:", a ** b)
print("Remainder:", a % b)


# Get length and width from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))


# Calculate the area
area = length * width


# Display the result
print(area)


### Application in conditions ###
x= 10
y= 20

x == y	
x != y	
x > y	
x < y	
x >= y	
x <= y	


### Comparison operators
a = 10
b = 20
print("a == b:", a == b)  # Equal
print("a != b:", a != b)  # Not equal
print("a > b:", a > b)    # Greater than
print("a < b:", a < b)    # Less than
print("a >= b:", a >= b)  # Greater than or equal
print("a <= b:", a <= b)  # Less than or equal


# Mahdi Fatemi (HAKAN)
# 09220630140
# www.hooko.ir
