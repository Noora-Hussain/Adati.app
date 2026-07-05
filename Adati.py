import pandas as pd

def load_habits():
    return pd.read_csv("habits.csv")

def add_habit(name, freq, target, category, date):
    df = load_habits()
    new_habit = pd.DataFrame({"Name": [name], "Frequency": [freq], "Target": [target], "Category": [category], "Start Date": [date]})
    df = pd.concat([df, new_habit], ignore_index=True)
    df.to_csv("habits.csv", index=False)

def get_all_habits():
    df = load_habits()
    return list(df["Name"].unique())

def log_completion(habit_name, date):
    df_logs = pd.read_csv("habits.csv")
    new_log = pd.DataFrame({"Name": [habit_name], "Date": [str(date)]})
    df_logs = pd.concat([df_logs, new_log], ignore_index=True)
    df_logs.to_csv("habits.csv", index=False)
    return f"Completion for '{habit_name}' logged successfully!"