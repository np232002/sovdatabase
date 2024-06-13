## get the urlparameter cin/ load that row from the dataframe and write out the information for that row

import streamlit as st
import pandas as pd

# Define your functions


def changeleadcolumn(cin_number, result, df):
    df.loc[df["CIN"] == cin_number, "Lead"] = result

def savedf(df):
    df.to_csv("/Users/neelpalle/Desktop/dbproject/final.xlsx", index=False)

# Load the DataFrame (replace with your file path)
def load_data():
    return pd.read_csv('/Users/neelpalle/Desktop/dbproject/final.xlsx')


# Step 1: Input CIN Number page

cin = st.session_state["cin"]

# Once the user puts in the number & clicks enter it should open up the table of 10 random options for the CIN number industry code



statedata = pd.read_excel("/Users/neelpalle/Desktop/dbproject/test1.xlsx")


foundcin = statedata[statedata["CIN"] == cin]

st.write(foundcin)

