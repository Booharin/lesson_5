import json
from statistics import mean


def my_func(el_1, el_2):
    return el_1 - el_2


def createDict():
    with open("new_text.txt") as my_file:
        data_dict = {}
        incomes = []

        for line in my_file:
            line_list = line.split()
            numbers = []

            for some_string in line_list:
                number_from_string = ''.join(filter(str.isdigit, some_string))
                if len(number_from_string) > 0:
                    numbers.append(int(number_from_string))

            if len(numbers) > 1:
                income = numbers[-2] - numbers[-1]
                data_dict[line_list[0]] = income
                if income > 0:
                    print(income)
                    incomes.append(income)

        data_dict["average_profit"] = mean(incomes)

        with open("dict.json", "w") as j:
            json.dump(data_dict, j)

        json_str = json.dumps(data_dict)
        print(json_str)


createDict()