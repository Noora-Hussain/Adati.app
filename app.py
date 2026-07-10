import streamlit as st
import pandas as pd
import datetime
import logic as Aa


st.title("Adati🎯") # Set the main title of the app
st.title("Adati Habit Tracker") 

st.image("Aadit.jpg") # add image 

option = st.selectbox("HabitFlow",("Add Habit➕", "View Habits📋", "Log Completion ✅", "View Stats📊", " Edit/Remove Habits⚙️"))
# Let the user choose an option

st.write("You selected:", option)



if option == "Add Habit➕": 
    st.header("Add a New Habit") 
    Name_Habit = st.text_input("What is the habit?")
    selection = st.selectbox("Frequency", ["Daily", "Weekly", "Monthly"])
    Target = st.number_input("How many times do you want to perform this habit?")
    Category = st.selectbox("Enter the habit category?", ("Health", "Study", "Personal Development", "Finance", "Other"))
    start_date = st.date_input("When do you want to start this habit?",datetime.date.today())
    # Show the form to add a new habit
    if Category == "Other":
        cat = st.text_input("Please specify the category:")
    else:
        cat = Category   # Let user type a category if they select "Other"
        if st.button("Add Habit ➕", type="primary"):
            if Name_Habit:
                Aa.save_habit(Name_Habit, selection,Target,cat, start_date)
                st.success(f"{Name_Habit} added successfully! 🎯")
            else:
                st.warning("Please enter a habit name") 


                
elif option == "View Habits📋":
    st.header("Edit Habit Categories") 
    df = Aa.get_all_habits() 
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
    if not edited_df.empty and 'Target' in edited_df.columns:
        top_habit_index = edited_df['Target'].idxmax()
        top_habit_name = edited_df.loc[top_habit_index, 'Name'] # Finds the row with the biggest target value and gets its habit name.
    
        st.markdown(f"### 🏆 Your most challenging habit is: **{top_habit_name}** 🎈")
        st.balloons()

elif option == "Log Completion ✅":
    st.header("Log Habit Completion")
    habits = Aa.get_all_habits()
    selected_habit = st.selectbox("Select a habit", habits["Name"]) # Select habit name
    completion_date = st.date_input("Completion Date", datetime.date.today()) # Select completion date
    if st.button("Log Completion ✅", type="primary"):
          Aa.complete_habit(selected_habit,completion_date )
          st.success(f"{selected_habit} completed 🎉")
# Add completion button


elif option == "View Stats📊":
    st.header("View Stats 📊")
    habits = Aa.get_all_habits()
    total_habits = len(habits)
    completed = 0
    for date in habits["Date"]:
        if pd.notna(date) and date != "":
            completed += 1 # Just counting the completed habits by checking if a date is entered.
    remaining = total_habits - completed

    col1, col2, col3 = st.columns(3)  # Create 3 columns to display statistics
    col1.metric("Total Habits 🎯", total_habits) # total habits
    col2.metric("Completed ✅", completed) # completed habits
    col3.metric("Remaining ⏳" , remaining) # remaining habits

    

elif option == " Edit/Remove Habits⚙️":
    st.header("Edit or Remove Habits ⚙️")
    habits = Aa.get_all_habits()
    habits = habits.dropna(subset=["Name"])# Remove empty names
    selected_habit = st.selectbox("Select a habit",habits["Name"])
    if st.button("Remove Habit 🗑️"):

        Aa.delete_habit(selected_habit)
        st.success(f"{selected_habit} removed")
        st.rerun()   # Refresh the app after deleting
    st.dataframe(Aa.get_all_habits())



# All of the code above was created using the Streamlit library
