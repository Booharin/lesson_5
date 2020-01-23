from statistics import mean


def funStaff():
    with open("new_text_2.txt", "w") as my_file:
        print("Ivanov 10000\n"
              "Petrov 15000\n"
              "Lapshina 30000\n"
              "Fedorov  40000\n"
              "Ptushkin 50000\n"
              "Directorovich 100000\n"
              "Gaykina 500\n"
              "Olenev 10500\n"
              "Polykarpova 350\n"
              "Antonov 75000", file=my_file)

    line_count = 0
    with open("new_text_2.txt") as my_f:
        marginals = []
        salaries = []

        for line in my_f:
            employee_list = line.split()
            try:
                salary = int(employee_list[-1])
            except ValueError:
                print("Value error")

            if len(employee_list) > 1 and isinstance(salary, int):

                salaries.append(salary)
                if salary < 20000:
                    marginals.append(employee_list[0])

        if len(marginals) > 0:
            print("Меньше 20000 получают:\n")
            for marginal in marginals:
                print(marginal)

        if len(salaries) > 0:
            print(f"\nСредняя зарплата: {mean(salaries)}")

funStaff()