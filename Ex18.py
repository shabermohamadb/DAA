# Recursive Divide and Conquer Multiplication
def multiply(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y))) // 2
    p = 10 ** n
    a, b = divmod(x, p)
    c, d = divmod(y, p)

    return (multiply(a, c) * p * p
            + (multiply(a, d) + multiply(b, c)) * p
            + multiply(b, d))

x = int(input("First: "))
y = int(input("Second: "))
print("Product =", multiply(x, y))
