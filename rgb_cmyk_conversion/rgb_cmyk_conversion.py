def rgb_to_cmyk(r, g, b: int) -> tuple[int, int, int]:
    """
    RGB to CMYK conversion.

    >>> rgb_to_cmyk(255, 200, "a")
    Traceback (most recent call last):
        ...
    ValueError: Expected int as input, found (<class 'int'>, <class 'int'>, <class 'str'>)

    >>> rgb_to_cmyk(255, 255, 999)
    Traceback (most recent call last):
        ...
    ValueError: Expected int of the range 0..255
    """

    if type(r) != int or type(g) != int or type(b) != int:
        raise ValueError(f"Expected int as input, found {type(r), type(g), type(b)}")

    if not 0 < r < 256 or not 0 < g < 256 or not 0 < b < 256:
        raise ValueError("Expected int of the range 0..255")
    return r, g, b


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    # print(rgb_to_cmyk(255, 200, "a"))
