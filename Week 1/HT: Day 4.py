#Today's exercise is all about creating dictionaries and storing data within those dictionaries,
#Basically helping users' store the status of their habits
# Day 4:
def run_day4():
    n = int(input("Please enter how many habits you would like to track: "))
    habits = []
    for i in range(n):
        item = input(f"Please enter your #{i+1} habit: ")
        habits.append(item)

    habit_status = {}
    for i, habit in enumerate(habits):
        ask_user = input(f"Please confirm if you have completed habit #{i+1}:")
        if ask_user.lower() in ("yes","y","YES"):
            habit_status[habit] = True
        else:
            habit_status[habit] = False
    for habit, completed in habit_status.items():
        if completed:
            print("✓", habit)
        else:
            print("✗", habit)

























