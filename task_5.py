from functools import reduce


def my_func(el_1, el_2):
    return el_1 * el_2


def numbersSum():
    with open("new_text.txt", "w") as my_file:
        print("1 2 3 4 5 6", file=my_file)

    with open("new_text.txt") as my_f:
        content = my_f.read().split()
        try:
            my_numbers_sum = list(map(int, content))
        except ValueError:
            print("Value error")

    print(reduce(my_func, my_numbers_sum))


numbersSum()
