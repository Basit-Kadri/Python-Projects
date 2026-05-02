#Today was all about creating user input lists and storing them for the tracker

#Day 2:
def run_day2():
    n = int(input("Please enter how many habits you would like to track: "))
    habits = []
    for i in range(n):
        item = input(f"Please enter your #{i+1} habit: ")
        habits.append(item)
        print(habits)