import random

class DataEnv:
    
    def __init__(self, df):
        self.df = df
        self.tasks = [
            "Total Sales",
            "Top Category",
            "Lowest Profit Category"
        ]
        self.current_task = None
    
    def reset(self):
        self.current_task = random.choice(self.tasks)
        return self.current_task
    
    def step(self, action):
        if self.current_task == "Total Sales":
            correct = self.df["Sales"].sum()
        
        elif self.current_task == "Top Category":
            correct = self.df.groupby("Category")["Sales"].sum().idxmax()
        
        elif self.current_task == "Lowest Profit Category":
            correct = self.df.groupby("Category")["Profit"].sum().idxmin()
        
        if str(action).strip().lower() == str(correct).strip().lower():
            reward = 1
        else:
            reward = 0
        
        return {
            "task": self.current_task,
            "your_answer": action,
            "correct_answer": correct,
            "reward": reward
        }
    
    def state(self):
        return self.current_task