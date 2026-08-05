import pandas as pd
import requests
from openai import OpenAI
from dotenv import load_dotenv
import os

    
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
    df.loc[df["Name"] == habit_name, "Date"] = str(completion_date)
    df.to_csv("habits.csv", index=False)
    return df # Logs the completion date for a specific habit



def get_external_quote():
    url = "https://quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com/quote"

    querystring = {"token":"ipworld.info"}

    headers = {
    	"x-rapidapi-key": "afa8a1b061msh042e1c3aa2f2082p13128ejsna074f9acc1b2",
    	"x-rapidapi-host": "quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com",
    	"Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers, params=querystring)    


def get_ai_quote(prompt):
    
    load_dotenv('1.env')
    openai_api_key = os.getenv('OPENAI_API_KEY')

    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openai_api_key
    )

    completion = client.chat.completions.create(
        model="cohere/north-mini-code:free",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a friendly and funny assistant. Give motivational"
                    " ideas and encouraging words in Bahrani Arabic"
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response




