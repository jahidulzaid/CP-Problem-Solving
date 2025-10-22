def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        word = input()
        total = 0
        for c in word:
            if c.islower():
                total += ord(c) - ord('a') + 1
            elif c.isupper():
                total += ord(c) - ord('A') + 27
        if is_prime(total):
            print("It is a prime word.")
        else:
            print("It is not a prime word.")
    except EOFError:
        break
