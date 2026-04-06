import pandas as pd
from environment import DataEnv

# Load data
df = pd.read_csv("Supermart Grocery Sales - Retail Analytics Dataset.csv")

# Create environment
env = DataEnv(df)

total_score = 0

for i in range(3):
    task = env.reset()
    print("\nTask:", task)
    
    if task == "Total Sales":
        answer = df["Sales"].sum()
    
    elif task == "Top Category":
        answer = df.groupby("Category")["Sales"].sum().idxmax()
    
    elif task == "Lowest Profit Category":
        answer = df.groupby("Category")["Profit"].sum().idxmin()
    
    result = env.step(answer)
    
    print("Answer:", answer)
    print("Reward:", result["reward"])
    
    total_score += result["reward"]

print("\nFinal Score:", total_score)