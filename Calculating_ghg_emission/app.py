# This script calculates GHG emissions in an event
# Task 1: Import required data make a summary dataframe
# Task 2: Calculate GHG emissions
# Task 3: Sum up GHG emissions in total and per scope
# Task 4: Visualise the result

# Task 1: Import necessary libraries
# core package
import streamlit as st
import pandas as pd


# DB fanctions packages
from db_fxns import *



# if there are no tables, this code makes the database automatically
create_event_table()
create_food_table()
create_beverage_table()
    


# get information
df_event = view_event()
df_food = view_food()
df_beverage = view_beverage()


# provide the information
st.write(df_food)

