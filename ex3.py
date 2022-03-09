def my_func(a, b, c):
    if (a > b and b > c) or (b > a and a > c):
        sum = a + b
    elif (a > c and c > b) or (c > a and a > c):
        sum = a + c
    elif (c > b and b > a) or (b > c and c > a):
        sum = c + b
    return sum

print(my_func(4, 6, 5))