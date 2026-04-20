import streamlit as st
import pandas as pd
import plotly.express as px #Dynamic Data Visualization tool

st.title("Cricket info app")

def load_data(file_path):
    df=pd.read_csv(file_path)
    return df

data_path="./newfile.csv"

df=load_data(data_path)

#st.dataframe(df)

matches=df.groupby("Country")["Matches"].sum().sort_values().reset_index()

st.sidebar.header("Filters")


country=st.sidebar.multiselect("select country",options=df["Country"].unique(),default=df["Country"].unique())
#duration=st.sidebar.slider("Select Duration",df["Duration"].min(),df["Duration"].max())
#player=st.sidebar.multiselect("Select Player")

filtered_df=df[
    (df["Country"].isin(country))
]

st.dataframe(filtered_df)


#metric - key perfomance indicator

total_runs=filtered_df["Runs"].sum()
total_matches=filtered_df["Matches"].sum()
total_hundreds=filtered_df["100"].sum()
total_sixes=filtered_df["6s"].sum()
total_player=filtered_df["Player"].nunique()

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.metric(label="Total Runs", value=total_runs)

with col2:
    st.metric(label="Matches", value=total_matches)

with col3:
    st.metric(label="Total Hundreds", value=total_hundreds)

with col4:
    st.metric(label="Total Sixes", value=total_sixes)

with col5:
    st.metric(label="Total Players", value=total_player)



fig_matches=px.pie(
    matches,
    names="Country",
    values="Matches",
    title="Country wise matches"
)

st.plotly_chart(fig_matches)

