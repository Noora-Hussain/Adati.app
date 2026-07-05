import pandas as pd

def load_habits():
    return pd.read_csv("habits.csv")


def add_habit(name, freq, target, category, date):
    df = load_habits()

    new_habit = pd.DataFrame({
        "Name": [name],
        "Frequency": [freq],
        "Target": [target],
        "Category": [category],
        "Start Date": [date],
        
    })

    df = pd.concat([df, new_habit], ignore_index=True)
    df.to_csv("habits.csv", index=False)    

def get_all_habits():
    df = load_habits()

    if df.empty:
        return []

    return list(df["Name"])


def log_completion(habit_name):
    df = load_habits()
    df.loc[df['Name'] == habit_name, 'Completions'] += 1
    df.to_csv('habits.csv', index=False)
    return f"Completion for '{habit_name}' logged successfully!"

    