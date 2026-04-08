import streamlit as st
import pandas as pd
from environment import DataEnv

df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip().str.replace(" ", "_")

env = DataEnv(df)

st.title("AI Data Analytics Environment 🚀")

if st.button("Run Tasks"):
    score = 0

    for _ in range(3):
        task = env.reset()
        st.write("Task:", task)

        if task == "Total Sales":
            ans = df["Global_Sales"].sum()
        elif task == "Top Category":
            ans = df.groupby("Genre")["Global_Sales"].sum().idxmax()
        else:
            ans = df.groupby("Genre")["Global_Sales"].sum().idxmin()

        result = env.step(ans)

        st.write("Reward:", result["reward"])
        score += result["reward"]

    st.success(f"Final Score: {score}/3")