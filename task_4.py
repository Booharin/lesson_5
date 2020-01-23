from googletrans import Translator


def funNumbers():
    translator = Translator()
    ru_numbers = []
    with open("new_text.txt") as my_file:
        for line in my_file:
            numbers_list = line.split(" ")
            if len(numbers_list) > 0:
                try:
                    translations = translator.translate([numbers_list[0]], dest='ru')
                    for translation in translations:
                        ru_numbers.append(f"{translation.text.capitalize()} - {numbers_list[-1]}")
                except ValueError:
                    print("Value error")

        with open("new_text_ru.txt", "w") as my_file_ru:
            print("\n".join(ru_numbers), file=my_file_ru)
        my_file.close()
        my_file_ru.close()


funNumbers()
