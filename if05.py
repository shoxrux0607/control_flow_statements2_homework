def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1 = n % 10
    n = n//10

    x2 = n % 10
    n = n//10

    x3 = n % 10
    n = n//10

    x4 = n % 10
    n = n//10

    x5 = n % 10
    n = n//10

    if x1 >= x2 and x1 >= x3 and x1 >= x4 and x1 >= x5:
        return x1
    elif x2 >= x1 and x2 >= x3 and x2 >= x4 and x2 >= x5:
        return x2
    elif x3 >= x1 and x3 >= x2 and x3 >= x4 and x3 >= x5:
        return x3
    elif x4 >= x1 and x4 >= x2 and x4 >= x3 and x4 >= x5:
        return x4
    else:
        return x5


print(main(50395))
