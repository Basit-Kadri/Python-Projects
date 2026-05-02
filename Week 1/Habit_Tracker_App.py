import streamlit as st
import json
import shutil
import os
import pandas as pd
from datetime import date
from datetime import timedelta
# =========================== USER INPUT ==============================================================
def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return{}
    except json.JSONDecodeError:
        st.warning("Uh oh, it looks like your file has crashed. Please revert back to your backup to continue your work!")
        return{}
def save_data(data):
    if os.path.exists("data.json"):
        shutil.copy("data.json", "data_backup.json")
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)
def save_habits(results):
    data = load_data()
    today = date.today().strftime("%Y-%m-%d")
    data[today] = results
    save_data(data)
    st.success(f"✅Habits saved for {today}!")

def show_charts():
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
    if len(habit_counts) == 0:
        st.write("There is no saved data, please save a week's worth of data to view the leaderboard!")
    else:
        df = pd.DataFrame.from_dict(habit_counts, orient="index", columns=["Days Completed"])
        st.bar_chart(df)

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
    st.divider()
    st.write(f"📊 Daily summary for {date.today().strftime('%B %d, %Y')}:")
    st.write(f"You completed {completed} out of {total} habits")
    st.write(f"Completion rate: {percentage:.0f}%")
    st.divider()

st.title("🏆 Welcome to your Habit Tracker!")

name = st.text_input("Enter your name: ")

if name:
    st.write(f"Welcome, {name}!")

n = st.number_input("Please enter how many habits you would like to track: ", min_value=1, max_value=10, step=1)

habitz = []
for i in range(n):
    item = st.text_input(f"Please enter habit #{i+1}: ", key=f"habit_{i}")
    habitz.append(item)

results = {}
if all(habitz):
    for habit in habitz:
        checked = st.checkbox(habit)
        if checked:
            results[habit] = "Done"
        else:
            results[habit] = "Not Done"

if st.button("Save"):
    save_habits(results)
    show_summary(results)
    for habit in results:
        streak = calculate_streak(habit)
        st.write(f"🔥 {habit}: {streak} day streak!")



selected_date = st.date_input("Would you like to view a previous date?")
data = load_data()
date_file = selected_date.strftime("%Y-%m-%d")
if date_file in data:
    habit = selected_date
    st.write(f"Here are your habits for {selected_date}: ")
    symbols = {"Done": "✓", "Not Done": "✗", "In Progress": "⋯"}
    for habit, status in data[date_file].items():
        st.write(f"{symbols[status]} {habit}: {status}")
else:
    st.write(f"No data found for {selected_date}")

if st.button("📊View Weekly Chart"):
    st.subheader("📊Weekly Habit Chart")
    show_charts()


