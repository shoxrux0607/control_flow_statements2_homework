def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    between = c
    if a<=b:
        if b<=c:
            between=b
        elif a>=c:
            between=a
    else:
        if a<=c:
            between=a
        elif b>=c:
            between=b


    return between  


print(main(2000,3100,440))