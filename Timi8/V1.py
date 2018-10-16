with open("test.txt") as file_1:
    text = ""
    for linestr in file_1:
        linestr = linestr.strip()
        text += linestr.replace(" ", "")
    print(text)