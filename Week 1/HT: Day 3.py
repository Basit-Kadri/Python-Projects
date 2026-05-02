#This code asks how many habits you want to track and then asks you whether you completed
#each habit and stores/displays the results

#Day 3:
def run_day3():
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
