def createEndEditTextFile():
    inputText = None

    while True:
        inputText = input("Введите строку, для выхода введите пустую строку ' ': ")
        if inputText == " ":
            my_file.close()
            break
        with open("new_text.txt", "w") as my_file:
            print(inputText, file=my_file)


createEndEditTextFile()