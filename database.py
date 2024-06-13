import streamlit as st
import pandas as pd

# Define your functions
def similarsearch(cin_number, df):
    industry_code = cin_number[1:6]
    sub_df = df[(df["CIN"].str.slice(1, 6) == industry_code) & (df["Lead"].isna())]
    random_rows = sub_df.sample(n=1, random_state=1)
    return random_rows

def changeleadcolumn(cin_number, result, df):
    df.loc[df["CIN"] == cin_number, "Lead"] = result

def savedf(df):
    df.to_csv("/Users/neelpalle/Desktop/dbproject/test1.xlsx", index=False)

# Load the DataFrame (replace with your file path)
def load_data():
    return pd.read_csv('/Users/neelpalle/Desktop/dbproject/test1.xlsx')


def directifclicked(cin):
    st.session_state['cin'] = cin
    st.session_state.button_clicked = True
    
    
    




# Step 1: Input CIN Number page

cin = "L25209DD1992PLC009784"

#st.text_input("CIN NUMBER", key="CIN")

# Once the user puts in the number & clicks enter it should open up the table of 10 random options for the CIN number industry code

statedata = pd.read_excel("/Users/neelpalle/Desktop/dbproject/test1.xlsx")


similarcin = similarsearch(cin,statedata)

st.write(similarcin)

i = 0 

st.session_state.button_clicked = False

for i in range(1):
    cin = similarcin.iloc[i,0]
    name = similarcin.iloc[i,1]
    #st.button(name, key = cin, on_click = directifclicked, args= [cin])
    if st.button(name):
        st.session_state['cin'] = cin
        st.switch_page("pages/companyprofile.py")


#while True:
    #if st.session_state.button_clicked:
        #st.switch_page("pages/companyprofile.py") # loading the company profile page














