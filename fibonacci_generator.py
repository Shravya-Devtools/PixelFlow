def generate_fibonacci(n):
    """Generate a list of the first n Fibonacci numbers."""
    if n <= 0:
        return []

    sequence = [0, 1]
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence[:n]

# Example usage
if __name__ == "__main__":
    count = 10
    fib_sequence = generate_fibonacci(count)
    print(f"First {count} Fibonacci numbers: {fib_sequence}")
