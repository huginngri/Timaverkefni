with open("word.txt", "r", encoding = "utf-8") as file_1:
    a = 0
    b =""
    for words in file_1:
        words = words.strip()
        if len(words)>a:
            a = len(words)
            b = words
        b = b.replace("\n", "")
    print("Longest word is '" + b + "' of length ", a)