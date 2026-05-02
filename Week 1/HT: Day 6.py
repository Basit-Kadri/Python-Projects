#Today was about learning how to create files to store the habits

with open("test.txt", "w") as file:
    file.write("My first file")
    file.write("\n")
    file.write("This is line 2!")

print("File created! Check your folder for test.txt")