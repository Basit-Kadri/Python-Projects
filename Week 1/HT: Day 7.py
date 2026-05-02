#Today is about learning how to read files that store the habits

#Day 7

with open("test.txt", "r") as file:
    content = file.read()
    print("File Contents: ", content)