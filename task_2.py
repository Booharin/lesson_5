def fileFun():
    with open("new_text_2.txt", "w") as my_file:
        print("Python\nthe best\nlanguage\n! ! !", file=my_file)

    line_count = 0
    with open("new_text_2.txt") as my_f:
        for index, line in enumerate(my_f):
            print(f"В {index + 1} строке {len(line.split())} слов")
            line_count += 1
    print("\nКоличество строк: ", line_count)


fileFun()
