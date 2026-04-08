import os
import pandas as pd
from environment import DataEnv

# ENV variables (mandatory)
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
HF_TOKEN = os.getenv("HF_TOKEN")

print("[START]")

df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip().str.replace(" ", "_")

env = DataEnv(df)

total_score = 0

for i in range(3):
    task = env.reset()
    print(f"[STEP] Task {i+1}: {task}")

    if task == "Total Sales":
        ans = df["Global_Sales"].sum()
    elif task == "Top Category":
        ans = df.groupby("Genre")["Global_Sales"].sum().idxmax()
    else:
        ans = df.groupby("Genre")["Global_Sales"].sum().idxmin()

    result = env.step(ans)
    reward = result["reward"]

    print(f"Answer: {ans}")
    print(f"Reward: {reward}")

    total_score += reward

print(f"Final Score: {total_score}/3")
print("[END]")
