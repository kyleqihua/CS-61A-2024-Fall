def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes

# why (5, 7) and (2, 4) perfectly match? 5*7 == 7*5, 2*10 == 4*5 
# if (5, 8), return 8. that's wrong, because they already met at 7th minute.
"""
The race function below sometimes returns the wrong value and sometimes runs forever.
Find positive integers x and y (with y larger than x but not larger than 2 * x) for which either:
race(x, y) returns the wrong value or
race(x, y) runs forever
"""