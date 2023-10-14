def is_polish_national_id(input_int: int) -> bool:
    """
    Verification of the correctness of the PESEL number.
    www-gov-pl.translate.goog/web/gov/czym-jest-numer-pesel?_x_tr_sl=auto&_x_tr_tl=en


    >>> is_polish_national_id(02070803628)
    True

    >>> is_polish_national_id(-99012212349)
    False

    >>> is_polish_national_id(990122123499999)
    False

    >>> is_polish_national_id("abc!@#")
    Traceback (most recent call last):
        ...
    ValueError: Expected int as input, found <class 'str'>
    """

    # check for invalid input type
    if not isinstance(input_int, int):
        msg = f"Expected int as input, found {type(input_int)}"
        raise ValueError(msg)

    # check number range (00010100000-99923199999)
    if input_int < 10100000 or input_int > 99923199999:
        return False

    # check month corectness (01-12), (21-32), (41-52), (61-72), (81-92)
    # check day corectness (01-31)

    # check the checksum
    multipliers = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    sum = 0

    digits_to_check = str(input_int)[:-1]  # cut off the checksum

    for index, digit in enumerate(digits_to_check):
        # Multiply corresponding digits and multipiers
        # With a double-digit result, add only the last digit
        sum += (int(digit) * multipliers[index]) % 10

    checksum = 10 - sum % 10

    if checksum != input_int % 10:
        return False

    return True


if __name__ == "__main__":
    from doctest import testmod

    testmod()
