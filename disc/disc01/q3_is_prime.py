def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False 
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True 

# one sentence: divide n by the numbers iterating from 2 to n-1, and if any remainders is equal to 0, n is not prime.