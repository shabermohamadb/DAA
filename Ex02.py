# Karatsuba Algorithm - Large Integer Multiplication
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2
    p = 10 ** m

    a, b = divmod(x, p)
    c, d = divmod(y, p)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    return ac * p * p + ad_bc * p + bd

x = int(input("First number: "))
y = int(input("Second number: "))
print("Product =", karatsuba(x, y))
