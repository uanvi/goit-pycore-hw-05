def caching_fibonacci():
    """Generate Fibonacci numbers using caching.
    Returns:
        Function: A function that calculates Fibonacci numbers.
    """

    #empty dictionary for caching numbers
    cache = {}

    # function to calculate fibonachi nu,ber
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache: # return number from cache if exist
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Examples
fib = caching_fibonacci()
print(fib(5))  # Calculation for 5
print(fib(10)) # Calculation for 55
