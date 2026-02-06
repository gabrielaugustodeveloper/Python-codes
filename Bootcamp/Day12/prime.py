def is_prime(num):
    # Numbers smaller than or equal to 1 are not prime
    if num <= 1:
        return False

    # Try dividing the number by every integer from 2 up to num - 1
    for i in range(2, num):
        # If num can be divided evenly by i, it's not prime
        if num % i == 0:
            return False

    # If no number divides num, then it's prime
    return True

print(is_prime(1))
print(is_prime(7))