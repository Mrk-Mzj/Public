def camel_to_snake_case(input_str: str) -> str:
    """
    Transforms a camelCase (or PascalCase) string to snake_case

    >>> camel_to_snake_case("someRandomString")
    'some_random_string'

    >>> camel_to_snake_case("SomeRandomString")
    'some_random_string'

    >>> camel_to_snake_case("someRandomStringWithNumbers123")
    'some_random_string_with_numbers_123'

    >>> camel_to_snake_case("SomeRandomStringWithNumbers123")
    'some_random_string_with_numbers_123'

    >>> camel_to_snake_case(123)
    Traceback (most recent call last):
        ...
    ValueError: Expected string as input, found <class 'int'>

    """

    import re

    # check for invalid input type
    if not isinstance(input_str, str):
        msg = f"Expected string as input, found {type(input_str)}"
        raise ValueError(msg)

    # split string to words
    words = re.findall("^[a-z]*", input_str) + re.findall("[A-Z][^A-Z]*", input_str)

    # filter out empty strings
    words = list(filter(None, words))

    return "_".join(words)


if __name__ == "__main__":
    from doctest import testmod

    # testmod()
    print(camel_to_snake_case("someRandomString"))
    print(camel_to_snake_case("SomeRandomString"))
