def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example: Generate the first 10 Fibonacci numbers
num_terms = 10
result = fibonacci(num_terms)
print(f"The first {num_terms} Fibonacci numbers are: {result}")
