import pandas as pd
    
def load_habits():
    return pd.read_csv("habits.csv") # Loads the habits data from the CSV file

def get_all_habits():
    df = load_habits()
    return df # Gets all habits 
    
def save_habit(name, frequency, target, category, start_date):

    df = load_habits()

    new_habit = {
        "Name": name,
        "Frequency": frequency,
        "Target": target,
        "Category": category,
        "Start Date": start_date,
        "Date": ""
    } 

    df.loc[len(df)] = new_habit

    df.to_csv("habits.csv", index=False)

    return df # Adds a new habit to the CSV file
    
        
def delete_habit(habit_name):
    df = load_habits()
    df = df[df["Name"] != habit_name]
    df.to_csv("habits.csv", index=False)
    return df # Deletes a habit from the CSV file


def complete_habit(habit_name, completion_date):

    df = load_habits()
    df["Date"] = df["Date"].astype(str)
    df.loc[df["Name"] == habit_name, "Date"] = pd.to_datetime(completion_date)
    return df # Logs the completion date for a specific habit

