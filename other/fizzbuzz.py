def fizz_buzz_checker(number: int) -> str:
    # checks if given number should be replaced
    # with fizz, buzz, fizzbuzz or left unchanged

    if number % 15 == 0:
        return "fizzbuzz"

    elif number % 3 == 0:
        return "fizz"

    elif number % 5 == 0:
        return "buzz"

    else:
        return str(number)


if __name__ == "__main__":
    end_ranage = 15

    for i in range(end_ranage):
        print(fizz_buzz_checker(i + 1))
