def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
    
def non_recursive(n):
    first = 0
    second = 1
    print(first, second, end=" ")
    while n > 2:
        third = first + second
        first = second
        second = third
        print(third, end=" ")
        n -= 1
    
if __name__ == "__main__":
    n = int(input("Enter number = "))
    for i in range(n):
        print(recursive_fibonacci(i), end=" ")
    print()
    non_recursive(n)
    print()