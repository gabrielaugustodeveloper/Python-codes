def is_prime(num):
    # Prime numbers must be greater than 1
    if num <= 1:
        return False

    # Loop from 2 up to the square root of the number
    # If any number divides num evenly, it is not prime
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    # If no divisors were found, the number is prime
    return True
