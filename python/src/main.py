import math


def summ(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print("Hello world")
    print(summ(3, 4))

# лабораторная работа на вычисление функций
def function(x):
    return(math.asin(x ** 2) + math.acos(x ** 3))

print("Задача 1:")
x = 0.11
while x <= 0.36:
    print(function(x))
    x += 0.05

print("Задача 2:")
x = [0.08, 0.26, 0.35, 0.41, 0.53]
for n in x:
    print(function(n))
