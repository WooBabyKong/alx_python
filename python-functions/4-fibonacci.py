def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci_numbers = [0]
    while len(fibonacci_numbers) < n:
        if len(fibonacci_numbers) == 1:
            fibonacci_numbers.append(1)
        else:
            next_fibonacci = fibonacci_numbers[-1] + fibonacci_numbers[-2]
            fibonacci_numbers.append(next_fibonacci)

    return fibonacci_numbers

