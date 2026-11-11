# Large Integer Multiplication - Recursive Divide and Conquer
def multiply(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2
    p = 10 ** m

    a, b = divmod(x, p)
    c, d = divmod(y, p)

    return (multiply(a, c) * p * p
            + (multiply(a, d) + multiply(b, c)) * p
            + multiply(b, d))

x = int(input("First number: "))
y = int(input("Second number: "))
print("Product =", multiply(x, y))
