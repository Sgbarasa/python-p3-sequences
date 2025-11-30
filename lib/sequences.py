def print_fibonacci(length):
    if length == 0:
        print([])
        return

    if length == 1:
        print([0])
        return

    # Start the sequence with the first two Fibonacci numbers
    seq = [0, 1]

    # Build the rest if needed
    while len(seq) < length:
        seq.append(seq[-1] + seq[-2])

    print(seq)
