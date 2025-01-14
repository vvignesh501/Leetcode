from functools import lru_cache


@lru_cache(maxsize=1000)
def factorial(input_value):
    if input_value < 2:
        return 1
    elif input_value >= 2:
        return input_value * factorial(input_value - 1)


for i in range(1, 5):
    print(f"{i}! = ", factorial(i))
