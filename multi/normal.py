def foo(x):
    """
    Simple function to return the factorial of an integer
    """
    if x == 0:
        return 1
    else:
        return x * x

if __name__ == "__main__":
    test = [x for x in range(1000)]
    for i in test:
        foo(i)
