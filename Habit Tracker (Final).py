from datetime import date

def get_user_name():
    name = input("Please enter your name: ")

    if name.lower().endswith('s'):
        name = f"{name}'"
    else:
        name = f"{name}'s"
    return name
#Day 1
def run_tracker():
    print(f"Welcome to {get_user_name()} habit tracker")
    print("Today's date is:", date.today())
    #Day 1

    #Day 2
    n = int(input("Please enter how many habits you would like to track: "))
    habits = []
    for i in range(n):
        item = input(f"Please enter your #{i+1} habit: ")
        habits.append(item)
        print(habits)
    #Day 2

    #Day 3
    n = int(input("Please enter how many habits you would like to track: "))
    habits = []
    for i in range(n):
        item = input(f"Please enter your #{i+1} habit: ")
        habits.append(item)
        print(habits)

    status = []
    for i, habit in enumerate(habits):
        while True:
            done = input(f"Please confirm if you have completed your #{i+1} habit: ")
            if done.lower() in ("yes","y"):
                status.append("✔")
                break
            elif done.lower() in ("no","n"):
                status.append("X")
                break
            else:
                print("Please enter a valid yes or no")

    for i in range(len(habits)):
        print(f"{habits[i]} - {status[i]}")
    #Day 3

    #Day 4
    habit_status = {}
    for i, habit in enumerate(habits):
        ask_user = input(f"Please confirm if you have completed habit #{i+1}:")
        if ask_user.lower() in ("yes","y"):
            habit_status[habit] = True
        else:
            habit_status[habit] = False
    for habit, completed in habit_status.items():
        if completed:
            print("✓", habit)
        else:
            print("✗", habit)
    #Day 4

run_tracker()