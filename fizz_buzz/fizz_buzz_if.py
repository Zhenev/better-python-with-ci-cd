import sys


def return_fizz_buzz(num: int) -> str | int:
    """This is aa simple solution to solve the famous Fizz Buzz problem.

    :param num: the number to check
    :return: `fizz`, `buzz`, `fizzbuzz` or the number itself
    """

    if num % 15 == 0:
        return "fizzbuzz"
    if num % 5 == 0:
        return "buzz"
    if num % 3 == 0:
        return "fizz"
    return num


def fetch_integer(num_str: str) -> int:
    try:
        num = int(num_str)
        print(f'{str(num_str)} as an int is {num}.')
        return num
    except ValueError as ex:
        sys.exit(f'"{num_str}" cannot be converted to an int: {ex}.')


if __name__ == "__main__":
    number = fetch_integer(sys.argv[1])
    output = return_fizz_buzz(number)
    if type(output) == str:
        print(f'{str(number)} is a "{output}" number.')
    else:
        print(f'{str(number)} is not a fizz/buzz number.')
