def fizz_buzz_checker(number: int) -> str:
    """
    Checks if given number should be replaced
    with fizz, buzz, fizzbuzz or left unchanged

    >>> fizz_buzz_checker("abc")
    Traceback (most recent call last):
    ...
    ValueError: Expected str as input, found <class 'str'>

    >>> fizz_buzz_checker(-5)
    Traceback (most recent call last):
    ...
    ValueError: input must be positive

    >>> fizz_buzz_checker(0)
    Traceback (most recent call last):
    ...
    ValueError: input must be positive

    >>> fizz_buzz_checker(3)
    'fizz'

    >>> fizz_buzz_checker(5)
    'buzz'

    >>> fizz_buzz_checker(15)
    'fizzbuzz'

    """

    if not isinstance(number, int):
        msg = f"Expected str as input, found {type(number)}"
        raise ValueError(msg)

    if number <= 0:
        raise ValueError("input must be positive")

    if number % 15 == 0:
        return "fizzbuzz"

    elif number % 3 == 0:
        return "fizz"

    elif number % 5 == 0:
        return "buzz"

    else:
        return str(number)


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    end_ranage = 15
    for i in range(end_ranage):
        print(fizz_buzz_checker(i + 1))
