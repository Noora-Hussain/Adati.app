import streamlit as st
import pandas as pd
import datetime
import Adati as Aa

st.set_page_config(page_title="Adati Habit Tracker", layout="centered")
st.image("Aadit.jpg", width=500)
st.title("Adati🎯") 

COLUMNS = ['Name', 'Frequency', 'Target', 'Category', 'Start Date']

add_selectbox = st.sidebar.selectbox(
    "HabitFlow Menu",
    ["➕ Add Habit", "📋 View Habits", "✅ Log Completion", "📊 View Stats", "⚙️ Edit/Remove Habits"]
)

if add_selectbox == "➕ Add Habit":
    st.header("Add a New Habit")
    Name_Habit = st.text_input("What is the habit?")
    selection = st.selectbox("Frequency", ["Daily", "Weekly", "Monthly"])
    Target = st.number_input("How many times do you want to perform this habit?", min_value=1, step=1, format='%d')
    Category = st.selectbox("Enter the habit category?", ("Health", "Study", "Personal Development", "Finance", "Other"))
    
    if Category == "Other":
        cat = st.text_input("Please specify the category:")
    else:
        cat = Category
        
    Date = st.date_input("Start Date")

    if st.button("Save Habit"):
        if Name_Habit.strip() == "":
            st.error("Please fill in all required fields.")
        else:
            # هنا نفترض أن دالة Aa.add_habit تحفظ الأعمدة بنفس الترتيب
            Aa.add_habit(Name_Habit, selection, Target, cat, str(Date))
            st.success("Habit added successfully 🎉")
            st.balloons()

elif add_selectbox == "📋 View Habits":
    st.header("Edit Habit Categories")
    df = Aa.load_habits()
    
    df = df[[col for col in COLUMNS if col in df.columns]]
    
    if 'Start Date' in df.columns:
        df['Start Date'] = pd.to_datetime(df['Start Date']).dt.date
        
    edited_df = st.data_editor(df, use_container_width=True)
    
    if st.button("Save Changes"):
        edited_df.to_csv('habits.csv', index=False)
        st.success("Changes saved!")

elif add_selectbox == "✅ Log Completion":
    st.header("Log Habit Completion")
    habits = Aa.get_all_habits()

    if len(habits) == 0:
        st.warning("No habits found.")
    else:
        selected_habit = st.selectbox("Select a habit", habits)
        completion_date = st.date_input("Completion Date", datetime.date.today())

        if st.button("Log Completion"):
            message = Aa.log_completion(selected_habit, completion_date)
            st.success(message)
            st.balloons()

elif add_selectbox == "📊 View Stats":
    st.header("Habit Statistics")
    try:
        df = pd.read_csv('habits.csv')
        if 'Name' in df.columns:
            completion_data = df.dropna(subset=['Name']) 
            st.metric("Total Records", len(completion_data))
            habit_counts = completion_data["Name"].value_counts()
            st.bar_chart(habit_counts)
        else:
            st.warning("Data structure error.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

elif add_selectbox == "⚙️ Edit/Remove Habits":
    st.header("Manage Your Habits")
    try:
        df = pd.read_csv('habits.csv')
        
        df = df[[col for col in COLUMNS if col in df.columns]]
        
        if 'Start Date' in df.columns:
            df['Start Date'] = pd.to_datetime(df['Start Date']).dt.date
            
        edited_df = st.data_editor(
            df, 
            num_rows="dynamic", 
            use_container_width=True
        )
        
        if st.button("Save Changes"):
            edited_df.to_csv('habits.csv', index=False)
            st.success("Changes saved successfully!")
            st.rerun() 
    except Exception as e:
        st.error(f"Error: {e}")
        