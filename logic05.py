def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' or 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    return a%2==0 or b%2==0
print(main(2,4))