def box(name):
    print(f"Hello {name}")
name = input("What's your name? ")
# box("Daniel")

box(name)

def cal(a, b):
    print(a + b)

a = int(input("What's your a? "))
b = int(input("What's your b? "))

cal(a, b)

def area(r):
    pi = 3.142
    print("Area is", pi * r * r)

# r = int(input("What's your radius? "))

# area(r)

k = int(input("What's your radius? "))

area(k)