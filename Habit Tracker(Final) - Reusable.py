import json
import shutil
import os
from datetime import date
from datetime import timedelta
from dateutil import parser

# =========================== USER INPUT ==============================================================
def get_user_name():
    while True:
        name = input("Please enter your name: ")
        if not name.isalpha():
            print("Please enter only letters")
        else:
            break
    if name.lower().endswith('s'):
        name = f"{name}'"
    else:
        name = f"{name}'s"
    return name
def get_habits():
    while True:
        try:
            n = int(input("Please enter how many habits you would like to track: "))
            if n > 0:
                break
            else:
                print("Please enter a number greater than 0!")
        except ValueError:
            print("Please enter a valid number!")
    habits = []
    for i in range(n):
        while True:
            item = input(f"Please enter your #{i+1} habit: ")
            if item.strip() == "":
                print("Please enter a valid habit")
            else:
                habits.append(item)
                break
    return habits

# ====================================== HABIT OPERATIONS =============================================
def check_habits(habits):
    habit_status = {}
    for i, habit in enumerate(habits):
        while True:
            ask_user = input(f"Please confirm if you have completed habit #{i+1}:")
            if ask_user.lower() in ("yes","y"):
                habit_status[habit] = "Done"
                break
            elif ask_user.lower() in ("no","n"):
                habit_status[habit] = "Not Done"
                break
            elif ask_user.lower() in ("in progress","not yet"):
                habit_status[habit] = "In Progress"
                break
            else:
                print("Please enter a valid Yes or No response")
    symbols = {"Done": "✓", "Not Done":"✗", "In Progress":"⋯"}
    for habit, completed in habit_status.items():
        print(symbols[completed], habit)
    return habit_status

def edit_habits(results):
    print("\nCurrent habits: ")
    for habit in results:
        print(f" - {habit}")
    while True:
        old_name = input("\nPlease select which habit you would like to rename: ").strip()
        if old_name not in results:
            print(f"❌ '{old_name}' not found!")
        else:
            break
    new_name = input(f"Rename '{old_name}' to: ").strip()
    results[new_name] = results[old_name]
    del results[old_name]
    print(f"✅ Renamed '{old_name}' to '{new_name}'!")
    return results

def del_habits(results):
    print("\nCurrent habits: ")
    for habit in results:
        print(f" - {habit}")
    while True:
        old_habit = input("\nPlease select which habit you would like to delete: ").strip()
        if old_habit not in results:
            print(f"❌ '{old_habit}' not found!")
        else:
            break
    del results[old_habit]
    print(f"✅ Deleted '{old_habit}'!")
    return results

# ====================================== ANALYTICS =============================================
def show_summary(results):
    completed = 0
    for habit, status in results.items():
        if status == "Done":
            completed += 1
    total = len(results)

    if total > 0:
        percentage = (completed/total) * 100
    else:
        percentage = 0
    print(f"\n{'='*30}")
    print(f"📊 Daily summary for {date.today().strftime('%B %d, %Y')}:")
    print(f"You completed {completed} out of {total} habits")
    print(f"Completion rate: {percentage:.0f}%")
    print(f"{'='*30}")

def calculate_streak(habit_name):
    data = load_data()
    streak = 0
    current_date = date.today()

    for i in range(365):
        date_key = (current_date - timedelta(days=i)).strftime("%Y-%m-%d")

        if date_key not in data:
            break
        elif habit_name not in data[date_key]:
            break
        elif data[date_key][habit_name] != "Done":
            break
        streak += 1

    return streak

def weekly_stats():
    data = load_data()
    current_date = date.today()
    habit_counts = {}

    for i in range(7):
        date_key = (current_date - timedelta(days=i)).strftime("%Y-%m-%d")
        if date_key not in data:
            continue
        for habit, status in data[date_key].items():
            if habit not in habit_counts:
                habit_counts[habit] = 0
            if status == "Done":
                habit_counts[habit] += 1
    while True:
        if len(habit_counts) == 0:
            print("There is no saved data, please save a week's worth of data to view the leaderboard!")
            break
        else:
            leaderboard = input("Would you like to view your weekly leaderboard🏆? (Y)es or (N)o: ")
            if leaderboard.lower() in ("yes","y"):
                leaderboard_sort = sorted(habit_counts.items(), key=lambda x:x[1], reverse=True)
                for i, (habit, count) in enumerate(leaderboard_sort, 1):
                    print(f"{i}, {habit}: {count}/7 days")
                break
            elif leaderboard.lower() in ("no","n"):
                print("Ok, see ya tomorrow! 👋")
                break
            else:
                print("Please enter a valid Yes or No response!")
# ====================================== DATA MANAGEMENT =============================================
def save_habits(results):
    data = load_data()
    today = date.today().strftime("%Y-%m-%d")
    if today in data:
        while True:
            save = input("Hey, you have already saved your habits for today...saving new habits will\
                overwrite the old ones, are you sure you want to continue? Press (Y)es or (N)o")
            if save.lower() in ("yes", "y"):
                data[today] = results
                save_data(data)
                print(f"✅ Habits saved for {today}!")
                break
            elif save.lower() in ("no", "n"):
                print("Understood, ❌ Save cancelled!")
                break
            else:
                print("Please input a valid Yes or No")
    else:
        data[today] = results
        save_data(data)
        print(f"✅Habits saved for {today}!")

def load_habits():
    while True:
        date_entry = input("Please tell me which day's habits you would like to see: ").strip()
        try:
            date_ent = parser.parse(date_entry)
            date_file = date_ent.strftime("%Y-%m-%d")

            data = load_data()
            if date_file in data:
                habit_status = data[date_file]

                symbols = {"Done": "✓", "Not Done": "✗", "In Progress": "⋯"}
                print(f"\nHabits for {date_ent.strftime('%B %d, %Y')}:")
                for habit, completed in habit_status.items():
                    print(symbols[completed], habit)
                break
            else:
                print(f"No data found for {date_file}")

        except (ValueError, parser.ParserError):
            print("Sorry, I couldn't understand the date. Please try again!")
            break

def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return{}
    except json.JSONDecodeError:
        print("Uh oh, it looks like your file has crashed. Please revert back to your backup to continue your work!")
        return{}
def save_data(data):
    if os.path.exists("data.json"):
        shutil.copy("data.json", "data_backup.json")
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)


# ====================================== MAIN PROGRAM =============================================
def habit_tracker():
    username = get_user_name()
    print(f"Welcome to {username} habit tracker!")
    print("Today's date is:" ,date.today())
    habits = get_habits()
    results = check_habits(habits)
    show_summary(results)
    for habit in results:
        streak = calculate_streak(habit)
        print(f"🔥{habit} streak: {streak} days")
    weekly_stats()

    while True:
        choice = input("Please select what action you would like to take: "
                       " (S)ave"
                       " (P)revious"
                       " (E)dit"
                       " (D)elete"
                       " (Q)uit: ").strip().lower()
        if choice in ("s", "save"):
            save_habits(results)
            break
        elif choice in ("p", "previous"):
            load_habits()
            break
        elif choice in ("e", "edit"):
            results = edit_habits(results)
        elif choice in ("d", "delete"):
            results = del_habits(results)
        elif choice in ("q", "quit"):
            print("👋 Goodbye!")
            break
        else:
            print("Please select from the following given options: ")

# ====================================== RUN =============================================
habit_tracker()



