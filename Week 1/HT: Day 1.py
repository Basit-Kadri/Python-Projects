#Today was all about importing the datetime function and creating the front display
# of the app, with the name and the date

def run_day1():
    from datetime import date
    name = input("Please enter your name: ")

    if name.endswith('s') or name.endswith('S'):
        name = f"{name}'"
    else:
        name = f"{name}'s"

    print(f"Welcome to {name} habit tracker")
    print("Today's date is:", date.today())

